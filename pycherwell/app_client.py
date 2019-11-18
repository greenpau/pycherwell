#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (C) 2019 Paul Greenberg @greenpau
See LICENSE for licensing details
'''

from __future__ import (absolute_import, division, print_function)
import os
import sys
import stat
import re
import json
import yaml
import logging
import pprint

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from pycherwell import ApiClient, Configuration, ServiceApi, BusinessObjectApi, ApiException
from pycherwell.app_configuration import AppConfiguration
import urllib3
urllib3.disable_warnings()
import requests
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

__author__ = "Paul Greenberg @greenpau"
__version__ = u'1.0.1'
__maintainer__ = "Paul Greenberg"
__email__ = "greenpau@outlook.com"
__status__ = "Alpha"

class CherwellClient(object):
    '''
    This class implements the client application.
    '''

    def __init__(self):
        ''' Initializes the class. '''
        self.log = logging.getLogger('cherwell-client')
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(name)s@%(lineno)d: %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.debug_enabled = False
        self.output_format = 'json'
        self.api_configuration = None
        self.api_client = None
        self.profile='default'
        self.config_file=None
        self._is_configured = False
        self.auth_token = None
        self.user_agent = None
        self._authenticated = False
        return

    def set_config_file(self, config_file):
        self.config_file = config_file

    def set_profile(self, profile='default'):
        self.profile = profile

    def _configure(self):
        self.config = AppConfiguration(self.config_file, self.profile)
        if self.debug_enabled:
            self.config.log.setLevel(logging.DEBUG)
            self.config.debug_enabled = True
        self.config.load()
        self.api_configuration = Configuration()
        if self.debug_enabled:
            self.api_configuration.debug = True
        self.api_configuration.verify_ssl = self.config.get_verify_ssl()
        self.api_configuration.ssl_ca_cert = self.config.get_ssl_ca_cert()
        self.api_configuration.assert_hostname = self.config.get_assert_hostname()
        self.api_configuration.connection_pool_maxsize = self.config.get_connection_pool_maxsize()
        self.api_configuration.proxy = self.config.get_proxy()
        self.api_configuration.cert_file = self.config.get_cert_file()
        self.api_configuration.key_file = self.config.get_key_file()
        self.api_configuration.safe_chars_for_path_param = self.config.get_safe_chars_for_path_param()
        self.api_configuration.host = self.config.get_host()
        self.user_agent = self.config.get_user_agent()
        return

    def _enable(self):
        if not self._is_configured:
            self._configure()
            self._is_configured = True
        if not self.auth_token:
            self._authenticate()
        if not self._authenticated:
            raise Exception('client', 'not authenticated')
        self.api_client = ApiClient(
            configuration = self.api_configuration,
            header_name=self.config.get_auth_header_name(),
            header_value=self.config.get_auth_header_value(),
        )
        self.api_client.user_agent = self.config.get_user_agent()
        return

    def debug(self):
        if self.debug_enabled:
            return
        http_client.HTTPConnection.debuglevel = 5
        self.log.setLevel(logging.DEBUG)
        self.debug_enabled = True
        return

    def set_output_format(self, output_format='json'):
        self.output_format = output_format

    def get_version(self):
        self._configure()
        return self.user_agent

    @staticmethod
    def _wrap_return(opts, container, data):
        if 'without_header' in opts:
            return data
        return {container: data}

    def get_service_info(self, opts={}):
        data = {}
        api_response = None
        self._enable()
        try:
            api_instance = ServiceApi(self.api_client)
            api_response = api_instance.service_get_service_info_v1()
        except ApiException as e:
            self.log.error('Exception when calling ServiceApi->service_get_service_info_v1: %s', e)
            return data
        '''
        data['api_version'] = api_response.api_version
        data['csm_culture'] = api_response.csm_culture
        data['csm_version'] = api_response.csm_version
        data['system_date_time'] = str(api_response.system_date_time)
        '''
        data = api_response.to_dict()
        data['system_date_time'] = str(data['system_date_time'])
        return self._wrap_return(opts, 'service_info', data)

    def get_business_object_summaries(self, opts={}):
        data = []
        api_response = None
        summary_type = 'Major'
        if 'summary_type' in opts:
            if opts['summary_type'] not in ['All', 'Major', 'Lookup', 'Supporting', 'Groups']:
                raise Exception('client', 'Unsupported summary type: %s' % (opts['summary_type']))
            summary_type = opts['summary_type']
        self._enable()
        try:
            api_instance = BusinessObjectApi(self.api_client)
            api_response = api_instance.business_object_get_business_object_summaries_v1(summary_type)
        except ApiException as e:
            self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_summaries_v1: %s', e)
            return data
        for entry in api_response:
            data.append(entry.to_dict())
        if 'save_app_section' in opts and summary_type == 'All':
            self.config.save_app_section('summaries', data)
        return self._wrap_return(opts, 'business_object_summaries', data)

    def get_incident(self, opts={}):
        data = {}
        api_response = None
        if 'incident_id' not in opts:
            raise Exception('client', 'incident_id not found')
        incident_id = str(opts['incident_id'])
        self._enable()
        if not self.config.app['summaries']:
            self.get_business_object_summaries({'summary_type': 'All', 'save_app_section': True})


        
        raise Exception('xxx', self.config.app['summaries'])
            
        raise Exception('xxx', 'xxx')

        try:
            api_instance = BusinessObjectApi(self.api_client)
            api_response = api_instance.business_object_get_business_object_summary_by_id_v1(incident_id)
        except ApiException as e:
            self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_summary_by_id_v1: %s', e)
            return data
        import pprint
        pprint.pprint(api_response)
        data = api_response
        return data

    def _authenticate(self):
        ''' Get cached authentication parameters '''
        self.auth_token = self.config.get_auth_token()
        if self.auth_token:
            self.log.debug("Found cached auth token %s", self.auth_token)
            self._authenticated = True
            return
        self.log.debug("Cached auth token not found")
        headers = {
            "Accept-Charset": "utf-8",
            "Accept-Encoding": "gzip, deflate, compress",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            'User-Agent': self.user_agent,
        }
        url = self.config.get_auth_url()
        if not url:
            raise Exception('client', 'authentication URL is empty')
        self.log.debug("Authentication URL: %s", url)
        fields = self.config.get_auth_req_fields()
        if not fields:
            raise Exception('client', 'authentication request fields are empty')
        self.log.debug('Authentication request fields: %s', fields)
        session = requests.Session()
        req = session.post(url, headers=headers, data=fields, verify=False)
        if req.status_code != 200:
            raise Exception('client', '%d: %s, message: %s' % (req.status_code, req.reason, req.text))
        self.log.debug("Authenticator response: %d %s", req.status_code, req.text)
        data = json.loads(req.text)
        if 'access_token' not in data:
            raise Exception('client', 'access_token is not in the response from authenticator')
        self.auth_token = data
        self._authenticated = True
        self.config.save_app_section('token', data)
        return

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

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

#import pycherwell
#from pycherwell.rest import ApiException
from pycherwell import ApiClient, Configuration, ServiceApi, ApiException
from pycherwell.app_configuration import AppConfiguration
import urllib3
urllib3.disable_warnings()
import requests
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

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
        self.config_file="~/.pycherwell.rc"
        self._is_configured = False
        self.auth_token = None
        self.user_agent = None
        self._authenticated = False
        return

    def set_config_file(self, config_file = "~/.pycherwell.rc"):
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

    def _decode_response(self, data):
        response = {}
        if self.output_format not in ['json', 'yaml']:
            return {}
        try:
            response = yaml.load('%s' % (data), Loader=yaml.FullLoader)
            #response = self._remove_unicode(response)
        except:
            self.log.error('erred processing data: %s', data)
            return {}
        return response

    def get_version(self):
        self._configure()
        return self.user_agent

    def _remove_unicode(self, data):
        if isinstance(data, (dict)):
            new_data = {}
            for k in data:
                if isinstance(k, (unicode)):
                    new_data[str(k)] = self._remove_unicode(data[k])
                    continue
                new_data[k] = self._remove_unicode(data[k])
            return new_data
        if isinstance(data, (list)):
            new_data = []
            for entry in data:
                new_data.append(self._remove_unicode(entry))
            return new_data
        elif isinstance(data, (unicode)):
            s = ''
            try:
                s = str(data)
            except:
                s = ''.join([i if ord(i) < 128 else ' ' for i in data])
            return str(s)
        elif isinstance(data, (long)):
            return str(data)
        elif isinstance(data, (datetime)):
            return (data - datetime(1970,1,1)).total_seconds()
        else:
            pass
        return data

    def get_service_info(self, opts={}):
        api_response = None
        self._enable()
        try:
            api_instance = ServiceApi(self.api_client)
            api_response = api_instance.service_get_service_info_v1()
        except ApiException as e:
            self.log.error('Exception when calling ServiceApi->service_get_service_info_v1: %s' % e)
        data = self._decode_response(api_response)
        return {'service_info': data}

    def get_incident(self, opts={}):
        if 'incident_id' not in opts:
            raise Exception('client', 'incident_id not found')
        incident_id = opts['incident_id']
        self._enable()
        data = incident_id

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
        self.config.save_token(data)
        return

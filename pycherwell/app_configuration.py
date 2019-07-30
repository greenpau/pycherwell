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
import logging
import ConfigParser
import base64
import re
import pprint
import time
import json

class AppConfiguration(object):
    '''
    This class implements the client application configuration.
    '''

    def __init__(self, config_file, profile):
        ''' Initializes the class. '''
        self.config_file = config_file
        self.profile = profile
        self.settings = {}
        self.log = logging.getLogger('cherwell-config')
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(name)s@%(lineno)d: %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.debug_enabled = False
        self.cfg_keys = [
            'client_id',
            'auth_mode',
            'username',
            'password',
            'host',
            'port',
            'protocol',
            'basepath'
        ]
        self.env_key_pairs = []
        for k in self.cfg_keys:
            self.env_key_pairs.append(('CHERWELL_%s' % (k.upper()), k))
        self.verify_ssl = False
        self.ssl_ca_cert = False
        self.assert_hostname = None
        self.connection_pool_maxsize = 4
        self.proxy = None
        self.cert_file = None
        self.key_file = None
        self.safe_chars_for_path_param = ''
        self.token_file_name = os.path.expanduser('~/.pycherwell.token')
        self.token = None
        return


    def load(self):
        cfg_file = self.config_file
        ''' Load configuration from a configuration file in RC format. '''
        if not self.config_file:
            cfg_file = '~/.pycherwell.rc'
        cfg_file = os.path.expanduser(cfg_file)
        self.log.debug('configuration file: %s', cfg_file)

        _has_cfg_file = True
        if not os.path.exists(cfg_file):
            self.log.debug('configuration file: %s does not exist ', cfg_file)
            _has_cfg_file = False

        ''' Validate configuration file permissions '''
        if _has_cfg_file:
            cfg_file_stat = os.stat(cfg_file)
            if cfg_file_stat.st_mode & stat.S_IROTH:
                raise Exception('config', 'configuration file %s is world readable' % cfg_file)
            if cfg_file_stat.st_mode & stat.S_IRGRP:
                raise Exception('config', 'configuration file %s is group readable' % cfg_file)

        ''' Handle configuration file '''
        if _has_cfg_file:
            self.cfg_file = cfg_file
            cfg_parser = ConfigParser.RawConfigParser()
            cfg_parser.read(cfg_file)
            if self.profile not in cfg_parser.sections():
                raise Exception('config', 'configuration file %s has no %s section' % (cfg_file, self.profile))
            for cfg_key in self.cfg_keys:
                if cfg_parser.has_option(self.profile, cfg_key):
                    self.settings[cfg_key] = cfg_parser.get(self.profile, cfg_key)
                    cfg_value = self.settings[cfg_key]
                    if re.match('password', cfg_key):
                        cfg_value = "*************"
                    self.log.debug('config file: key = %s, value = %s', cfg_key, cfg_value)

        ''' Handle environment variables '''
        for env_key_pair in self.env_key_pairs:
            if not os.environ.get(env_key_pair[0]):
                continue
            cfg_key = env_key_pair[1]
            cfg_value = os.environ.get(env_key_pair[0])
            self.settings[cfg_key] = cfg_value
            if re.match('password', cfg_key):
                cfg_value = "*************"
            self.log.debug('environment var: key = %s, value = %s', cfg_key, cfg_value)

        self.validate()
        return

    def validate(self):
        '''
        Validates that all configuration parameters necessary to establish
        a connection to SEP Manager are present.
        '''
        for cfg_key in self.cfg_keys:
            if cfg_key not in self.settings:
                if cfg_key == 'protocol':
                    self.settings[cfg_key] = 'https'
                elif cfg_key == 'port':
                    self.settings[cfg_key] = '443'
                elif cfg_key == 'basepath':
                    self.settings[cfg_key] = '/CherwellAPI'
                elif cfg_key == 'host':
                    self.settings[cfg_key] = 'localhost'
                else:
                    raise Exception('config', \
                            "no '%s' key in '%s' " % (cfg_key, self.profile) + \
                            "section of the configuration")
            else:
                self.settings[cfg_key] = self.settings[cfg_key].strip("'").strip('"')
        return

    def get_host(self):
        if self.settings['protocol'] == 'https' and self.settings['port'] == '443':
            return '%s://%s/%s' % (self.settings['protocol'], self.settings['host'], self.settings['basepath'])
        else:
            return '%s://%s:%s/%s' % (self.settings['protocol'], self.settings['host'], self.settings['port'], self.settings['basepath'])

    def get_auth_url(self):
        ''' Return base path URL. '''
        base = self.get_host()
        base += '/token?'
        base += 'auth_mode=' + self.settings['auth_mode']
        base += '&api_key=' + self.settings['client_id']
        return base

    def get_auth_req_fields(self):
        fields = {}
        fields['grant_type'] = 'password'
        if self.settings['auth_mode'] == 'LDAP':
            fields['client_id'] = self.settings['client_id']
            fields['username'] = self.settings['username']
            fields['password'] = self.settings['password']
        return fields

    def get_verify_ssl(self):
        return self.verify_ssl

    def get_ssl_ca_cert(self):
        return self.ssl_ca_cert

    def get_assert_hostname(self):
        return self.assert_hostname

    def get_connection_pool_maxsize(self):
        return self.connection_pool_maxsize

    def get_proxy(self):
        return self.proxy

    def get_cert_file(self):
        return self.cert_file

    def get_key_file(self):
        return self.key_file

    def get_safe_chars_for_path_param(self):
        return self.safe_chars_for_path_param

    def set_verify_ssl(self, param=False):
        self.verify_ssl = param
        return

    def set_ssl_ca_cert(self, param=False):
        self.ssl_ca_cert = param
        return

    def set_assert_hostname(self, param=None):
        self.assert_hostname = param
        return

    def set_connection_pool_maxsize(self, param=4):
        self.connection_pool_maxsize = param
        return

    def set_proxy(self, param=None):
        self.proxy = param
        return

    def set_cert_file(self, param=None):
        self.cert_file = param
        return

    def set_key_file(self, param=None):
        self.key_file = param
        return

    def set_safe_chars_for_path_param(self, param=''):
        self.safe_chars_for_path_param = param
        return

    def get_auth_header_name(self):
        return 'Authorization'

    def get_auth_header_value(self):
        return 'Bearer %s' % (self.token['access_token'])

    def get_user_agent(self):
        return 'pycherwell/1.0'

    def get_auth_token(self):
        self.log.debug('Authentication token file path: %s', self.token_file_name)
        if os.path.exists(self.token_file_name):
            if os.stat(self.token_file_name).st_size > 100:
                with open(self.token_file_name, 'r') as token_file:
                    self.token = json.load(token_file)
                    self.log.debug('Authentication token: %s', self.token)
        return self.token

    def save_token(self, data):
        self.log.debug('Saving auth token in %s', self.token_file_name)
        data['expires_in_timestamp'] = int(time.time()) + data['expires_in']
        self.token = data
        with open(self.token_file_name, 'w') as f:
            json.dump(data, f)
            f.write('\n')
        return

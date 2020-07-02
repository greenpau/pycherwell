#!/usr/bin/env python3
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
try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser  # ver. < 3.0
import base64
import re
import pprint
import time
import json

__pkg_name__ = 'pycherwell'
__author__ = 'Paul Greenberg @greenpau'
__version__ = u'1.0.1'
__maintainer__ = 'Paul Greenberg'
__email__ = 'greenpau@outlook.com'
__status__ = 'Alpha'

class AppConfiguration(object):
    '''
    This class implements the client application configuration.
    '''

    def __init__(self, config_file, profile):
        ''' Initializes the class. '''
        self.app_name = __pkg_name__
        self.app_version = __version__
        self.config_file = config_file
        if not self.config_file:
            self.app_conf_dir = os.path.expanduser('~/.%s' % (self.app_name.lstrip('py')))
            self.config_file = os.path.join(self.app_conf_dir, 'config')
        else:
            self.app_conf_dir = os.path.dirname(config_file)
        self.profile = profile
        self.settings = {}
        self.log = logging.getLogger('%s-config' % (self.app_name))
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
            self.env_key_pairs.append(('%s_%s' % (self.app_name, k.upper()), k))
        self.verify_ssl = False
        self.ssl_ca_cert = False
        self.assert_hostname = None
        self.connection_pool_maxsize = 4
        self.proxy = None
        self.cert_file = None
        self.key_file = None
        self.safe_chars_for_path_param = ''
        self.app_conf_file_names = {
            'token': os.path.join(self.app_conf_dir, 'token.json'),
            'business_objects': os.path.join(self.app_conf_dir, 'business_objects.json'),
            'teams': os.path.join(self.app_conf_dir, 'teams'),
        }
        self.app = {}
        for k in self.app_conf_file_names:
            self.app[k] = None
        return


    def load(self):
        cfg_file = self.config_file
        ''' Load configuration from a configuration file in RC format. '''
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
            cfg_parser = RawConfigParser()
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
        if self.settings['auth_mode'].lower() in ['internal', 'ldap']:
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
        return 'Bearer %s' % (self.app['token']['access_token'])

    def get_user_agent(self):
        return '%s/%s' % (self.app_name, self.app_version)

    def get_auth_token(self):
        self.load_app_section('token')
        self.log.debug('Authentication token: %s', self.app['token'])
        if self.app['token'] is not None:
            if 'expires_at_timestamp' not in self.app['token']:
                self.app['token'] = None
                self.wipe_app_section('token')
                return self.app['token']
            if int(time.time()) > self.app['token']['expires_at_timestamp']:
                self.app['token'] = None
                self.wipe_app_section('token')
                return self.app['token']
        return self.app['token']


    def enrich_app_section(self, section):
        if section not in ['business_objects']:
            return
        ref_section = section + '_ref'
        if ref_section not in self.app:
            self.app[ref_section] = {}
        mandatory_fields = ['bus_ob_id', 'name', 'major']
        for entry in self.app[section]:
            is_valid_entry = True
            for f in mandatory_fields:
                if f not in entry:
                    is_valid_entry = False
                    break
            if not is_valid_entry:
                continue
            if entry['major'] != True:
                continue
            self.app[ref_section][entry['name']] = entry
        return

    def get_business_object(self, name):
        if name in self.app['business_objects_ref']:
            return self.app['business_objects_ref'][name]['bus_ob_id']
        return None


    def load_app_section(self, section):
        if section not in self.app_conf_file_names:
            self.log.error('The app config %s section is unsupported', section)
            return False
        if section in self.app:
            if self.app[section] is not None:
                return True
        fn = self.app_conf_file_names[section]
        if os.path.exists(fn):
            if os.stat(fn).st_size > 100:
                with open(fn, 'r') as f:
                    self.app[section] = json.load(f)
                self.log.debug('Loaded app config %s section from %s', section, fn)
                self.enrich_app_section(section)
        return True

    def save_app_section(self, section, data):
        if section not in self.app_conf_file_names:
            self.log.error('The app config %s section is unsupported', section)
            return
        fn = self.app_conf_file_names[section]
        self.log.debug('Saving app config %s section from %s', section, fn)
        try:
            if not os.path.exists(self.app_conf_dir):
                os.makedirs(self.app_conf_dir)
        except:
            pass
        if section == 'token':
            data['expires_at_timestamp'] = int(time.time()) + data['expires_in']
        with open(fn, 'w') as f:
            formatted_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            f.write(formatted_data)
            f.write('\n')
        self.app[section] = data
        return

    def wipe_app_section(self, section):
        if section not in self.app_conf_file_names:
            self.log.error('The app config %s section is unsupported', section)
            return
        fn = self.app_conf_file_names[section]
        with open(fn, 'w') as f:
            pass
        self.app[section] = None
        return

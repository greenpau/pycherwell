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
import copy
import logging
import textwrap
from datetime import datetime, timedelta
from pprint import pprint

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from pycherwell import ApiClient, Configuration, ApiException
from pycherwell import BusinessObjectApi, TemplateRequest, SaveRequest, FieldTemplateItem
from pycherwell import SearchesApi, SearchResultsRequest, FilterInfo
from pycherwell import TeamsApi
from pycherwell import ServiceApi
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

    def _enable(self, opts={}):
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
        app_sections = [
            'business_objects',
            'teams',
        ]
        for app_section in app_sections:
            loaded = self.config.load_app_section(app_section)
            self.log.debug('the %s section data was not loaded from cache', app_section)
        return

    def _ensure_required_business_objects(self, app_sections=[], opts={}):
        for app_section in app_sections:
            self.log.debug('ensuring required section exists in cache: %s', app_section)
            if self.config.app[app_section]:
                continue
            if app_section == "business_objects":
                self.get_business_object_summaries({
                    'save_app_section': True,
                    'summary_type': 'All'
                })
            elif app_section == "teams":
                self.get_teams()
            else:
                raise Exception('client', '_ensure_required_business_objects does not support %s section' % (app_section))

            loaded = self.config.load_app_section(app_section)
            if not loaded:
                raise Exception('client', '_ensure_required_business_objects() failed to load %s section' % (app_section))

    def _ensure_required_business_object_fields(self, business_objects=[], opts={}):
        for business_object_name in business_objects:
            self.log.debug('ensuring business object fields exist in cache: %s', business_object_name)
            business_object_id = self.config.get_business_object_id(business_object_name)
            if not business_object_id:
                raise Exception('client', 'failed finding ID for BO %s' % (business_object_name))

            business_object_fields = self.get_business_object_fields({'business_object_id': business_object_id})
            if not business_object_fields:
                raise Exception('client', '_ensure_required_business_object_fields() failed for BO %s' % (business_object_name))
        return

    def _ensure_required_business_object_templates(self, business_objects=[], opts={}):
        for business_object_name in business_objects:
            self.log.debug('ensuring business object templates exist in cache: %s', business_object_name)
            business_object_id = self.config.get_business_object_id(business_object_name)
            if not business_object_id:
                raise Exception('client', 'failed finding ID for BO %s' % (business_object_name))

            business_object_template = self.get_business_object_template({'business_object_id': business_object_id})
            if not business_object_template:
                raise Exception('client', '_ensure_required_business_object_templates() failed for BO %s' % (business_object_name))
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
            self.config.save_app_section('business_objects', data)
        return self._wrap_return(opts, 'business_object_summaries', data)


    def get_business_object_fields(self, opts={}):
        self._enable()
        if 'business_object_id' not in opts:
            raise Exception('client', 'get_business_object_fields() requires business_object_id')
        business_object_id = opts['business_object_id']
        if 'business_object_fields_ref' in self.config.app:
            if business_object_id in self.config.app['business_object_fields_ref']:
                return self.config.app['business_object_fields_ref'][business_object_id]
        loaded = self.config.load_app_data('business_object_fields_ref', business_object_id)
        if loaded:
            return self.config.app['business_object_fields_ref'][business_object_id]
        api_response = None
        try:
            api_instance = BusinessObjectApi(self.api_client)
            api_response = api_instance.business_object_get_business_object_schema_v1(business_object_id)
        except ApiException as e:
            self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_summaries_v1: %s', e)
            return False
        api_response = api_response.to_dict()
        if 'field_definitions' not in api_response:
            err = 'field_definitions not found in API response'
            self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_summaries_v1: %s', err)
            return False

        self.config.save_app_data('business_object_fields_ref', business_object_id, api_response['field_definitions'])
        return self.config.app['business_object_fields_ref'][business_object_id]

    def get_business_object_template(self, opts={}):
        self._enable()
        if 'business_object_id' not in opts:
            raise Exception('client', 'get_business_object_template() requires business_object_id')
        business_object_id = opts['business_object_id']
        if 'business_object_template_ref' in self.config.app:
            if business_object_id in self.config.app['business_object_template_ref']:
                return self.config.app['business_object_template_ref'][business_object_id]
        loaded = self.config.load_app_data('business_object_template_ref', business_object_id)
        if loaded:
            return self.config.app['business_object_template_ref'][business_object_id]

        template_fields = None
        required_template_fields = {}

        for i in [1, 2]:
            api_response = None
            kwargs = {
                'bus_ob_id': business_object_id,
                'include_all': True,
                'include_required': True,
            }
            if i == 2:
                kwargs['include_all'] = False
            try:
                template_request = TemplateRequest(**kwargs)
                api_instance = BusinessObjectApi(self.api_client)
                api_response = api_instance.business_object_get_business_object_template_v1(template_request)
            except ApiException as e:
                self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_template_v1: %s', e)
                return False
            api_response = api_response.to_dict()
            if 'fields' not in api_response:
                err = 'fields not found in API response'
                self.log.error('Exception when calling BusinessObjectApi->business_object_get_business_object_template_v1: %s', err)
                return False

            if i == 1:
                template_fields = api_response['fields']
                continue

            for field in api_response['fields']:
                if 'field_id' not in field:
                    continue
                required_template_fields[field['field_id']] = True

        for i, field in enumerate(template_fields):
            if 'field_id' not in field:
                continue
            if field['field_id'] in required_template_fields:
                template_fields[i]['required'] = True
            else:
                template_fields[i]['required'] = False

        self.config.save_app_data('business_object_template_ref', business_object_id, template_fields)
        return self.config.app['business_object_template_ref'][business_object_id]

    def get_incident(self, opts={}):
        """lookup an incident by human visible id (publicid).

        Note: only a single dict is returned.

        Args:
            opts: List of options to perform lookup.

        Returns:
            returns a single dict containing the incident information.

        """

        api_response = None
        if 'incident_id' not in opts:
            raise Exception('client', 'incident_id not found')
        incident_id = str(opts['incident_id'])
        self._enable()
        self._ensure_required_business_objects(['business_objects'])
        self._ensure_required_business_object_fields(['Incident'], opts)

        busObId = self.config.get_business_object_id('Incident')
        if not busObId:
            raise Exception('internal','Failed to find business object ID of Incident Type')
        
        apiName = 'BusinessObjectApi'
        apiFunc = 'business_object_get_business_object_by_public_id_v1'

        try:
            api_instance = BusinessObjectApi(self.api_client)
            api_response = getattr(api_instance, apiFunc)(busObId, incident_id)
            api_response = api_response.to_dict()
        except ApiException as e:
            if 'RECORDNOTFOUND' in str(e):
                self.log.warn("Incident ID %s not found", incident_id)
                return
            self.log.error('Exception when calling %s->%s: %s', apiName, apiFunc, e)
            return

        if 'bus_ob_public_id' not in api_response:
            self.log.warn("Incident ID %s not found", incident_id)
            return

        if 'output_format' in opts and opts['output_format'] in ['csv', 'text']:
            rows = []
            if 'fields' not in api_response:
                self.log.warn("Incident ID %s has no data: %s", incident_id, api_response)
                return
            if opts['output_format'] == 'text':
                incident_type = self._get_field_value(api_response['fields'], ('display_name', 'value', 'Incident Type'))
                rows.append(['', '%s # %s' % (incident_type, incident_id)])
                rows.extend(self._serialize_kv(api_response['fields'], ('display_name', 'value'), opts))
            elif opts['output_format'] == 'csv':
                rows.append(self._get_csv_headers(api_response['fields'], 'display_name'))
                rows.append(self._get_csv_columns(api_response['fields'], api_response['fields']))
            else:
                pass
            return rows
        return api_response

    def get_teams(self, opts={}):
        teams = []
        api_response = None
        self._enable()
        try:
            api_instance = TeamsApi(self.api_client)
            api_response = api_instance.teams_get_teams_v2()
        except ApiException as e:
            self.log.error('Exception when calling TeamsApi->teams_get_teams_v2: %s', e)
            return teams
        api_response = api_response.to_dict()
        if 'teams' not in api_response:
            self.log.error('The response from TeamsApi->teams_get_teams_v2() did not contain teams key')
            return teams
        if len(api_response['teams']) == 0:
            self.log.error('The response from TeamsApi->teams_get_teams_v2() had no teams')
            return teams

        if 'output_format' in opts and opts['output_format'] in ['csv', 'text']:
            teams.append(['Team Name', 'UUID'])

        for team in api_response['teams']:
            if 'output_format' in opts and opts['output_format'] in ['csv', 'text']:
                try:
                    teams.append([team['team_name'], team['team_id']])
                except:
                    pass
            else:
                teams.append(team)
        self.config.save_app_section('teams', api_response['teams'])
        return teams

    def get_journal(self, opts={}):
        api_response = None
        if 'incident_id' not in opts:
            raise Exception('client', 'incident_id not found')
        incident_id = str(opts['incident_id'])
        self._enable()
        self._ensure_required_business_objects(['business_objects'])
        self._ensure_required_business_object_fields(['Incident', 'Journal'], opts)

        busObId = self.config.get_business_object_id('Incident')
        if not busObId:
            raise Exception('internal', 'Failed to find business object ID of Incident Type')
        jbusObId = self.config.get_business_object_id('Journal')
        if not jbusObId:
             raise Exception('internal', 'Failed to find business object ID of Journal Type')
        self.log.debug("Get journal (%s) for incident %s (%s)", jbusObId, incident_id, busObId)

        apiName = 'BusinessObjectApi'
        apiFunc = 'business_object_get_business_object_by_public_id_v1'

        try:
            # First, get business object id
            api_instance = BusinessObjectApi(self.api_client)
            api_response = getattr(api_instance, apiFunc)(busObId, incident_id)
            api_response = api_response.to_dict()
            busRecId = api_response['bus_ob_rec_id']
            # Next, search by the business object id
            apiName = 'SearchesApi'
            apiFunc = 'searches_get_search_results_ad_hoc_v1'
            busObFilter = self._build_filter('RecID:eq:' + busRecId, busObId)
            busObFilters = [busObFilter]
            if 'search_conditions' in opts:
                for search_condition in opts['search_conditions']:
                    busObFilter = self._build_filter(search_condition, jbusObId)
                    if busObFilter:
                        busObFilters.append(busObFilter)
            kwargs = {
                'bus_ob_id': jbusObId,
                'filters': busObFilters,
                'include_all_fields': True,
            }
            search_request = SearchResultsRequest(**kwargs)
            api_instance = SearchesApi(self.api_client)
            api_response = getattr(api_instance, apiFunc)(search_request)
            api_response = api_response.to_dict()
            api_response = api_response['business_objects']
        except ApiException as e:
            if 'RECORDNOTFOUND' in str(e):
                self.log.warn("Incident ID %s not found", incident_id)
                return
            self.log.error('Exception when calling %s() via %s API: %s', apiFunc, apiName, e)
            return

        records = []
        record_fields = [
            'Created Date Time',
            'Created By',
            'Journal Type Name',
            'Details',
        ]
        for record in api_response:
            if 'fields' not in record:
                continue
            parsed_record = self._parse_record_fields(record['fields'], record_fields)
            records.append(parsed_record)

        if opts['output_format'] not in ['csv', 'text']:
            return records

        if 'output_format' in opts and opts['output_format'] in ['csv', 'text']:
            rows = []
            rows.append(record_fields)
            opts['column_width_allocation'] = [10, 10, 10, 70]
            if opts['output_format'] == 'text':
                column_width_allocation = self._get_column_width(record_fields, records, opts)
            for record in records:
                row = []
                for i, field in enumerate(record_fields):
                    if field in record:
                        v = record[field]
                        if opts['output_format'] == 'text':
                            if len(v) > column_width_allocation[i]:
                                v = '\n'.join(textwrap.wrap(v, width=column_width_allocation[i]))
                                v = v.replace('  ', '\n')
                        row.append(v)
                        continue
                    row.append('---')
                rows.append(row)
            return rows
        return records

    @staticmethod
    def _get_column_width(columns, entries, opts={}):
        width = {}
        max_width = 120
        if 'terminal_columns' in opts and opts['terminal_columns'] > 0:
            max_width = opts['terminal_columns'] - (len(columns) * 4)
        for i, column in enumerate(columns):
            column_width = max_width / 100 * opts['column_width_allocation'][i]
            width[i] = int(column_width)
        return width

    @staticmethod
    def _parse_record_fields(entries=[], fields=None):
        record = {}
        for entry in entries:
            if fields and entry['display_name'] not in fields:
                continue
            record[entry['display_name']] = entry['value']
        return record

    @staticmethod
    def _time_travel_snapshot(unit, count, measure='seconds'):
        if unit not in ['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']:
            return None
        if unit == 'minute':
            multiplier = 60
        elif unit == 'hour':
            multiplier = 3600
        elif unit == 'day':
            multiplier = 86400
        elif unit == 'week':
            multiplier = 604800
        elif unit == 'month':
            multiplier = 2.628e+6
        elif unit == 'quarter':
            multiplier = 7.884e+6
        elif unit == 'year':
            multiplier = 3.154e+7
        seconds = int(count) * multiplier
        return seconds

    def _build_filter(self, s, busObId):
        parts = s.split(':')
        if len(parts) < 3:
            raise Exception('parameters', 'invalid filter string: %s' % (s))
        field_id = parts[0]
        conditional = parts[1]
        value = None
        if len(parts) == 3:
            value = parts[2]
        else:
            value = ':'.join(parts[2:])
        if ' ago' in value:
            value = value.lower()
            m = re.match('(?P<count>\d+)\s+(?P<unit>minute|hour|day|week|month|quarter|year)[s]?\s+ago$', value)
            if not m:
                raise Exception('parameters', 'invalid filter string: %s' % (s))
            seconds = self._time_travel_snapshot(m.group('unit'), m.group('count'))
            if not seconds:
                raise Exception('parameters', 'invalid filter string: %s' % (s))
            ts = datetime.now() - timedelta(seconds=seconds)
            value = '%d/%d/%d 00:00:00 AM' % (ts.year, ts.month, ts.day)

        busObFieldId = self.config.get_business_object_field_id(busObId, field_id)
        kwargs = {
            'field_id': busObFieldId,
            'operator': conditional,
            'value': value,
        }
        return FilterInfo(**kwargs)

    def create_incident(self, opts={}):
        if 'create_as' not in opts:
            return {'error': 'no create-as found when creating the incident'}
        if 'create_fields' not in opts:
            return {'error': 'no create-fields found when creating the incident'}

        api_response = None
        self._enable()
        self._ensure_required_business_objects(['business_objects', 'teams'], opts)
        self._ensure_required_business_object_fields(['Incident', 'Customer'], opts)
        self._ensure_required_business_object_templates(['Incident'], opts)

        incidentBusObId = self.config.get_business_object_id('Incident')
        if not incidentBusObId:
            raise Exception('internal', 'Failed to find Incident business object ID')
        customerBusObId = self.config.get_business_object_id('Customer')
        if not customerBusObId:
            raise Exception('internal', 'Failed to find %s business object ID' % ('Customer'))
        incidentTemplate = self.get_business_object_template({'business_object_id': incidentBusObId})
        if not incidentTemplate:
            raise Exception('internal', 'Failed to find business object template for %s (%s)' % ('Incident', incidentBusObId))

        incidentFields = opts['create_fields']

        # customerBusOb = self.get_business_object('Customer', ...
        requestors = self.get_requestors({'search_conditions': opts['create_as']})
        if len(requestors) == 0:
            return {
                'error': 'requestor not found',
                'requestor_criteria': opts['create_as'],
            }
        elif len(requestors) > 1:
            return {
                'error': 'multiple requestors found',
                'requestor_criteria': opts['create_as'],
                'requestor_matches': requestors,
            }
        else:
            pass

        requestor = requestors[0]
        if  'bus_ob_rec_id' not in requestor:
            return {
                'error': 'requestor business object has no bus_ob_rec_id',
                'requestor': requestor,
            }

        incidentFields.append('Customer ID:%s' % (requestor['bus_ob_rec_id']))

        kwargs = {
            'bus_ob_id': incidentBusObId,
            'template': incidentTemplate,
            'fields': incidentFields,
        }
        result = self.create_business_object(**kwargs)

        return result

    def create_business_object(self, bus_ob_id=None, template=[], fields=[], opts={}):
        response = {}
        api_response = None
        if not bus_ob_id:
            raise Exception('internal', 'business object is None')
        if len(template) == 0:
            raise Exception('internal', 'business object template is empty')

        # Build input fields reference.
        input_fields = {}
        for entry in fields:
            parts = entry.split(':')
            if len(parts) != 2:
                if 'errors' not in response:
                    response['errors'] = []
                response['errors'].append('input field entry is invalid: %s' % (entry))
                continue
            if parts[0] in input_fields:
                if 'errors' not in response:
                    response['errors'] = []
                response['errors'].append('input field entry is duplicate: %s' % (entry))
                continue
            input_fields[parts[0]] = {'value': parts[1]}
        if 'Description' not in input_fields and 'ShortDescription' in input_fields:
            input_fields['Description'] = input_fields['ShortDescription']
        if 'ShortDescription' not in input_fields and 'Description' in input_fields:
            input_fields['ShortDescription'] = str(input_fields['Description']).split('\n')[0]

        if 'errors' in response:
            return response

        # Build template fields reference.
        template_fields = {}
        for entry in template:
            if 'field_id' not in entry:
                continue
            for k in ['name', 'display_name']:
                template_fields[entry[k]] = entry
            if 'required' in entry and entry['required'] == True:
                # required_found = False
                required_found = True
                for k in ['name', 'display_name']:
                    if entry[k] not in input_fields:
                        continue
                    required_found = True
                if not required_found:
                    if 'errors' not in response:
                        response['errors'] = []
                    response['errors'].append('required template field %s (%s) not found in input fields' % (entry['name'], entry['field_id']))

        # Check whether input fields are valid
        for k in input_fields:
            if k not in template_fields:
                if 'errors' not in response:
                    response['errors'] = []
                response['errors'].append('input field %s (%s) not found in template fields' % (k, input_fields[k]['value']))

        if 'errors' in response:
            return response

        # Build business object save request
        request_fields = []
        for k in input_fields:
            f = copy.deepcopy(template_fields[k])
            del f['required']
            f['value'] = input_fields[k]['value']
            f['field_id'] = 'BO:%s,FI:%s' % (bus_ob_id, template_fields[k]['field_id'])
            f['dirty'] = True
            ti = FieldTemplateItem(**f)
            request_fields.append(ti)

        # Perform request
        try:
            save_request = SaveRequest(bus_ob_id = bus_ob_id, fields=request_fields)
            api_instance = BusinessObjectApi(self.api_client)
            api_response = api_instance.business_object_save_business_object_v1(save_request)
        except ApiException as e:
            err_msg = None
            if 'errors' not in response:
                response['errors'] = []
            try:
                err_msg = json.loads(e.body)
            except:
                err_msg = 'Exception when calling BusinessObjectApi->business_object_save_business_object_v1: %s' % (e)
            response['errors'].append(err_msg)
            return response

        api_response = api_response.to_dict()
        for k in api_response:
            response[k] = api_response[k]
        return response

    def get_requestors(self, opts={}):
        response = {}
        if 'search_conditions' not in opts:
            raise Exception('internal', 'search conditions are required for searching requestor')
        api_response = None
        self._enable()
        self._ensure_required_business_objects(['business_objects'], opts)
        self._ensure_required_business_object_fields(['Customer'], opts)

        customerBusObId = self.config.get_business_object_id('Customer')
        if not customerBusObId:
            raise Exception('internal', 'Failed to find Customer business object ID')

        kwargs = {
            'bus_ob_id': customerBusObId,
        }

        busObFilters = []
        for search_condition in opts['search_conditions']:
            busObFilter = self._build_filter(search_condition, customerBusObId)
            if busObFilter:
                busObFilters.append(busObFilter)
        if not busObFilters:
            raise Exception('internal', 'failed to build search filters for Customer business object')

        kwargs = {
            'bus_ob_id': customerBusObId,
            'filters': busObFilters,
        }

        try:
            search_request = SearchResultsRequest(**kwargs)
            api_instance = SearchesApi(self.api_client)
            api_response = api_instance.searches_get_search_results_ad_hoc_v1(search_request)
        except ApiException as e:
            err_msg = None
            if 'errors' not in response:
                response['errors'] = []
            try:
                err_msg = json.loads(e.body)
            except:
                err_msg = 'Exception when calling SearchesApi->searches_get_search_results_ad_hoc_v1: %s' % (e)
            response['errors'].append(err_msg)
            return response

        api_response = api_response.to_dict()
        if 'business_objects' not in api_response:
            err_msg = 'Exception when calling SearchesApi->searches_get_search_results_ad_hoc_v1: business_objects not found'
            response['errors'] = [err_msg]
            return response

        return api_response['business_objects']


    def get_incidents(self, opts={}):
        incidents = []
        api_response = None
        self._enable()

        self._ensure_required_business_objects(['business_objects', 'teams'], opts)
        self._ensure_required_business_object_fields(['Incident'], opts)

        busObFields = []
        busObName = 'Incident'
        busObId = self.config.get_business_object_id(busObName)
        if not busObId:
            raise Exception('internal','Failed to find %s business object ID' % (busObName))

        kwargs = {'bus_ob_id': busObId}

        if 'search_conditions' in opts:
            busObFilters = []
            for search_condition in opts['search_conditions']:
                busObFilter = self._build_filter(search_condition, busObId)
                if busObFilter:
                    busObFilters.append(busObFilter)
            if busObFilters:
                kwargs['filters'] = busObFilters

        if 'search_fields' in opts:
            busObFieldIds = []
            for busObFieldName in opts['search_fields']:
                if busObFieldName not in busObFields:
                    busObFields.append(busObFieldName)
                busObFieldId = self.config.get_business_object_field_id(busObId, busObFieldName)
                if busObFieldId not in busObFieldIds:
                    busObFieldIds.append(busObFieldId)
            if busObFieldIds:
                kwargs['fields'] = busObFieldIds

        try:
            search_request = SearchResultsRequest(**kwargs)
            api_instance = SearchesApi(self.api_client)
            api_response = api_instance.searches_get_search_results_ad_hoc_v1(search_request)
        except ApiException as e:
            self.log.error('Exception when calling SearchesApi->searches_get_search_results_ad_hoc_v1: %s', e)
            return incidents
        api_response = api_response.to_dict()
        incidents = api_response['business_objects']
        if 'output_format' not in opts:
            return incidents
        if opts['output_format'] not in ['csv', 'text']:
            return incidents

        if 'output_format' in opts and opts['output_format'] in ['csv', 'text']:
            rows = []
            if not busObFields:
                for incident in incidents:
                    if 'fields' not in incident:
                        continue
                    for field in incident['fields']:
                        if 'display_name' not in field:
                            continue
                        if field['display_name'] in busObFields:
                            continue
                        v = self._clean_charset(field['display_name'])
                        busObFields.append(v)

            rows.append(busObFields)
            for incident in incidents:
                row = []
                if 'fields' not in incident:
                    continue
                incident_field_ref = {}
                incident_fields = incident['fields']
                for incident_field in incident_fields:
                    if 'value' not in incident_field:
                        continue
                    if incident_field['value'] == '':
                        continue
                    for k in ['display_name', 'name']:
                        if k not in incident_field:
                            continue
                        if incident_field[k] not in busObFields:
                            continue
                        incident_field_ref[incident_field[k]] = incident_field['value']
                for k in busObFields:
                    if k not in incident_field_ref:
                        row.append('---')
                        continue
                    v = self._clean_charset(incident_field_ref[k])
                    row.append(v)
                rows.append(row)
            return rows

        return incidents

    def add_journal_note(self, opts={}):
        return {'status': 'success'}

    @staticmethod
    def _clean_charset(s):
        s = str(s)
        arr = s.split('\n')
        if len(arr) == 1:
            return s.rstrip()
        for i, v in enumerate(arr):
            arr[i] = v.rstrip()
        return '\n'.join(arr)

    def _get_field_value(self, entry, pair):
        for f in entry:
            if pair[0] not in f or pair[1] not in f:
                continue
            if f[pair[0]] == pair[2]:
                return f[pair[1]]
        return ""

    def _get_csv_columns(self, header, entry):
        """Returns list of column headers.

        Args:
            header: List of business objects.
            entry: List of business objects.

        Returns:
            Returns a CSV row.

        """

        ref_entry = {}
        for f in entry:
            if 'field_id' not in f:
                continue
            ref_entry[f['field_id']] = f

        row = []
        for f in header:
            if 'field_id' not in f:
                continue
            if f['field_id'] not in ref_entry:
                row.append('')
                continue
            if 'value' not in ref_entry[f['field_id']]:
                row.append('')
                continue
            row.append(ref_entry[f['field_id']]['value'])
        return row


    def _get_csv_headers(self, entry, name):
        """Returns list of column headers.

        Args:
            entry: List of objects (dictionaries).
            name: The reference to the key containing column name.

        Returns:
            Returns list of strings.

        """

        headers = []
        for f in entry:
            if 'field_id' not in f:
                continue
            if 'name' not in f:
                headers.append(f['field_id'])
                continue
            headers.append(f[name])
        return headers


    def _serialize_kv(self, entry, pair, opts={}):
        """Converts a list of objects (dict) to list of two-element lists.

        Args:
            entry: List of objects (dictionaries).
            pair: The names of key and values.
            opts: Upstream parameters and options.

        Returns:
            returns a single dict containing the incident information.

        """
        width = None

        if 'terminal_columns' in opts and opts['terminal_columns'] > 0:
            if 'output_format' in opts and opts['output_format'] == 'text':
                width = {}
                width[0] = 30
                width[1] = opts['terminal_columns'] - width[0] - 10

        rows = []
        for f in entry:
            row = []
            for i in [0, 1]:
                if pair[i] in f:
                    v = str(f[pair[i]])
                    if width:
                        v = "\n".join(textwrap.wrap(v, width=width[i]))
                    row.append(v)
                    continue
                row.append('-')
            rows.append(row)
        return rows

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

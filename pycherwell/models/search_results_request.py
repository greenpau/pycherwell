# coding: utf-8

"""
    Cherwell REST API

    Unofficial Python Cherwell REST API library.  # noqa: E501

    The version of the OpenAPI document: 9.3.2
    Contact: See AUTHORS.
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pycherwell.configuration import Configuration


class SearchResultsRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'association': 'str',
        'bus_ob_id': 'str',
        'custom_grid_def_id': 'str',
        'date_time_formatting': 'str',
        'field_id': 'str',
        'fields': 'list[str]',
        'filters': 'list[FilterInfo]',
        'include_all_fields': 'bool',
        'include_schema': 'bool',
        'page_number': 'int',
        'page_size': 'int',
        'scope': 'str',
        'scope_owner': 'str',
        'search_id': 'str',
        'search_name': 'str',
        'search_text': 'str',
        'sorting': 'list[SortInfo]',
        'prompt_values': 'list[PromptValue]'
    }

    attribute_map = {
        'association': 'association',
        'bus_ob_id': 'busObId',
        'custom_grid_def_id': 'customGridDefId',
        'date_time_formatting': 'dateTimeFormatting',
        'field_id': 'fieldId',
        'fields': 'fields',
        'filters': 'filters',
        'include_all_fields': 'includeAllFields',
        'include_schema': 'includeSchema',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'scope': 'scope',
        'scope_owner': 'scopeOwner',
        'search_id': 'searchId',
        'search_name': 'searchName',
        'search_text': 'searchText',
        'sorting': 'sorting',
        'prompt_values': 'promptValues'
    }

    def __init__(self, association=None, bus_ob_id=None, custom_grid_def_id=None, date_time_formatting=None, field_id=None, fields=None, filters=None, include_all_fields=None, include_schema=None, page_number=None, page_size=None, scope=None, scope_owner=None, search_id=None, search_name=None, search_text=None, sorting=None, prompt_values=None, local_vars_configuration=None):  # noqa: E501
        """SearchResultsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association = None
        self._bus_ob_id = None
        self._custom_grid_def_id = None
        self._date_time_formatting = None
        self._field_id = None
        self._fields = None
        self._filters = None
        self._include_all_fields = None
        self._include_schema = None
        self._page_number = None
        self._page_size = None
        self._scope = None
        self._scope_owner = None
        self._search_id = None
        self._search_name = None
        self._search_text = None
        self._sorting = None
        self._prompt_values = None
        self.discriminator = None

        if association is not None:
            self.association = association
        if bus_ob_id is not None:
            self.bus_ob_id = bus_ob_id
        if custom_grid_def_id is not None:
            self.custom_grid_def_id = custom_grid_def_id
        if date_time_formatting is not None:
            self.date_time_formatting = date_time_formatting
        if field_id is not None:
            self.field_id = field_id
        if fields is not None:
            self.fields = fields
        if filters is not None:
            self.filters = filters
        if include_all_fields is not None:
            self.include_all_fields = include_all_fields
        if include_schema is not None:
            self.include_schema = include_schema
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if scope is not None:
            self.scope = scope
        if scope_owner is not None:
            self.scope_owner = scope_owner
        if search_id is not None:
            self.search_id = search_id
        if search_name is not None:
            self.search_name = search_name
        if search_text is not None:
            self.search_text = search_text
        if sorting is not None:
            self.sorting = sorting
        if prompt_values is not None:
            self.prompt_values = prompt_values

    @property
    def association(self):
        """Gets the association of this SearchResultsRequest.  # noqa: E501


        :return: The association of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this SearchResultsRequest.


        :param association: The association of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._association = association

    @property
    def bus_ob_id(self):
        """Gets the bus_ob_id of this SearchResultsRequest.  # noqa: E501


        :return: The bus_ob_id of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_id

    @bus_ob_id.setter
    def bus_ob_id(self, bus_ob_id):
        """Sets the bus_ob_id of this SearchResultsRequest.


        :param bus_ob_id: The bus_ob_id of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._bus_ob_id = bus_ob_id

    @property
    def custom_grid_def_id(self):
        """Gets the custom_grid_def_id of this SearchResultsRequest.  # noqa: E501


        :return: The custom_grid_def_id of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_grid_def_id

    @custom_grid_def_id.setter
    def custom_grid_def_id(self, custom_grid_def_id):
        """Sets the custom_grid_def_id of this SearchResultsRequest.


        :param custom_grid_def_id: The custom_grid_def_id of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._custom_grid_def_id = custom_grid_def_id

    @property
    def date_time_formatting(self):
        """Gets the date_time_formatting of this SearchResultsRequest.  # noqa: E501


        :return: The date_time_formatting of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_time_formatting

    @date_time_formatting.setter
    def date_time_formatting(self, date_time_formatting):
        """Sets the date_time_formatting of this SearchResultsRequest.


        :param date_time_formatting: The date_time_formatting of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._date_time_formatting = date_time_formatting

    @property
    def field_id(self):
        """Gets the field_id of this SearchResultsRequest.  # noqa: E501


        :return: The field_id of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this SearchResultsRequest.


        :param field_id: The field_id of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def fields(self):
        """Gets the fields of this SearchResultsRequest.  # noqa: E501


        :return: The fields of this SearchResultsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SearchResultsRequest.


        :param fields: The fields of this SearchResultsRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def filters(self):
        """Gets the filters of this SearchResultsRequest.  # noqa: E501


        :return: The filters of this SearchResultsRequest.  # noqa: E501
        :rtype: list[FilterInfo]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SearchResultsRequest.


        :param filters: The filters of this SearchResultsRequest.  # noqa: E501
        :type: list[FilterInfo]
        """

        self._filters = filters

    @property
    def include_all_fields(self):
        """Gets the include_all_fields of this SearchResultsRequest.  # noqa: E501


        :return: The include_all_fields of this SearchResultsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_all_fields

    @include_all_fields.setter
    def include_all_fields(self, include_all_fields):
        """Sets the include_all_fields of this SearchResultsRequest.


        :param include_all_fields: The include_all_fields of this SearchResultsRequest.  # noqa: E501
        :type: bool
        """

        self._include_all_fields = include_all_fields

    @property
    def include_schema(self):
        """Gets the include_schema of this SearchResultsRequest.  # noqa: E501


        :return: The include_schema of this SearchResultsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_schema

    @include_schema.setter
    def include_schema(self, include_schema):
        """Sets the include_schema of this SearchResultsRequest.


        :param include_schema: The include_schema of this SearchResultsRequest.  # noqa: E501
        :type: bool
        """

        self._include_schema = include_schema

    @property
    def page_number(self):
        """Gets the page_number of this SearchResultsRequest.  # noqa: E501


        :return: The page_number of this SearchResultsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this SearchResultsRequest.


        :param page_number: The page_number of this SearchResultsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this SearchResultsRequest.  # noqa: E501


        :return: The page_size of this SearchResultsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SearchResultsRequest.


        :param page_size: The page_size of this SearchResultsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def scope(self):
        """Gets the scope of this SearchResultsRequest.  # noqa: E501


        :return: The scope of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SearchResultsRequest.


        :param scope: The scope of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def scope_owner(self):
        """Gets the scope_owner of this SearchResultsRequest.  # noqa: E501


        :return: The scope_owner of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope_owner

    @scope_owner.setter
    def scope_owner(self, scope_owner):
        """Sets the scope_owner of this SearchResultsRequest.


        :param scope_owner: The scope_owner of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._scope_owner = scope_owner

    @property
    def search_id(self):
        """Gets the search_id of this SearchResultsRequest.  # noqa: E501


        :return: The search_id of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this SearchResultsRequest.


        :param search_id: The search_id of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def search_name(self):
        """Gets the search_name of this SearchResultsRequest.  # noqa: E501


        :return: The search_name of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        """Sets the search_name of this SearchResultsRequest.


        :param search_name: The search_name of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._search_name = search_name

    @property
    def search_text(self):
        """Gets the search_text of this SearchResultsRequest.  # noqa: E501


        :return: The search_text of this SearchResultsRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this SearchResultsRequest.


        :param search_text: The search_text of this SearchResultsRequest.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def sorting(self):
        """Gets the sorting of this SearchResultsRequest.  # noqa: E501


        :return: The sorting of this SearchResultsRequest.  # noqa: E501
        :rtype: list[SortInfo]
        """
        return self._sorting

    @sorting.setter
    def sorting(self, sorting):
        """Sets the sorting of this SearchResultsRequest.


        :param sorting: The sorting of this SearchResultsRequest.  # noqa: E501
        :type: list[SortInfo]
        """

        self._sorting = sorting

    @property
    def prompt_values(self):
        """Gets the prompt_values of this SearchResultsRequest.  # noqa: E501


        :return: The prompt_values of this SearchResultsRequest.  # noqa: E501
        :rtype: list[PromptValue]
        """
        return self._prompt_values

    @prompt_values.setter
    def prompt_values(self, prompt_values):
        """Sets the prompt_values of this SearchResultsRequest.


        :param prompt_values: The prompt_values of this SearchResultsRequest.  # noqa: E501
        :type: list[PromptValue]
        """

        self._prompt_values = prompt_values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchResultsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchResultsRequest):
            return True

        return self.to_dict() != other.to_dict()

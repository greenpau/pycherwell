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


class RelatedBusinessObjectRequest(object):
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
        'all_fields': 'bool',
        'custom_grid_id': 'str',
        'fields_list': 'list[str]',
        'filters': 'list[FilterInfo]',
        'page_number': 'int',
        'page_size': 'int',
        'parent_bus_ob_id': 'str',
        'parent_bus_ob_rec_id': 'str',
        'relationship_id': 'str',
        'sorting': 'list[SortInfo]',
        'use_default_grid': 'bool'
    }

    attribute_map = {
        'all_fields': 'allFields',
        'custom_grid_id': 'customGridId',
        'fields_list': 'fieldsList',
        'filters': 'filters',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'parent_bus_ob_id': 'parentBusObId',
        'parent_bus_ob_rec_id': 'parentBusObRecId',
        'relationship_id': 'relationshipId',
        'sorting': 'sorting',
        'use_default_grid': 'useDefaultGrid'
    }

    def __init__(self, all_fields=None, custom_grid_id=None, fields_list=None, filters=None, page_number=None, page_size=None, parent_bus_ob_id=None, parent_bus_ob_rec_id=None, relationship_id=None, sorting=None, use_default_grid=None, local_vars_configuration=None):  # noqa: E501
        """RelatedBusinessObjectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._all_fields = None
        self._custom_grid_id = None
        self._fields_list = None
        self._filters = None
        self._page_number = None
        self._page_size = None
        self._parent_bus_ob_id = None
        self._parent_bus_ob_rec_id = None
        self._relationship_id = None
        self._sorting = None
        self._use_default_grid = None
        self.discriminator = None

        if all_fields is not None:
            self.all_fields = all_fields
        if custom_grid_id is not None:
            self.custom_grid_id = custom_grid_id
        if fields_list is not None:
            self.fields_list = fields_list
        if filters is not None:
            self.filters = filters
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if parent_bus_ob_id is not None:
            self.parent_bus_ob_id = parent_bus_ob_id
        if parent_bus_ob_rec_id is not None:
            self.parent_bus_ob_rec_id = parent_bus_ob_rec_id
        if relationship_id is not None:
            self.relationship_id = relationship_id
        if sorting is not None:
            self.sorting = sorting
        if use_default_grid is not None:
            self.use_default_grid = use_default_grid

    @property
    def all_fields(self):
        """Gets the all_fields of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The all_fields of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._all_fields

    @all_fields.setter
    def all_fields(self, all_fields):
        """Sets the all_fields of this RelatedBusinessObjectRequest.


        :param all_fields: The all_fields of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: bool
        """

        self._all_fields = all_fields

    @property
    def custom_grid_id(self):
        """Gets the custom_grid_id of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The custom_grid_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_grid_id

    @custom_grid_id.setter
    def custom_grid_id(self, custom_grid_id):
        """Sets the custom_grid_id of this RelatedBusinessObjectRequest.


        :param custom_grid_id: The custom_grid_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: str
        """

        self._custom_grid_id = custom_grid_id

    @property
    def fields_list(self):
        """Gets the fields_list of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The fields_list of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields_list

    @fields_list.setter
    def fields_list(self, fields_list):
        """Sets the fields_list of this RelatedBusinessObjectRequest.


        :param fields_list: The fields_list of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields_list = fields_list

    @property
    def filters(self):
        """Gets the filters of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The filters of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: list[FilterInfo]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this RelatedBusinessObjectRequest.


        :param filters: The filters of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: list[FilterInfo]
        """

        self._filters = filters

    @property
    def page_number(self):
        """Gets the page_number of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The page_number of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this RelatedBusinessObjectRequest.


        :param page_number: The page_number of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The page_size of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this RelatedBusinessObjectRequest.


        :param page_size: The page_size of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def parent_bus_ob_id(self):
        """Gets the parent_bus_ob_id of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The parent_bus_ob_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_bus_ob_id

    @parent_bus_ob_id.setter
    def parent_bus_ob_id(self, parent_bus_ob_id):
        """Sets the parent_bus_ob_id of this RelatedBusinessObjectRequest.


        :param parent_bus_ob_id: The parent_bus_ob_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: str
        """

        self._parent_bus_ob_id = parent_bus_ob_id

    @property
    def parent_bus_ob_rec_id(self):
        """Gets the parent_bus_ob_rec_id of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The parent_bus_ob_rec_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_bus_ob_rec_id

    @parent_bus_ob_rec_id.setter
    def parent_bus_ob_rec_id(self, parent_bus_ob_rec_id):
        """Sets the parent_bus_ob_rec_id of this RelatedBusinessObjectRequest.


        :param parent_bus_ob_rec_id: The parent_bus_ob_rec_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: str
        """

        self._parent_bus_ob_rec_id = parent_bus_ob_rec_id

    @property
    def relationship_id(self):
        """Gets the relationship_id of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The relationship_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._relationship_id

    @relationship_id.setter
    def relationship_id(self, relationship_id):
        """Sets the relationship_id of this RelatedBusinessObjectRequest.


        :param relationship_id: The relationship_id of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: str
        """

        self._relationship_id = relationship_id

    @property
    def sorting(self):
        """Gets the sorting of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The sorting of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: list[SortInfo]
        """
        return self._sorting

    @sorting.setter
    def sorting(self, sorting):
        """Sets the sorting of this RelatedBusinessObjectRequest.


        :param sorting: The sorting of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: list[SortInfo]
        """

        self._sorting = sorting

    @property
    def use_default_grid(self):
        """Gets the use_default_grid of this RelatedBusinessObjectRequest.  # noqa: E501


        :return: The use_default_grid of this RelatedBusinessObjectRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_grid

    @use_default_grid.setter
    def use_default_grid(self, use_default_grid):
        """Sets the use_default_grid of this RelatedBusinessObjectRequest.


        :param use_default_grid: The use_default_grid of this RelatedBusinessObjectRequest.  # noqa: E501
        :type: bool
        """

        self._use_default_grid = use_default_grid

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
        if not isinstance(other, RelatedBusinessObjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedBusinessObjectRequest):
            return True

        return self.to_dict() != other.to_dict()

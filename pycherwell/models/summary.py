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


class Summary(object):
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
        'first_rec_id_field': 'str',
        'group_summaries': 'list[Summary]',
        'rec_id_fields': 'str',
        'state_field_id': 'str',
        'states': 'str',
        'bus_ob_id': 'str',
        'display_name': 'str',
        'group': 'bool',
        'lookup': 'bool',
        'major': 'bool',
        'name': 'str',
        'supporting': 'bool'
    }

    attribute_map = {
        'first_rec_id_field': 'firstRecIdField',
        'group_summaries': 'groupSummaries',
        'rec_id_fields': 'recIdFields',
        'state_field_id': 'stateFieldId',
        'states': 'states',
        'bus_ob_id': 'busObId',
        'display_name': 'displayName',
        'group': 'group',
        'lookup': 'lookup',
        'major': 'major',
        'name': 'name',
        'supporting': 'supporting'
    }

    def __init__(self, first_rec_id_field=None, group_summaries=None, rec_id_fields=None, state_field_id=None, states=None, bus_ob_id=None, display_name=None, group=None, lookup=None, major=None, name=None, supporting=None, local_vars_configuration=None):  # noqa: E501
        """Summary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first_rec_id_field = None
        self._group_summaries = None
        self._rec_id_fields = None
        self._state_field_id = None
        self._states = None
        self._bus_ob_id = None
        self._display_name = None
        self._group = None
        self._lookup = None
        self._major = None
        self._name = None
        self._supporting = None
        self.discriminator = None

        if first_rec_id_field is not None:
            self.first_rec_id_field = first_rec_id_field
        if group_summaries is not None:
            self.group_summaries = group_summaries
        if rec_id_fields is not None:
            self.rec_id_fields = rec_id_fields
        if state_field_id is not None:
            self.state_field_id = state_field_id
        if states is not None:
            self.states = states
        if bus_ob_id is not None:
            self.bus_ob_id = bus_ob_id
        if display_name is not None:
            self.display_name = display_name
        if group is not None:
            self.group = group
        if lookup is not None:
            self.lookup = lookup
        if major is not None:
            self.major = major
        if name is not None:
            self.name = name
        if supporting is not None:
            self.supporting = supporting

    @property
    def first_rec_id_field(self):
        """Gets the first_rec_id_field of this Summary.  # noqa: E501


        :return: The first_rec_id_field of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._first_rec_id_field

    @first_rec_id_field.setter
    def first_rec_id_field(self, first_rec_id_field):
        """Sets the first_rec_id_field of this Summary.


        :param first_rec_id_field: The first_rec_id_field of this Summary.  # noqa: E501
        :type: str
        """

        self._first_rec_id_field = first_rec_id_field

    @property
    def group_summaries(self):
        """Gets the group_summaries of this Summary.  # noqa: E501


        :return: The group_summaries of this Summary.  # noqa: E501
        :rtype: list[Summary]
        """
        return self._group_summaries

    @group_summaries.setter
    def group_summaries(self, group_summaries):
        """Sets the group_summaries of this Summary.


        :param group_summaries: The group_summaries of this Summary.  # noqa: E501
        :type: list[Summary]
        """

        self._group_summaries = group_summaries

    @property
    def rec_id_fields(self):
        """Gets the rec_id_fields of this Summary.  # noqa: E501


        :return: The rec_id_fields of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._rec_id_fields

    @rec_id_fields.setter
    def rec_id_fields(self, rec_id_fields):
        """Sets the rec_id_fields of this Summary.


        :param rec_id_fields: The rec_id_fields of this Summary.  # noqa: E501
        :type: str
        """

        self._rec_id_fields = rec_id_fields

    @property
    def state_field_id(self):
        """Gets the state_field_id of this Summary.  # noqa: E501


        :return: The state_field_id of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._state_field_id

    @state_field_id.setter
    def state_field_id(self, state_field_id):
        """Sets the state_field_id of this Summary.


        :param state_field_id: The state_field_id of this Summary.  # noqa: E501
        :type: str
        """

        self._state_field_id = state_field_id

    @property
    def states(self):
        """Gets the states of this Summary.  # noqa: E501


        :return: The states of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this Summary.


        :param states: The states of this Summary.  # noqa: E501
        :type: str
        """

        self._states = states

    @property
    def bus_ob_id(self):
        """Gets the bus_ob_id of this Summary.  # noqa: E501


        :return: The bus_ob_id of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_id

    @bus_ob_id.setter
    def bus_ob_id(self, bus_ob_id):
        """Sets the bus_ob_id of this Summary.


        :param bus_ob_id: The bus_ob_id of this Summary.  # noqa: E501
        :type: str
        """

        self._bus_ob_id = bus_ob_id

    @property
    def display_name(self):
        """Gets the display_name of this Summary.  # noqa: E501


        :return: The display_name of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Summary.


        :param display_name: The display_name of this Summary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def group(self):
        """Gets the group of this Summary.  # noqa: E501


        :return: The group of this Summary.  # noqa: E501
        :rtype: bool
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Summary.


        :param group: The group of this Summary.  # noqa: E501
        :type: bool
        """

        self._group = group

    @property
    def lookup(self):
        """Gets the lookup of this Summary.  # noqa: E501


        :return: The lookup of this Summary.  # noqa: E501
        :rtype: bool
        """
        return self._lookup

    @lookup.setter
    def lookup(self, lookup):
        """Sets the lookup of this Summary.


        :param lookup: The lookup of this Summary.  # noqa: E501
        :type: bool
        """

        self._lookup = lookup

    @property
    def major(self):
        """Gets the major of this Summary.  # noqa: E501


        :return: The major of this Summary.  # noqa: E501
        :rtype: bool
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this Summary.


        :param major: The major of this Summary.  # noqa: E501
        :type: bool
        """

        self._major = major

    @property
    def name(self):
        """Gets the name of this Summary.  # noqa: E501


        :return: The name of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Summary.


        :param name: The name of this Summary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def supporting(self):
        """Gets the supporting of this Summary.  # noqa: E501


        :return: The supporting of this Summary.  # noqa: E501
        :rtype: bool
        """
        return self._supporting

    @supporting.setter
    def supporting(self, supporting):
        """Sets the supporting of this Summary.


        :param supporting: The supporting of this Summary.  # noqa: E501
        :type: bool
        """

        self._supporting = supporting

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
        if not isinstance(other, Summary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Summary):
            return True

        return self.to_dict() != other.to_dict()

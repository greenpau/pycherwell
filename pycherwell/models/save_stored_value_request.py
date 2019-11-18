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


class SaveStoredValueRequest(object):
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
        'description': 'str',
        'folder': 'str',
        'name': 'str',
        'scope': 'str',
        'scope_owner': 'str',
        'stand_in_key': 'str',
        'stored_value_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'description': 'description',
        'folder': 'folder',
        'name': 'name',
        'scope': 'scope',
        'scope_owner': 'scopeOwner',
        'stand_in_key': 'standInKey',
        'stored_value_type': 'storedValueType',
        'value': 'value'
    }

    def __init__(self, description=None, folder=None, name=None, scope=None, scope_owner=None, stand_in_key=None, stored_value_type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """SaveStoredValueRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._folder = None
        self._name = None
        self._scope = None
        self._scope_owner = None
        self._stand_in_key = None
        self._stored_value_type = None
        self._value = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if folder is not None:
            self.folder = folder
        if name is not None:
            self.name = name
        if scope is not None:
            self.scope = scope
        if scope_owner is not None:
            self.scope_owner = scope_owner
        if stand_in_key is not None:
            self.stand_in_key = stand_in_key
        if stored_value_type is not None:
            self.stored_value_type = stored_value_type
        if value is not None:
            self.value = value

    @property
    def description(self):
        """Gets the description of this SaveStoredValueRequest.  # noqa: E501


        :return: The description of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SaveStoredValueRequest.


        :param description: The description of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def folder(self):
        """Gets the folder of this SaveStoredValueRequest.  # noqa: E501


        :return: The folder of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this SaveStoredValueRequest.


        :param folder: The folder of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def name(self):
        """Gets the name of this SaveStoredValueRequest.  # noqa: E501


        :return: The name of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaveStoredValueRequest.


        :param name: The name of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def scope(self):
        """Gets the scope of this SaveStoredValueRequest.  # noqa: E501


        :return: The scope of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SaveStoredValueRequest.


        :param scope: The scope of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def scope_owner(self):
        """Gets the scope_owner of this SaveStoredValueRequest.  # noqa: E501


        :return: The scope_owner of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope_owner

    @scope_owner.setter
    def scope_owner(self, scope_owner):
        """Sets the scope_owner of this SaveStoredValueRequest.


        :param scope_owner: The scope_owner of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._scope_owner = scope_owner

    @property
    def stand_in_key(self):
        """Gets the stand_in_key of this SaveStoredValueRequest.  # noqa: E501


        :return: The stand_in_key of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._stand_in_key

    @stand_in_key.setter
    def stand_in_key(self, stand_in_key):
        """Sets the stand_in_key of this SaveStoredValueRequest.


        :param stand_in_key: The stand_in_key of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._stand_in_key = stand_in_key

    @property
    def stored_value_type(self):
        """Gets the stored_value_type of this SaveStoredValueRequest.  # noqa: E501


        :return: The stored_value_type of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._stored_value_type

    @stored_value_type.setter
    def stored_value_type(self, stored_value_type):
        """Sets the stored_value_type of this SaveStoredValueRequest.


        :param stored_value_type: The stored_value_type of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Text", "Number", "DateTime", "Logical", "Color", "Json", "JsonArray", "Xml", "XmlCollection"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and stored_value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `stored_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(stored_value_type, allowed_values)
            )

        self._stored_value_type = stored_value_type

    @property
    def value(self):
        """Gets the value of this SaveStoredValueRequest.  # noqa: E501


        :return: The value of this SaveStoredValueRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SaveStoredValueRequest.


        :param value: The value of this SaveStoredValueRequest.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, SaveStoredValueRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaveStoredValueRequest):
            return True

        return self.to_dict() != other.to_dict()

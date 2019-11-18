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


class RoleReadResponse(object):
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
        'error': 'str',
        'error_code': 'str',
        'has_error': 'bool',
        'roles': 'list[Role]'
    }

    attribute_map = {
        'error': 'error',
        'error_code': 'errorCode',
        'has_error': 'hasError',
        'roles': 'roles'
    }

    def __init__(self, error=None, error_code=None, has_error=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """RoleReadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._error_code = None
        self._has_error = None
        self._roles = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        if has_error is not None:
            self.has_error = has_error
        if roles is not None:
            self.roles = roles

    @property
    def error(self):
        """Gets the error of this RoleReadResponse.  # noqa: E501


        :return: The error of this RoleReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RoleReadResponse.


        :param error: The error of this RoleReadResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this RoleReadResponse.  # noqa: E501


        :return: The error_code of this RoleReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RoleReadResponse.


        :param error_code: The error_code of this RoleReadResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def has_error(self):
        """Gets the has_error of this RoleReadResponse.  # noqa: E501


        :return: The has_error of this RoleReadResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this RoleReadResponse.


        :param has_error: The has_error of this RoleReadResponse.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    @property
    def roles(self):
        """Gets the roles of this RoleReadResponse.  # noqa: E501


        :return: The roles of this RoleReadResponse.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this RoleReadResponse.


        :param roles: The roles of this RoleReadResponse.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

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
        if not isinstance(other, RoleReadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleReadResponse):
            return True

        return self.to_dict() != other.to_dict()

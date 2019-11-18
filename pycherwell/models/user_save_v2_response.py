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


class UserSaveV2Response(object):
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
        'bus_ob_public_id': 'str',
        'bus_ob_rec_id': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'bus_ob_public_id': 'busObPublicId',
        'bus_ob_rec_id': 'busObRecId',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, bus_ob_public_id=None, bus_ob_rec_id=None, error_code=None, error_message=None, has_error=None, local_vars_configuration=None):  # noqa: E501
        """UserSaveV2Response - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bus_ob_public_id = None
        self._bus_ob_rec_id = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if bus_ob_public_id is not None:
            self.bus_ob_public_id = bus_ob_public_id
        if bus_ob_rec_id is not None:
            self.bus_ob_rec_id = bus_ob_rec_id
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def bus_ob_public_id(self):
        """Gets the bus_ob_public_id of this UserSaveV2Response.  # noqa: E501


        :return: The bus_ob_public_id of this UserSaveV2Response.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_public_id

    @bus_ob_public_id.setter
    def bus_ob_public_id(self, bus_ob_public_id):
        """Sets the bus_ob_public_id of this UserSaveV2Response.


        :param bus_ob_public_id: The bus_ob_public_id of this UserSaveV2Response.  # noqa: E501
        :type: str
        """

        self._bus_ob_public_id = bus_ob_public_id

    @property
    def bus_ob_rec_id(self):
        """Gets the bus_ob_rec_id of this UserSaveV2Response.  # noqa: E501


        :return: The bus_ob_rec_id of this UserSaveV2Response.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_rec_id

    @bus_ob_rec_id.setter
    def bus_ob_rec_id(self, bus_ob_rec_id):
        """Sets the bus_ob_rec_id of this UserSaveV2Response.


        :param bus_ob_rec_id: The bus_ob_rec_id of this UserSaveV2Response.  # noqa: E501
        :type: str
        """

        self._bus_ob_rec_id = bus_ob_rec_id

    @property
    def error_code(self):
        """Gets the error_code of this UserSaveV2Response.  # noqa: E501


        :return: The error_code of this UserSaveV2Response.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this UserSaveV2Response.


        :param error_code: The error_code of this UserSaveV2Response.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this UserSaveV2Response.  # noqa: E501


        :return: The error_message of this UserSaveV2Response.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this UserSaveV2Response.


        :param error_message: The error_message of this UserSaveV2Response.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this UserSaveV2Response.  # noqa: E501


        :return: The has_error of this UserSaveV2Response.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this UserSaveV2Response.


        :param has_error: The has_error of this UserSaveV2Response.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

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
        if not isinstance(other, UserSaveV2Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSaveV2Response):
            return True

        return self.to_dict() != other.to_dict()

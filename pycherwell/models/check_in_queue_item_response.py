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


class CheckInQueueItemResponse(object):
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
        'history_rec_id': 'str',
        'history_text': 'str',
        'history_type_id': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'history_rec_id': 'historyRecId',
        'history_text': 'historyText',
        'history_type_id': 'historyTypeId',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, history_rec_id=None, history_text=None, history_type_id=None, error_code=None, error_message=None, has_error=None, local_vars_configuration=None):  # noqa: E501
        """CheckInQueueItemResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._history_rec_id = None
        self._history_text = None
        self._history_type_id = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if history_rec_id is not None:
            self.history_rec_id = history_rec_id
        if history_text is not None:
            self.history_text = history_text
        if history_type_id is not None:
            self.history_type_id = history_type_id
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def history_rec_id(self):
        """Gets the history_rec_id of this CheckInQueueItemResponse.  # noqa: E501


        :return: The history_rec_id of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._history_rec_id

    @history_rec_id.setter
    def history_rec_id(self, history_rec_id):
        """Sets the history_rec_id of this CheckInQueueItemResponse.


        :param history_rec_id: The history_rec_id of this CheckInQueueItemResponse.  # noqa: E501
        :type: str
        """

        self._history_rec_id = history_rec_id

    @property
    def history_text(self):
        """Gets the history_text of this CheckInQueueItemResponse.  # noqa: E501


        :return: The history_text of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._history_text

    @history_text.setter
    def history_text(self, history_text):
        """Sets the history_text of this CheckInQueueItemResponse.


        :param history_text: The history_text of this CheckInQueueItemResponse.  # noqa: E501
        :type: str
        """

        self._history_text = history_text

    @property
    def history_type_id(self):
        """Gets the history_type_id of this CheckInQueueItemResponse.  # noqa: E501


        :return: The history_type_id of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._history_type_id

    @history_type_id.setter
    def history_type_id(self, history_type_id):
        """Sets the history_type_id of this CheckInQueueItemResponse.


        :param history_type_id: The history_type_id of this CheckInQueueItemResponse.  # noqa: E501
        :type: str
        """

        self._history_type_id = history_type_id

    @property
    def error_code(self):
        """Gets the error_code of this CheckInQueueItemResponse.  # noqa: E501


        :return: The error_code of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CheckInQueueItemResponse.


        :param error_code: The error_code of this CheckInQueueItemResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this CheckInQueueItemResponse.  # noqa: E501


        :return: The error_message of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CheckInQueueItemResponse.


        :param error_message: The error_message of this CheckInQueueItemResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this CheckInQueueItemResponse.  # noqa: E501


        :return: The has_error of this CheckInQueueItemResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this CheckInQueueItemResponse.


        :param has_error: The has_error of this CheckInQueueItemResponse.  # noqa: E501
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
        if not isinstance(other, CheckInQueueItemResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckInQueueItemResponse):
            return True

        return self.to_dict() != other.to_dict()

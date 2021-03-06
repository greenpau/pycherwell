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


class QuickSearchConfigurationRequest(object):
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
        'bus_ob_ids': 'list[str]'
    }

    attribute_map = {
        'bus_ob_ids': 'busObIds'
    }

    def __init__(self, bus_ob_ids=None, local_vars_configuration=None):  # noqa: E501
        """QuickSearchConfigurationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bus_ob_ids = None
        self.discriminator = None

        if bus_ob_ids is not None:
            self.bus_ob_ids = bus_ob_ids

    @property
    def bus_ob_ids(self):
        """Gets the bus_ob_ids of this QuickSearchConfigurationRequest.  # noqa: E501


        :return: The bus_ob_ids of this QuickSearchConfigurationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bus_ob_ids

    @bus_ob_ids.setter
    def bus_ob_ids(self, bus_ob_ids):
        """Sets the bus_ob_ids of this QuickSearchConfigurationRequest.


        :param bus_ob_ids: The bus_ob_ids of this QuickSearchConfigurationRequest.  # noqa: E501
        :type: list[str]
        """

        self._bus_ob_ids = bus_ob_ids

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
        if not isinstance(other, QuickSearchConfigurationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuickSearchConfigurationRequest):
            return True

        return self.to_dict() != other.to_dict()

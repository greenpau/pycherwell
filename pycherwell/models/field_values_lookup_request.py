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


class FieldValuesLookupRequest(object):
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
        'busb_public_id': 'str',
        'bus_ob_id': 'str',
        'bus_ob_rec_id': 'str',
        'field_id': 'str',
        'field_name': 'str',
        'fields': 'list[FieldTemplateItem]'
    }

    attribute_map = {
        'busb_public_id': 'busbPublicId',
        'bus_ob_id': 'busObId',
        'bus_ob_rec_id': 'busObRecId',
        'field_id': 'fieldId',
        'field_name': 'fieldName',
        'fields': 'fields'
    }

    def __init__(self, busb_public_id=None, bus_ob_id=None, bus_ob_rec_id=None, field_id=None, field_name=None, fields=None, local_vars_configuration=None):  # noqa: E501
        """FieldValuesLookupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._busb_public_id = None
        self._bus_ob_id = None
        self._bus_ob_rec_id = None
        self._field_id = None
        self._field_name = None
        self._fields = None
        self.discriminator = None

        if busb_public_id is not None:
            self.busb_public_id = busb_public_id
        if bus_ob_id is not None:
            self.bus_ob_id = bus_ob_id
        if bus_ob_rec_id is not None:
            self.bus_ob_rec_id = bus_ob_rec_id
        if field_id is not None:
            self.field_id = field_id
        if field_name is not None:
            self.field_name = field_name
        if fields is not None:
            self.fields = fields

    @property
    def busb_public_id(self):
        """Gets the busb_public_id of this FieldValuesLookupRequest.  # noqa: E501


        :return: The busb_public_id of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._busb_public_id

    @busb_public_id.setter
    def busb_public_id(self, busb_public_id):
        """Sets the busb_public_id of this FieldValuesLookupRequest.


        :param busb_public_id: The busb_public_id of this FieldValuesLookupRequest.  # noqa: E501
        :type: str
        """

        self._busb_public_id = busb_public_id

    @property
    def bus_ob_id(self):
        """Gets the bus_ob_id of this FieldValuesLookupRequest.  # noqa: E501


        :return: The bus_ob_id of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_id

    @bus_ob_id.setter
    def bus_ob_id(self, bus_ob_id):
        """Sets the bus_ob_id of this FieldValuesLookupRequest.


        :param bus_ob_id: The bus_ob_id of this FieldValuesLookupRequest.  # noqa: E501
        :type: str
        """

        self._bus_ob_id = bus_ob_id

    @property
    def bus_ob_rec_id(self):
        """Gets the bus_ob_rec_id of this FieldValuesLookupRequest.  # noqa: E501


        :return: The bus_ob_rec_id of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._bus_ob_rec_id

    @bus_ob_rec_id.setter
    def bus_ob_rec_id(self, bus_ob_rec_id):
        """Sets the bus_ob_rec_id of this FieldValuesLookupRequest.


        :param bus_ob_rec_id: The bus_ob_rec_id of this FieldValuesLookupRequest.  # noqa: E501
        :type: str
        """

        self._bus_ob_rec_id = bus_ob_rec_id

    @property
    def field_id(self):
        """Gets the field_id of this FieldValuesLookupRequest.  # noqa: E501


        :return: The field_id of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this FieldValuesLookupRequest.


        :param field_id: The field_id of this FieldValuesLookupRequest.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def field_name(self):
        """Gets the field_name of this FieldValuesLookupRequest.  # noqa: E501


        :return: The field_name of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this FieldValuesLookupRequest.


        :param field_name: The field_name of this FieldValuesLookupRequest.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def fields(self):
        """Gets the fields of this FieldValuesLookupRequest.  # noqa: E501


        :return: The fields of this FieldValuesLookupRequest.  # noqa: E501
        :rtype: list[FieldTemplateItem]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this FieldValuesLookupRequest.


        :param fields: The fields of this FieldValuesLookupRequest.  # noqa: E501
        :type: list[FieldTemplateItem]
        """

        self._fields = fields

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
        if not isinstance(other, FieldValuesLookupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldValuesLookupRequest):
            return True

        return self.to_dict() != other.to_dict()

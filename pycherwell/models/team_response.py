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


class TeamResponse(object):
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
        'email_alias': 'str',
        'fields': 'list[FieldTemplateItem]',
        'image': 'str',
        'name': 'str',
        'team_id': 'str',
        'team_type': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'has_error': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'email_alias': 'emailAlias',
        'fields': 'fields',
        'image': 'image',
        'name': 'name',
        'team_id': 'teamId',
        'team_type': 'teamType',
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'has_error': 'hasError'
    }

    def __init__(self, description=None, email_alias=None, fields=None, image=None, name=None, team_id=None, team_type=None, error_code=None, error_message=None, has_error=None, local_vars_configuration=None):  # noqa: E501
        """TeamResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._email_alias = None
        self._fields = None
        self._image = None
        self._name = None
        self._team_id = None
        self._team_type = None
        self._error_code = None
        self._error_message = None
        self._has_error = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if email_alias is not None:
            self.email_alias = email_alias
        if fields is not None:
            self.fields = fields
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if team_id is not None:
            self.team_id = team_id
        if team_type is not None:
            self.team_type = team_type
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if has_error is not None:
            self.has_error = has_error

    @property
    def description(self):
        """Gets the description of this TeamResponse.  # noqa: E501


        :return: The description of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TeamResponse.


        :param description: The description of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_alias(self):
        """Gets the email_alias of this TeamResponse.  # noqa: E501


        :return: The email_alias of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_alias

    @email_alias.setter
    def email_alias(self, email_alias):
        """Sets the email_alias of this TeamResponse.


        :param email_alias: The email_alias of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._email_alias = email_alias

    @property
    def fields(self):
        """Gets the fields of this TeamResponse.  # noqa: E501


        :return: The fields of this TeamResponse.  # noqa: E501
        :rtype: list[FieldTemplateItem]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this TeamResponse.


        :param fields: The fields of this TeamResponse.  # noqa: E501
        :type: list[FieldTemplateItem]
        """

        self._fields = fields

    @property
    def image(self):
        """Gets the image of this TeamResponse.  # noqa: E501


        :return: The image of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TeamResponse.


        :param image: The image of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this TeamResponse.  # noqa: E501


        :return: The name of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamResponse.


        :param name: The name of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team_id(self):
        """Gets the team_id of this TeamResponse.  # noqa: E501


        :return: The team_id of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamResponse.


        :param team_id: The team_id of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def team_type(self):
        """Gets the team_type of this TeamResponse.  # noqa: E501


        :return: The team_type of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._team_type

    @team_type.setter
    def team_type(self, team_type):
        """Sets the team_type of this TeamResponse.


        :param team_type: The team_type of this TeamResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "CustomerWorkgroup"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and team_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `team_type` ({0}), must be one of {1}"  # noqa: E501
                .format(team_type, allowed_values)
            )

        self._team_type = team_type

    @property
    def error_code(self):
        """Gets the error_code of this TeamResponse.  # noqa: E501


        :return: The error_code of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TeamResponse.


        :param error_code: The error_code of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this TeamResponse.  # noqa: E501


        :return: The error_message of this TeamResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this TeamResponse.


        :param error_message: The error_message of this TeamResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def has_error(self):
        """Gets the has_error of this TeamResponse.  # noqa: E501


        :return: The has_error of this TeamResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this TeamResponse.


        :param has_error: The has_error of this TeamResponse.  # noqa: E501
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
        if not isinstance(other, TeamResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamResponse):
            return True

        return self.to_dict() != other.to_dict()

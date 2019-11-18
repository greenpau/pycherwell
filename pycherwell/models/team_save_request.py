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


class TeamSaveRequest(object):
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
        'image': 'str',
        'team_id': 'str',
        'team_name': 'str',
        'team_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'email_alias': 'emailAlias',
        'image': 'image',
        'team_id': 'teamId',
        'team_name': 'teamName',
        'team_type': 'teamType'
    }

    def __init__(self, description=None, email_alias=None, image=None, team_id=None, team_name=None, team_type=None, local_vars_configuration=None):  # noqa: E501
        """TeamSaveRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._email_alias = None
        self._image = None
        self._team_id = None
        self._team_name = None
        self._team_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if email_alias is not None:
            self.email_alias = email_alias
        if image is not None:
            self.image = image
        if team_id is not None:
            self.team_id = team_id
        if team_name is not None:
            self.team_name = team_name
        if team_type is not None:
            self.team_type = team_type

    @property
    def description(self):
        """Gets the description of this TeamSaveRequest.  # noqa: E501


        :return: The description of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TeamSaveRequest.


        :param description: The description of this TeamSaveRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_alias(self):
        """Gets the email_alias of this TeamSaveRequest.  # noqa: E501


        :return: The email_alias of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_alias

    @email_alias.setter
    def email_alias(self, email_alias):
        """Sets the email_alias of this TeamSaveRequest.


        :param email_alias: The email_alias of this TeamSaveRequest.  # noqa: E501
        :type: str
        """

        self._email_alias = email_alias

    @property
    def image(self):
        """Gets the image of this TeamSaveRequest.  # noqa: E501


        :return: The image of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TeamSaveRequest.


        :param image: The image of this TeamSaveRequest.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def team_id(self):
        """Gets the team_id of this TeamSaveRequest.  # noqa: E501


        :return: The team_id of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamSaveRequest.


        :param team_id: The team_id of this TeamSaveRequest.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def team_name(self):
        """Gets the team_name of this TeamSaveRequest.  # noqa: E501


        :return: The team_name of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this TeamSaveRequest.


        :param team_name: The team_name of this TeamSaveRequest.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

    @property
    def team_type(self):
        """Gets the team_type of this TeamSaveRequest.  # noqa: E501


        :return: The team_type of this TeamSaveRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_type

    @team_type.setter
    def team_type(self, team_type):
        """Sets the team_type of this TeamSaveRequest.


        :param team_type: The team_type of this TeamSaveRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "CustomerWorkgroup"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and team_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `team_type` ({0}), must be one of {1}"  # noqa: E501
                .format(team_type, allowed_values)
            )

        self._team_type = team_type

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
        if not isinstance(other, TeamSaveRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamSaveRequest):
            return True

        return self.to_dict() != other.to_dict()

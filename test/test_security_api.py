# coding: utf-8

"""
    Cherwell REST API

    Unofficial Python Cherwell REST API library.  # noqa: E501

    The version of the OpenAPI document: 9.3.2
    Contact: See AUTHORS.
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pycherwell
from pycherwell.api.security_api import SecurityApi  # noqa: E501
from pycherwell.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = pycherwell.api.security_api.SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_security_get_client_security_settings_v1(self):
        """Test case for security_get_client_security_settings_v1

        Get client security settings  # noqa: E501
        """
        pass

    def test_security_get_roles_v1(self):
        """Test case for security_get_roles_v1

        Get all available Roles  # noqa: E501
        """
        pass

    def test_security_get_roles_v2(self):
        """Test case for security_get_roles_v2

        Get all available Roles  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_by_bus_ob_id_v1(self):
        """Test case for security_get_security_group_business_object_permissions_by_bus_ob_id_v1

        Get Business Object permissions by Security Group  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_by_bus_ob_id_v2(self):
        """Test case for security_get_security_group_business_object_permissions_by_bus_ob_id_v2

        Get Business Object permissions by Security Group  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_by_bus_ob_name_v1(self):
        """Test case for security_get_security_group_business_object_permissions_by_bus_ob_name_v1

        Get Business Object permissions by Security Group  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_by_bus_ob_name_v2(self):
        """Test case for security_get_security_group_business_object_permissions_by_bus_ob_name_v2

        Get Business Object permissions by Security Group  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_id_v1(self):
        """Test case for security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_id_v1

        Get Business Object permission for current user  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_id_v2(self):
        """Test case for security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_id_v2

        Get Business Object permission for current user  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_name_v1(self):
        """Test case for security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_name_v1

        Get Business Object permissions for current user  # noqa: E501
        """
        pass

    def test_security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_name_v2(self):
        """Test case for security_get_security_group_business_object_permissions_for_current_user_by_bus_ob_name_v2

        Get Business Object permissions for current user  # noqa: E501
        """
        pass

    def test_security_get_security_group_categories_v1(self):
        """Test case for security_get_security_group_categories_v1

        Get all Security Group categories  # noqa: E501
        """
        pass

    def test_security_get_security_group_categories_v2(self):
        """Test case for security_get_security_group_categories_v2

        Get all Security Group categories  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_by_group_id_and_category_id_v1(self):
        """Test case for security_get_security_group_rights_by_group_id_and_category_id_v1

        Get permissions for a Security Group by category  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_by_group_id_and_category_id_v2(self):
        """Test case for security_get_security_group_rights_by_group_id_and_category_id_v2

        Get permissions for a Security Group by category  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_by_group_name_and_category_name_v1(self):
        """Test case for security_get_security_group_rights_by_group_name_and_category_name_v1

        Get permissions for a Security Group by category  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_by_group_name_and_category_name_v2(self):
        """Test case for security_get_security_group_rights_by_group_name_and_category_name_v2

        Get permissions for a Security Group by category  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_for_current_user_by_category_id_v1(self):
        """Test case for security_get_security_group_rights_for_current_user_by_category_id_v1

        Get current user's permissions by Security Group category by ID  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_for_current_user_by_category_id_v2(self):
        """Test case for security_get_security_group_rights_for_current_user_by_category_id_v2

        Get current user's permissions by Security Group category by ID  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_for_current_user_by_category_name_v1(self):
        """Test case for security_get_security_group_rights_for_current_user_by_category_name_v1

        Get current user's permissions by Security Group category by name  # noqa: E501
        """
        pass

    def test_security_get_security_group_rights_for_current_user_by_category_name_v2(self):
        """Test case for security_get_security_group_rights_for_current_user_by_category_name_v2

        Get current user's permissions by Security Group category by name  # noqa: E501
        """
        pass

    def test_security_get_security_groups_v1(self):
        """Test case for security_get_security_groups_v1

        Get all available Security Groups  # noqa: E501
        """
        pass

    def test_security_get_security_groups_v2(self):
        """Test case for security_get_security_groups_v2

        Get all available Security Groups  # noqa: E501
        """
        pass

    def test_security_get_users_in_security_group_v1(self):
        """Test case for security_get_users_in_security_group_v1

        Get users in a Security Group  # noqa: E501
        """
        pass

    def test_security_get_users_in_security_group_v2(self):
        """Test case for security_get_users_in_security_group_v2

        Get users in a Security Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

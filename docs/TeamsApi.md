# pycherwell.TeamsApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_add_user_to_team_by_batch_v1**](TeamsApi.md#teams_add_user_to_team_by_batch_v1) | **POST** /api/V1/addusertoteambybatch | Add users to a team by batch
[**teams_add_user_to_team_v1**](TeamsApi.md#teams_add_user_to_team_v1) | **POST** /api/V1/addusertoteam | Add a user to a team
[**teams_add_user_to_team_v2**](TeamsApi.md#teams_add_user_to_team_v2) | **POST** /api/V2/addusertoteam | Add a user to a team
[**teams_delete_team_v1**](TeamsApi.md#teams_delete_team_v1) | **DELETE** /api/V1/deleteteam/{teamid} | Delete a Team
[**teams_get_team_v1**](TeamsApi.md#teams_get_team_v1) | **GET** /api/V1/getteam/{teamid} | Get a team by its TeamId
[**teams_get_teams_v1**](TeamsApi.md#teams_get_teams_v1) | **GET** /api/V1/getteams | Get all available Teams
[**teams_get_teams_v2**](TeamsApi.md#teams_get_teams_v2) | **GET** /api/V2/getteams | Get all available Teams
[**teams_get_users_teams_v1**](TeamsApi.md#teams_get_users_teams_v1) | **GET** /api/V1/getusersteams/userrecordid/{userRecordId} | Get Team assignments for a user
[**teams_get_users_teams_v2**](TeamsApi.md#teams_get_users_teams_v2) | **GET** /api/V2/getusersteams/userrecordid/{userRecordId} | Get Team assignments for a user
[**teams_get_workgroups_v1**](TeamsApi.md#teams_get_workgroups_v1) | **GET** /api/V1/getworkgroups | Get all available Workgroups
[**teams_get_workgroups_v2**](TeamsApi.md#teams_get_workgroups_v2) | **GET** /api/V2/getworkgroups | Get all available Workgroups
[**teams_remove_customer_from_workgroup_v1**](TeamsApi.md#teams_remove_customer_from_workgroup_v1) | **DELETE** /api/V1/removecustomerfromworkgroup/workgroupid/{workgroupid}/customerrecordid/{customerrecordid} | Remove a customer from a Workgroup
[**teams_remove_user_from_team_v1**](TeamsApi.md#teams_remove_user_from_team_v1) | **DELETE** /api/V1/removeuserfromteam/teamid/{teamId}/userrecordid/{userrecordid} | Operation to remove a User from a Team.
[**teams_remove_user_from_team_v2**](TeamsApi.md#teams_remove_user_from_team_v2) | **DELETE** /api/V2/removeuserfromteam/teamid/{teamId}/userrecordid/{userrecordid} | Operation to remove a User from a Team.
[**teams_save_team_member_v1**](TeamsApi.md#teams_save_team_member_v1) | **POST** /api/V1/saveteammember | Add or Update a team member
[**teams_save_team_v1**](TeamsApi.md#teams_save_team_v1) | **POST** /api/V1/saveteam | Create or update a team
[**teams_save_workgroup_member_v1**](TeamsApi.md#teams_save_workgroup_member_v1) | **POST** /api/V1/saveworkgroupmember | Save the membership status of a Workgroup member.


# **teams_add_user_to_team_by_batch_v1**
> AddUserToTeamByBatchResponse teams_add_user_to_team_by_batch_v1(add_user_to_team_by_batch_request)

Add users to a team by batch

Operation to add users to a Team by batch. To get internal IDs for users, use “Get User Information in a Batch.” To get a Team's internal ID, use \"Get all available Teams.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
add_user_to_team_by_batch_request = pycherwell.AddUserToTeamByBatchRequest() # AddUserToTeamByBatchRequest | Request object to specify a list of add user to team request objects.

try:
    # Add users to a team by batch
    api_response = api_instance.teams_add_user_to_team_by_batch_v1(add_user_to_team_by_batch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_add_user_to_team_by_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_team_by_batch_request** | [**AddUserToTeamByBatchRequest**](AddUserToTeamByBatchRequest.md)| Request object to specify a list of add user to team request objects. | 

### Return type

[**AddUserToTeamByBatchResponse**](AddUserToTeamByBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_user_to_team_v1**
> teams_add_user_to_team_v1(add_user_to_team_request)

Add a user to a team

Operation to add a user to a Team. To get the user's internal ID, use \"Get a user by login ID\" or \"Get a user by public ID.\" To get a Team's internal ID, use \"Get all available Teams.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
add_user_to_team_request = pycherwell.AddUserToTeamRequest() # AddUserToTeamRequest | Request object to specify user and team values.

try:
    # Add a user to a team
    api_instance.teams_add_user_to_team_v1(add_user_to_team_request)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_add_user_to_team_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_team_request** | [**AddUserToTeamRequest**](AddUserToTeamRequest.md)| Request object to specify user and team values. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_user_to_team_v2**
> AddUserToTeamResponse teams_add_user_to_team_v2(add_user_to_team_request)

Add a user to a team

Operation to add a user to a Team. To get the user's internal ID, use \"Get a user by login ID\" or \"Get a user by public ID.\" To get a Team's internal ID, use \"Get all available Teams.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
add_user_to_team_request = pycherwell.AddUserToTeamRequest() # AddUserToTeamRequest | Request object to specify user and team values.

try:
    # Add a user to a team
    api_response = api_instance.teams_add_user_to_team_v2(add_user_to_team_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_add_user_to_team_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_team_request** | [**AddUserToTeamRequest**](AddUserToTeamRequest.md)| Request object to specify user and team values. | 

### Return type

[**AddUserToTeamResponse**](AddUserToTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_delete_team_v1**
> teams_delete_team_v1(teamid)

Delete a Team

Operation to delete a Team by Team ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
teamid = 'teamid_example' # str | Specify the Team ID.

try:
    # Delete a Team
    api_instance.teams_delete_team_v1(teamid)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_delete_team_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamid** | **str**| Specify the Team ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_team_v1**
> TeamResponse teams_get_team_v1(teamid)

Get a team by its TeamId

Operation to get Team Info for a  single Team using its Team ID. To get a Team's internal ID, use \"Get all available Teams.\" Note that TeamType has two possible values, where TeamType = 0 for User (CSM Users), or TeamType = 1 for Workgroup (CSM Customers).

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
teamid = 'teamid_example' # str | The Team ID of the Team to get.

try:
    # Get a team by its TeamId
    api_response = api_instance.teams_get_team_v1(teamid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_team_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamid** | **str**| The Team ID of the Team to get. | 

### Return type

[**TeamResponse**](TeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_teams_v1**
> TeamsResponse teams_get_teams_v1()

Get all available Teams

Operation to get IDs and names for all available Teams.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()

try:
    # Get all available Teams
    api_response = api_instance.teams_get_teams_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_teams_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamsResponse**](TeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_teams_v2**
> TeamsV2Response teams_get_teams_v2()

Get all available Teams

Operation to get IDs and names for all available Teams.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()

try:
    # Get all available Teams
    api_response = api_instance.teams_get_teams_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_teams_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamsV2Response**](TeamsV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_users_teams_v1**
> TeamsResponse teams_get_users_teams_v1(user_record_id)

Get Team assignments for a user

Operation to get Team assignments for a user. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
user_record_id = 'user_record_id_example' # str | Specify the user record ID.

try:
    # Get Team assignments for a user
    api_response = api_instance.teams_get_users_teams_v1(user_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_users_teams_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_record_id** | **str**| Specify the user record ID. | 

### Return type

[**TeamsResponse**](TeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_users_teams_v2**
> TeamsV2Response teams_get_users_teams_v2(user_record_id)

Get Team assignments for a user

Operation to get Team assignments for a user. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
user_record_id = 'user_record_id_example' # str | Specify the user record ID.

try:
    # Get Team assignments for a user
    api_response = api_instance.teams_get_users_teams_v2(user_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_users_teams_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_record_id** | **str**| Specify the user record ID. | 

### Return type

[**TeamsV2Response**](TeamsV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_workgroups_v1**
> TeamsResponse teams_get_workgroups_v1()

Get all available Workgroups

Operation to get IDs and names for all available Workgroups.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()

try:
    # Get all available Workgroups
    api_response = api_instance.teams_get_workgroups_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_workgroups_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamsResponse**](TeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_workgroups_v2**
> TeamsV2Response teams_get_workgroups_v2()

Get all available Workgroups

Operation to get IDs and names for all available Workgroups.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()

try:
    # Get all available Workgroups
    api_response = api_instance.teams_get_workgroups_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_get_workgroups_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamsV2Response**](TeamsV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_customer_from_workgroup_v1**
> RemoveCustomerFromWorkgroupResponse teams_remove_customer_from_workgroup_v1(workgroupid, customerrecordid)

Remove a customer from a Workgroup

Operation to remove a Customer from a Workgroup.  To remove, specify the Workgroup ID and the Customer Record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
workgroupid = 'workgroupid_example' # str | Specify the Workgroup ID.
customerrecordid = 'customerrecordid_example' # str | Specify the Customer record ID.

try:
    # Remove a customer from a Workgroup
    api_response = api_instance.teams_remove_customer_from_workgroup_v1(workgroupid, customerrecordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_remove_customer_from_workgroup_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workgroupid** | **str**| Specify the Workgroup ID. | 
 **customerrecordid** | **str**| Specify the Customer record ID. | 

### Return type

[**RemoveCustomerFromWorkgroupResponse**](RemoveCustomerFromWorkgroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_user_from_team_v1**
> teams_remove_user_from_team_v1(team_id, userrecordid)

Operation to remove a User from a Team.

Operation to remove a User from a Team. To get the User's record ID, use \"Get a User by login ID\" or \"Get a User by public ID.\" To get a Team's internal ID, use \"Get all available Teams.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
team_id = 'team_id_example' # str | Specify the internal ID of the Team.
userrecordid = 'userrecordid_example' # str | Specify the record ID of the User to remove.

try:
    # Operation to remove a User from a Team.
    api_instance.teams_remove_user_from_team_v1(team_id, userrecordid)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_remove_user_from_team_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Specify the internal ID of the Team. | 
 **userrecordid** | **str**| Specify the record ID of the User to remove. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_user_from_team_v2**
> RemoveUserFromTeamResponse teams_remove_user_from_team_v2(team_id, userrecordid)

Operation to remove a User from a Team.

Operation to remove a User from a Team. To get the User's record ID, use \"Get a User by login ID\" or \"Get a User by public ID.\" To get a Team's internal ID, use \"Get all available Teams.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
team_id = 'team_id_example' # str | Specify the internal ID of the Team.
userrecordid = 'userrecordid_example' # str | Specify the record ID of the User to remove.

try:
    # Operation to remove a User from a Team.
    api_response = api_instance.teams_remove_user_from_team_v2(team_id, userrecordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_remove_user_from_team_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Specify the internal ID of the Team. | 
 **userrecordid** | **str**| Specify the record ID of the User to remove. | 

### Return type

[**RemoveUserFromTeamResponse**](RemoveUserFromTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_save_team_member_v1**
> SaveTeamMemberResponse teams_save_team_member_v1(save_team_member_request)

Add or Update a team member

Operation to add or update a Team Member. To add or update, specify User ID, Team ID, and if Team Manager.   Optionally, set the Team as the User's default Team.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
save_team_member_request = pycherwell.SaveTeamMemberRequest() # SaveTeamMemberRequest | The request object to add or update a Team Member. User recID specifies the User to add or update. TeamId specifies the Team to update. IsTeamManager specifies whether the User is a Team Manager, and SetAsDefaultTeam specifies whether to set this Team as the User's default team. UserRecId, TeamId, and IsTeamManager are required.

try:
    # Add or Update a team member
    api_response = api_instance.teams_save_team_member_v1(save_team_member_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_save_team_member_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_team_member_request** | [**SaveTeamMemberRequest**](SaveTeamMemberRequest.md)| The request object to add or update a Team Member. User recID specifies the User to add or update. TeamId specifies the Team to update. IsTeamManager specifies whether the User is a Team Manager, and SetAsDefaultTeam specifies whether to set this Team as the User&#39;s default team. UserRecId, TeamId, and IsTeamManager are required. | 

### Return type

[**SaveTeamMemberResponse**](SaveTeamMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_save_team_v1**
> TeamSaveResponse teams_save_team_v1(team_save_request)

Create or update a team

Operation to create or update a Team or Workgroup. 

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
team_save_request = pycherwell.TeamSaveRequest() # TeamSaveRequest | Request object to create Teams or Workgroups. To create a Team, use teamType and teamName. To update a team, use teamID. Team type values must be User or CustomerWorkgroup. The teamType cannot be changed for existing Teams or Workgroups.

try:
    # Create or update a team
    api_response = api_instance.teams_save_team_v1(team_save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_save_team_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_save_request** | [**TeamSaveRequest**](TeamSaveRequest.md)| Request object to create Teams or Workgroups. To create a Team, use teamType and teamName. To update a team, use teamID. Team type values must be User or CustomerWorkgroup. The teamType cannot be changed for existing Teams or Workgroups. | 

### Return type

[**TeamSaveResponse**](TeamSaveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_save_workgroup_member_v1**
> SaveWorkgroupMemberResponse teams_save_workgroup_member_v1(save_workgroup_member_request)

Save the membership status of a Workgroup member.

Operation to add or update a Workgroup Member.  To add or update, specify Customer Record ID, Workgroup ID, and if Workgroup Manager.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.TeamsApi()
save_workgroup_member_request = pycherwell.SaveWorkgroupMemberRequest() # SaveWorkgroupMemberRequest | The request object to add or update a Workgroup Member. CustomerRecordId specifies the Customer to add or update. WorkgroupId specifies the Workgroup to update. CustomerIsWorkgroupManager specifies whether the Customer is a Workgroup Manager.

try:
    # Save the membership status of a Workgroup member.
    api_response = api_instance.teams_save_workgroup_member_v1(save_workgroup_member_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_save_workgroup_member_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_workgroup_member_request** | [**SaveWorkgroupMemberRequest**](SaveWorkgroupMemberRequest.md)| The request object to add or update a Workgroup Member. CustomerRecordId specifies the Customer to add or update. WorkgroupId specifies the Workgroup to update. CustomerIsWorkgroupManager specifies whether the Customer is a Workgroup Manager. | 

### Return type

[**SaveWorkgroupMemberResponse**](SaveWorkgroupMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


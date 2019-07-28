# pycherwell.UsersApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_delete_user_batch_v1**](UsersApi.md#users_delete_user_batch_v1) | **POST** /api/V1/deleteuserbatch | Delete a batch of users
[**users_delete_user_batch_v2**](UsersApi.md#users_delete_user_batch_v2) | **POST** /api/V2/deleteuserbatch | Delete a batch of users
[**users_delete_user_v1**](UsersApi.md#users_delete_user_v1) | **DELETE** /api/V1/deleteuser/userrecordid/{userrecordid} | Delete a user by record ID
[**users_delete_user_v2**](UsersApi.md#users_delete_user_v2) | **DELETE** /api/V2/deleteuser/userrecordid/{userrecordid} | Delete a user by record ID
[**users_get_list_of_users**](UsersApi.md#users_get_list_of_users) | **GET** /api/V1/getlistofusers | Get a list of all system users.
[**users_get_user_batch_v1**](UsersApi.md#users_get_user_batch_v1) | **POST** /api/V1/getuserbatch | Get user information in a batch
[**users_get_user_by_login_id_v1**](UsersApi.md#users_get_user_by_login_id_v1) | **GET** /api/V1/getuserbyloginid/loginid/{loginid} | Get a user by login ID
[**users_get_user_by_login_id_v2**](UsersApi.md#users_get_user_by_login_id_v2) | **GET** /api/V2/getuserbyloginid | Get a user by login ID and login ID type
[**users_get_user_by_login_id_v3**](UsersApi.md#users_get_user_by_login_id_v3) | **GET** /api/V3/getuserbyloginid | Get a user by login ID and login ID type
[**users_get_user_by_public_id_v1**](UsersApi.md#users_get_user_by_public_id_v1) | **GET** /api/V1/getuserbypublicid/publicid/{publicid} | Get a user by public ID
[**users_get_user_by_public_id_v2**](UsersApi.md#users_get_user_by_public_id_v2) | **GET** /api/V2/getuserbypublicid/publicid/{publicid} | Get a user by public ID
[**users_get_user_by_rec_id**](UsersApi.md#users_get_user_by_rec_id) | **GET** /api/V1/getuserbyrecid/recid/{recid} | Get a user by record ID
[**users_save_user_batch_v1**](UsersApi.md#users_save_user_batch_v1) | **POST** /api/V1/saveuserbatch | Create or update users in a batch
[**users_save_user_batch_v2**](UsersApi.md#users_save_user_batch_v2) | **POST** /api/V2/saveuserbatch | Create or update users in a batch
[**users_save_user_v1**](UsersApi.md#users_save_user_v1) | **POST** /api/V1/saveuser | Create or update a user
[**users_save_user_v2**](UsersApi.md#users_save_user_v2) | **POST** /api/V2/saveuser | Create or update a user


# **users_delete_user_batch_v1**
> UserBatchDeleteResponse users_delete_user_batch_v1(user_batch_delete_request)

Delete a batch of users

Operation to delete a batch of users. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_batch_delete_request = pycherwell.UserBatchDeleteRequest() # UserBatchDeleteRequest | Request object listing record IDs for users to be deleted and an error flag.

try:
    # Delete a batch of users
    api_response = api_instance.users_delete_user_batch_v1(user_batch_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_user_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_delete_request** | [**UserBatchDeleteRequest**](UserBatchDeleteRequest.md)| Request object listing record IDs for users to be deleted and an error flag. | 

### Return type

[**UserBatchDeleteResponse**](UserBatchDeleteResponse.md)

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

# **users_delete_user_batch_v2**
> UserBatchDeleteV2Response users_delete_user_batch_v2(user_batch_delete_request)

Delete a batch of users

Operation to delete a batch of users. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_batch_delete_request = pycherwell.UserBatchDeleteRequest() # UserBatchDeleteRequest | Request object listing record IDs for users to be deleted and an error flag.

try:
    # Delete a batch of users
    api_response = api_instance.users_delete_user_batch_v2(user_batch_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_user_batch_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_delete_request** | [**UserBatchDeleteRequest**](UserBatchDeleteRequest.md)| Request object listing record IDs for users to be deleted and an error flag. | 

### Return type

[**UserBatchDeleteV2Response**](UserBatchDeleteV2Response.md)

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

# **users_delete_user_v1**
> UserDeleteResponse users_delete_user_v1(userrecordid)

Delete a user by record ID

Operation to delete a user by record ID. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
userrecordid = 'userrecordid_example' # str | Specify the record ID of the user you want to delete

try:
    # Delete a user by record ID
    api_response = api_instance.users_delete_user_v1(userrecordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_user_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userrecordid** | **str**| Specify the record ID of the user you want to delete | 

### Return type

[**UserDeleteResponse**](UserDeleteResponse.md)

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

# **users_delete_user_v2**
> UserDeleteV2Response users_delete_user_v2(userrecordid)

Delete a user by record ID

Operation to delete a user by record ID. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
userrecordid = 'userrecordid_example' # str | Specify the record ID of the user you want to delete

try:
    # Delete a user by record ID
    api_response = api_instance.users_delete_user_v2(userrecordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userrecordid** | **str**| Specify the record ID of the user you want to delete | 

### Return type

[**UserDeleteV2Response**](UserDeleteV2Response.md)

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

# **users_get_list_of_users**
> UserListResponse users_get_list_of_users(loginidfilter, stoponerror=stoponerror)

Get a list of all system users.

Operation to get a list of all system users.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
loginidfilter = 'loginidfilter_example' # str | Specify the login ID filter to apply to the users list.
stoponerror = True # bool | Specify whether the operation is interrupted if retrieving any user causes an error. (optional)

try:
    # Get a list of all system users.
    api_response = api_instance.users_get_list_of_users(loginidfilter, stoponerror=stoponerror)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_list_of_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginidfilter** | **str**| Specify the login ID filter to apply to the users list. | 
 **stoponerror** | **bool**| Specify whether the operation is interrupted if retrieving any user causes an error. | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **users_get_user_batch_v1**
> UserBatchReadResponse users_get_user_batch_v1(user_batch_read_request)

Get user information in a batch

Operation to get user information in a batch. To get record IDs, use \"Get a user by login ID\" or \"Get a user by public id.\"

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_batch_read_request = pycherwell.UserBatchReadRequest() # UserBatchReadRequest | Request object that lists user record IDs or public IDs of users and an error flag.

try:
    # Get user information in a batch
    api_response = api_instance.users_get_user_batch_v1(user_batch_read_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_read_request** | [**UserBatchReadRequest**](UserBatchReadRequest.md)| Request object that lists user record IDs or public IDs of users and an error flag. | 

### Return type

[**UserBatchReadResponse**](UserBatchReadResponse.md)

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

# **users_get_user_by_login_id_v1**
> User users_get_user_by_login_id_v1(loginid)

Get a user by login ID

Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example. This operation has been deprecated by a V2 operation of the same name, but with query string parameters.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
loginid = 'loginid_example' # str | Specify the user's login ID.

try:
    # Get a user by login ID
    api_response = api_instance.users_get_user_by_login_id_v1(loginid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_login_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginid** | **str**| Specify the user&#39;s login ID. | 

### Return type

[**User**](User.md)

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

# **users_get_user_by_login_id_v2**
> User users_get_user_by_login_id_v2(loginid, loginidtype)

Get a user by login ID and login ID type

Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
loginid = 'loginid_example' # str | Specify the user's login ID.
loginidtype = 'loginidtype_example' # str | Specify the login ID type.

try:
    # Get a user by login ID and login ID type
    api_response = api_instance.users_get_user_by_login_id_v2(loginid, loginidtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_login_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginid** | **str**| Specify the user&#39;s login ID. | 
 **loginidtype** | **str**| Specify the login ID type. | 

### Return type

[**User**](User.md)

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

# **users_get_user_by_login_id_v3**
> UserV2 users_get_user_by_login_id_v3(loginid, loginidtype)

Get a user by login ID and login ID type

Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
loginid = 'loginid_example' # str | Specify the user's login ID.
loginidtype = 'loginidtype_example' # str | Specify the login ID type.

try:
    # Get a user by login ID and login ID type
    api_response = api_instance.users_get_user_by_login_id_v3(loginid, loginidtype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_login_id_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loginid** | **str**| Specify the user&#39;s login ID. | 
 **loginidtype** | **str**| Specify the login ID type. | 

### Return type

[**UserV2**](UserV2.md)

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

# **users_get_user_by_public_id_v1**
> UserReadResponse users_get_user_by_public_id_v1(publicid)

Get a user by public ID

Operation to get detailed user information by public ID. Use to get user record IDs and account settings, for example.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
publicid = 'publicid_example' # str | Specify the user's public ID.

try:
    # Get a user by public ID
    api_response = api_instance.users_get_user_by_public_id_v1(publicid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicid** | **str**| Specify the user&#39;s public ID. | 

### Return type

[**UserReadResponse**](UserReadResponse.md)

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

# **users_get_user_by_public_id_v2**
> UserReadV2Response users_get_user_by_public_id_v2(publicid)

Get a user by public ID

Operation to get detailed user information by public ID. Use to get user record IDs and account settings, for example.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
publicid = 'publicid_example' # str | Specify the user's public ID.

try:
    # Get a user by public ID
    api_response = api_instance.users_get_user_by_public_id_v2(publicid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_public_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publicid** | **str**| Specify the user&#39;s public ID. | 

### Return type

[**UserReadV2Response**](UserReadV2Response.md)

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

# **users_get_user_by_rec_id**
> UserV2 users_get_user_by_rec_id(recid)

Get a user by record ID

Operation to get detailed user information by record ID.  Use to get user public IDs and account settings, for example.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
recid = 'recid_example' # str | Specify the user's record ID

try:
    # Get a user by record ID
    api_response = api_instance.users_get_user_by_rec_id(recid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_user_by_rec_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recid** | **str**| Specify the user&#39;s record ID | 

### Return type

[**UserV2**](UserV2.md)

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

# **users_save_user_batch_v1**
> UserBatchSaveResponse users_save_user_batch_v1(user_batch_save_request)

Create or update users in a batch

Operation to create or update users in a batch. To update, specify record ID. To create, leave record ID empty.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_batch_save_request = pycherwell.UserBatchSaveRequest() # UserBatchSaveRequest | Request object listing user record IDs and an error flag.

try:
    # Create or update users in a batch
    api_response = api_instance.users_save_user_batch_v1(user_batch_save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_save_user_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_save_request** | [**UserBatchSaveRequest**](UserBatchSaveRequest.md)| Request object listing user record IDs and an error flag. | 

### Return type

[**UserBatchSaveResponse**](UserBatchSaveResponse.md)

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

# **users_save_user_batch_v2**
> UserBatchSaveV2Response users_save_user_batch_v2(user_batch_save_v2_request)

Create or update users in a batch

Operation to create or update users in a batch. To update, specify record ID. To create, leave record ID empty.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_batch_save_v2_request = pycherwell.UserBatchSaveV2Request() # UserBatchSaveV2Request | Request object listing user record IDs and an error flag.

try:
    # Create or update users in a batch
    api_response = api_instance.users_save_user_batch_v2(user_batch_save_v2_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_save_user_batch_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_batch_save_v2_request** | [**UserBatchSaveV2Request**](UserBatchSaveV2Request.md)| Request object listing user record IDs and an error flag. | 

### Return type

[**UserBatchSaveV2Response**](UserBatchSaveV2Response.md)

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

# **users_save_user_v1**
> UserSaveResponse users_save_user_v1(user_save_request)

Create or update a user

Operation to create or update a user.  The response is a collection because if you use a public ID, more than one user could be updated since public IDs may not be unique. 

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_save_request = pycherwell.UserSaveRequest() # UserSaveRequest | Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required.

try:
    # Create or update a user
    api_response = api_instance.users_save_user_v1(user_save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_save_user_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_save_request** | [**UserSaveRequest**](UserSaveRequest.md)| Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required. | 

### Return type

[**UserSaveResponse**](UserSaveResponse.md)

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

# **users_save_user_v2**
> UserSaveV2Response users_save_user_v2(user_save_v2_request)

Create or update a user

Operation to create or update a user.  The response is a collection because if you use a public ID, more than one user could be updated since public IDs may not be unique. 

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.UsersApi()
user_save_v2_request = pycherwell.UserSaveV2Request() # UserSaveV2Request | Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required.

try:
    # Create or update a user
    api_response = api_instance.users_save_user_v2(user_save_v2_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_save_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_save_v2_request** | [**UserSaveV2Request**](UserSaveV2Request.md)| Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required. | 

### Return type

[**UserSaveV2Response**](UserSaveV2Response.md)

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


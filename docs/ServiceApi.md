# pycherwell.ServiceApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_get_service_info_v1**](ServiceApi.md#service_get_service_info_v1) | **GET** /api/V1/serviceinfo | Get information about the REST Api and CSM
[**service_logout_user_v1**](ServiceApi.md#service_logout_user_v1) | **DELETE** /api/V1/logout | Log out user by token


# **service_get_service_info_v1**
> ServiceInfoResponse service_get_service_info_v1()

Get information about the REST Api and CSM

Operation to get information about the REST API and CSM.  The response is latest REST API operation version, CSM version, and CSM system date and time.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.ServiceApi()

try:
    # Get information about the REST Api and CSM
    api_response = api_instance.service_get_service_info_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->service_get_service_info_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceInfoResponse**](ServiceInfoResponse.md)

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

# **service_logout_user_v1**
> service_logout_user_v1()

Log out user by token

Operation that logs out the user referenced in the authentication token.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.ServiceApi()

try:
    # Log out user by token
    api_instance.service_logout_user_v1()
except ApiException as e:
    print("Exception when calling ServiceApi->service_logout_user_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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


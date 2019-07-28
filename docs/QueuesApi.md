# pycherwell.QueuesApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queues_add_item_to_queue_v1**](QueuesApi.md#queues_add_item_to_queue_v1) | **POST** /api/V1/additemtoqueue | Add a Business Object to a queue
[**queues_check_in_queue_item_v1**](QueuesApi.md#queues_check_in_queue_item_v1) | **POST** /api/V1/checkinqueueitem | Check a Business Object in to a queue
[**queues_check_out_queue_item_v1**](QueuesApi.md#queues_check_out_queue_item_v1) | **POST** /api/V1/checkoutqueueitem | Check a Business Object out of a queue
[**queues_get_queues_folder_v1**](QueuesApi.md#queues_get_queues_folder_v1) | **GET** /api/V1/getqueues/scope/{scope}/scopeowner/{scopeowner}/folder/{folder} | Get available queues.
[**queues_get_queues_scope_owner_v1**](QueuesApi.md#queues_get_queues_scope_owner_v1) | **GET** /api/V1/getqueues/scope/{scope}/scopeowner/{scopeowner} | Get available queues.
[**queues_get_queues_scope_v1**](QueuesApi.md#queues_get_queues_scope_v1) | **GET** /api/V1/getqueues/scope/{scope} | Get available queues.
[**queues_get_queues_v1**](QueuesApi.md#queues_get_queues_v1) | **GET** /api/V1/getqueues | Get available queues.
[**queues_remove_item_from_queue_v1**](QueuesApi.md#queues_remove_item_from_queue_v1) | **POST** /api/V1/removeitemfromqueue | Remove an item from a queue


# **queues_add_item_to_queue_v1**
> AddItemToQueueResponse queues_add_item_to_queue_v1(add_item_to_queue_request)

Add a Business Object to a queue

Operation to add a Business Object to a queue

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
add_item_to_queue_request = pycherwell.AddItemToQueueRequest() # AddItemToQueueRequest | Request object containing all properties necessary to add an item to a queue. All properties are required. The standin key defines the queue to which we want to add the Business Object.

try:
    # Add a Business Object to a queue
    api_response = api_instance.queues_add_item_to_queue_v1(add_item_to_queue_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_add_item_to_queue_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_item_to_queue_request** | [**AddItemToQueueRequest**](AddItemToQueueRequest.md)| Request object containing all properties necessary to add an item to a queue. All properties are required. The standin key defines the queue to which we want to add the Business Object. | 

### Return type

[**AddItemToQueueResponse**](AddItemToQueueResponse.md)

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

# **queues_check_in_queue_item_v1**
> CheckInQueueItemResponse queues_check_in_queue_item_v1(check_in_queue_item_request)

Check a Business Object in to a queue

Operation to check in a queue item

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
check_in_queue_item_request = pycherwell.CheckInQueueItemRequest() # CheckInQueueItemRequest | The request object for checking in an item to a queue. All properties are required except for historyNotes

try:
    # Check a Business Object in to a queue
    api_response = api_instance.queues_check_in_queue_item_v1(check_in_queue_item_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_check_in_queue_item_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_in_queue_item_request** | [**CheckInQueueItemRequest**](CheckInQueueItemRequest.md)| The request object for checking in an item to a queue. All properties are required except for historyNotes | 

### Return type

[**CheckInQueueItemResponse**](CheckInQueueItemResponse.md)

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

# **queues_check_out_queue_item_v1**
> CheckOutQueueItemResponse queues_check_out_queue_item_v1(check_out_queue_item_request)

Check a Business Object out of a queue

Operation to check out a queue item

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
check_out_queue_item_request = pycherwell.CheckOutQueueItemRequest() # CheckOutQueueItemRequest | The request object for checking out an item from a queue. All properties are required except for historyNotes

try:
    # Check a Business Object out of a queue
    api_response = api_instance.queues_check_out_queue_item_v1(check_out_queue_item_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_check_out_queue_item_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_out_queue_item_request** | [**CheckOutQueueItemRequest**](CheckOutQueueItemRequest.md)| The request object for checking out an item from a queue. All properties are required except for historyNotes | 

### Return type

[**CheckOutQueueItemResponse**](CheckOutQueueItemResponse.md)

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

# **queues_get_queues_folder_v1**
> ManagerData queues_get_queues_folder_v1(scope, scopeowner, folder, links=links)

Get available queues.

Get available queues for a specific Business Object type based on scope, scope owner, and folder.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
scope = 'scope_example' # str | The scope to get available queues for.
scopeowner = 'scopeowner_example' # str | The scope owner to get available queues for.
folder = 'folder_example' # str | The folder to get available queues for.
links = True # bool | Whether or not to include links. (optional)

try:
    # Get available queues.
    api_response = api_instance.queues_get_queues_folder_v1(scope, scopeowner, folder, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_get_queues_folder_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get available queues for. | 
 **scopeowner** | **str**| The scope owner to get available queues for. | 
 **folder** | **str**| The folder to get available queues for. | 
 **links** | **bool**| Whether or not to include links. | [optional] 

### Return type

[**ManagerData**](ManagerData.md)

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

# **queues_get_queues_scope_owner_v1**
> ManagerData queues_get_queues_scope_owner_v1(scope, scopeowner, links=links)

Get available queues.

Get available queues for a specific Business Object type based on scope, and scope owner.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
scope = 'scope_example' # str | The scope to get available queues for.
scopeowner = 'scopeowner_example' # str | The scope owner to get available queues for.
links = True # bool | Whether or not to include links. (optional)

try:
    # Get available queues.
    api_response = api_instance.queues_get_queues_scope_owner_v1(scope, scopeowner, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_get_queues_scope_owner_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get available queues for. | 
 **scopeowner** | **str**| The scope owner to get available queues for. | 
 **links** | **bool**| Whether or not to include links. | [optional] 

### Return type

[**ManagerData**](ManagerData.md)

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

# **queues_get_queues_scope_v1**
> ManagerData queues_get_queues_scope_v1(scope, links=links)

Get available queues.

Get available queues for a specific Business Object type based on scope.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
scope = 'scope_example' # str | The scope to get available queues for.
links = True # bool | Whether or not to include links. (optional)

try:
    # Get available queues.
    api_response = api_instance.queues_get_queues_scope_v1(scope, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_get_queues_scope_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get available queues for. | 
 **links** | **bool**| Whether or not to include links. | [optional] 

### Return type

[**ManagerData**](ManagerData.md)

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

# **queues_get_queues_v1**
> ManagerData queues_get_queues_v1(links=links)

Get available queues.

Get available queues for a specific Business Object.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
links = True # bool | Whether or not to include links. (optional)

try:
    # Get available queues.
    api_response = api_instance.queues_get_queues_v1(links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_get_queues_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **links** | **bool**| Whether or not to include links. | [optional] 

### Return type

[**ManagerData**](ManagerData.md)

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

# **queues_remove_item_from_queue_v1**
> RemoveItemFromQueueResponse queues_remove_item_from_queue_v1(remove_item_from_queue_request)

Remove an item from a queue

Operation to remove an item from a queue

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.QueuesApi()
remove_item_from_queue_request = pycherwell.RemoveItemFromQueueRequest() # RemoveItemFromQueueRequest | The request object to remove an item from a queue. All properties are required except for historyNotes

try:
    # Remove an item from a queue
    api_response = api_instance.queues_remove_item_from_queue_v1(remove_item_from_queue_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueuesApi->queues_remove_item_from_queue_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_item_from_queue_request** | [**RemoveItemFromQueueRequest**](RemoveItemFromQueueRequest.md)| The request object to remove an item from a queue. All properties are required except for historyNotes | 

### Return type

[**RemoveItemFromQueueResponse**](RemoveItemFromQueueResponse.md)

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


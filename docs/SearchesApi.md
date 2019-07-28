# pycherwell.SearchesApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searches_get_quick_search_configuration_for_bus_obs_v1**](SearchesApi.md#searches_get_quick_search_configuration_for_bus_obs_v1) | **POST** /api/V1/getquicksearchconfigurationforbusobs | Get a Quick Search from a list of Business Object IDs
[**searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1**](SearchesApi.md#searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1) | **GET** /api/V1/getquicksearchconfigurationforbusobswithviewrights | Get a Quick Search by Business Objects with view rights
[**searches_get_quick_search_results_v1**](SearchesApi.md#searches_get_quick_search_results_v1) | **POST** /api/V1/getquicksearchresults | Execute a Quick Search from a list of Business Object IDs and search text
[**searches_get_quick_search_specific_results_v1**](SearchesApi.md#searches_get_quick_search_specific_results_v1) | **POST** /api/V1/getquicksearchspecificresults | Execute a Quick Search on a specific Business Object
[**searches_get_quick_search_specific_results_v2**](SearchesApi.md#searches_get_quick_search_specific_results_v2) | **POST** /api/V2/getquicksearchspecificresults | Execute a Quick Search on a specific Business Object
[**searches_get_search_items_by_association_scope_scope_owner_folder_v1**](SearchesApi.md#searches_get_search_items_by_association_scope_scope_owner_folder_v1) | **GET** /api/V1/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}/folder/{folder} | Get all saved searches by Folder ID
[**searches_get_search_items_by_association_scope_scope_owner_folder_v2**](SearchesApi.md#searches_get_search_items_by_association_scope_scope_owner_folder_v2) | **GET** /api/V2/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}/folder/{folder} | Get all saved searches by Folder ID
[**searches_get_search_items_by_association_scope_scope_owner_v1**](SearchesApi.md#searches_get_search_items_by_association_scope_scope_owner_v1) | **GET** /api/V1/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner} | Get all saved searches by scope owner (sub scope)
[**searches_get_search_items_by_association_scope_scope_owner_v2**](SearchesApi.md#searches_get_search_items_by_association_scope_scope_owner_v2) | **GET** /api/V2/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner} | Get all saved searches by scope owner (sub scope)
[**searches_get_search_items_by_association_scope_v1**](SearchesApi.md#searches_get_search_items_by_association_scope_v1) | **GET** /api/V1/getsearchitems/association/{association}/scope/{scope} | Get all saved searches by scope
[**searches_get_search_items_by_association_scope_v2**](SearchesApi.md#searches_get_search_items_by_association_scope_v2) | **GET** /api/V2/getsearchitems/association/{association}/scope/{scope} | Get all saved searches by scope
[**searches_get_search_items_by_association_v1**](SearchesApi.md#searches_get_search_items_by_association_v1) | **GET** /api/V1/getsearchitems/association/{association} | Get all saved searches by Business Object association
[**searches_get_search_items_by_association_v2**](SearchesApi.md#searches_get_search_items_by_association_v2) | **GET** /api/V2/getsearchitems/association/{association} | Get all saved searches by Business Object association
[**searches_get_search_items_v1**](SearchesApi.md#searches_get_search_items_v1) | **GET** /api/V1/getsearchitems | Get all saved searches by default Business Object association
[**searches_get_search_items_v2**](SearchesApi.md#searches_get_search_items_v2) | **GET** /api/V2/getsearchitems | Get all saved searches by default Business Object association
[**searches_get_search_results_ad_hoc_v1**](SearchesApi.md#searches_get_search_results_ad_hoc_v1) | **POST** /api/V1/getsearchresults | Run an ad-hoc search
[**searches_get_search_results_by_id_v1**](SearchesApi.md#searches_get_search_results_by_id_v1) | **GET** /api/V1/getsearchresults/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchid/{searchid} | Run a saved search by internal ID
[**searches_get_search_results_by_name_v1**](SearchesApi.md#searches_get_search_results_by_name_v1) | **GET** /api/V1/getsearchresults/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchname/{searchname} | Run a saved search by name
[**searches_get_search_results_export_ad_hoc_v1**](SearchesApi.md#searches_get_search_results_export_ad_hoc_v1) | **POST** /api/V1/getsearchresultsexport | Export an ad-hoc search
[**searches_get_search_results_export_by_id_v1**](SearchesApi.md#searches_get_search_results_export_by_id_v1) | **GET** /api/V1/getsearchresultsexport/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchid/{searchid}/exportformat/{exportformat} | Export a saved search by ID
[**searches_get_search_results_export_by_name_v1**](SearchesApi.md#searches_get_search_results_export_by_name_v1) | **GET** /api/V1/getsearchresultsexport/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchname/{searchname}/exportformat/{exportformat} | Export a saved search by name


# **searches_get_quick_search_configuration_for_bus_obs_v1**
> QuickSearchConfigurationResponse searches_get_quick_search_configuration_for_bus_obs_v1(quick_search_configuration_request)

Get a Quick Search from a list of Business Object IDs

Operation to build a Quick Search configuration that you can use to execute a Quick Search for multiple Business Objects. The configuration  includes supplied Business Object IDs and specific search items with the following options. Use the Option Key to determine if you can change the options. </br></br></br>ChangedOption</br></br>NonFinalStateOption</br></br>SearchAnyWordsOption</br></br>SearchAttachmentsOption</br></br>SearchRelatedOption</br></br>SortByOption</br></br></br>Option Key:</br></br>0 = None (Not selected and cannot select.)</br></br>1 = Use (Selected and cannot clear.)</br></br>2 = Display (Not selected and can select.)</br></br>3 = UseAndDisplay (Selected and can clear.)</br></br></br>SearchTargetType:</br></br>0 = BusOb (Business Object)</br></br>1 = DocRepository (Document Repository)

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
quick_search_configuration_request = pycherwell.QuickSearchConfigurationRequest() # QuickSearchConfigurationRequest | Request containing the Business Object IDs list.

try:
    # Get a Quick Search from a list of Business Object IDs
    api_response = api_instance.searches_get_quick_search_configuration_for_bus_obs_v1(quick_search_configuration_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_quick_search_configuration_for_bus_obs_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_search_configuration_request** | [**QuickSearchConfigurationRequest**](QuickSearchConfigurationRequest.md)| Request containing the Business Object IDs list. | 

### Return type

[**QuickSearchConfigurationResponse**](QuickSearchConfigurationResponse.md)

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

# **searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1**
> QuickSearchConfigurationResponse searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1()

Get a Quick Search by Business Objects with view rights

Operation to get a Quick Search configuration that you can use to execute a Quick Search based the current user's Business Object view rights. The configuration  includes supplied Business Object IDs and specific search items with the following options. Use the Option Key to determine if you can change the options.</br></br>ChangedOption</br></br>NonFinalStateOption</br></br>SearchAnyWordsOption</br></br>SearchAttachmentsOption</br></br>SearchRelatedOption</br></br>SortByOption</br></br></br>Option Key:</br></br>0 = None (Not selected and cannot select.)</br></br>1 = Use (Selected and cannot clear.)</br></br>2 = Display (Not selected and can select.)</br></br>3 = UseAndDisplay (Selected and can clear.)</br></br></br>SearchTargetType:</br></br>0 = BusOb (Business Object)</br></br>1 = DocRepository (Document Repository)

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()

try:
    # Get a Quick Search by Business Objects with view rights
    api_response = api_instance.searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_quick_search_configuration_for_bus_obs_with_view_rights_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuickSearchConfigurationResponse**](QuickSearchConfigurationResponse.md)

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

# **searches_get_quick_search_results_v1**
> SimpleResultsList searches_get_quick_search_results_v1(quick_search_request, include_links=include_links)

Execute a Quick Search from a list of Business Object IDs and search text

Operation to execute a Quick Search using a list of Business Object IDs and search text.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
quick_search_request = pycherwell.QuickSearchRequest() # QuickSearchRequest | Request object listing Business Object IDs and search text. Leave out the entire Business Object IDs parameter and all configured quick search Business Objects will be searched.
include_links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Execute a Quick Search from a list of Business Object IDs and search text
    api_response = api_instance.searches_get_quick_search_results_v1(quick_search_request, include_links=include_links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_quick_search_results_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_search_request** | [**QuickSearchRequest**](QuickSearchRequest.md)| Request object listing Business Object IDs and search text. Leave out the entire Business Object IDs parameter and all configured quick search Business Objects will be searched. | 
 **include_links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SimpleResultsList**](SimpleResultsList.md)

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

# **searches_get_quick_search_specific_results_v1**
> SearchResultsTableResponse searches_get_quick_search_specific_results_v1(quick_search_specific_request, include_schema=include_schema, include_location_fields=include_location_fields, include_links=include_links)

Execute a Quick Search on a specific Business Object

Operation to execute a Quick Search for a specific Business Object ID. Use \"Get a Quick Search from a list of Business Object IDs\" to find values for specific search item options, such as NonFinalStateOption.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
quick_search_specific_request = pycherwell.QuickSearchSpecificRequest() # QuickSearchSpecificRequest | Request object containing the parameters for specific Business Object Quick Search execution.
include_schema = True # bool | Flag to include the schema for the results. (optional)
include_location_fields = True # bool | Flag to include location fields in the results. (optional)
include_links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Execute a Quick Search on a specific Business Object
    api_response = api_instance.searches_get_quick_search_specific_results_v1(quick_search_specific_request, include_schema=include_schema, include_location_fields=include_location_fields, include_links=include_links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_quick_search_specific_results_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_search_specific_request** | [**QuickSearchSpecificRequest**](QuickSearchSpecificRequest.md)| Request object containing the parameters for specific Business Object Quick Search execution. | 
 **include_schema** | **bool**| Flag to include the schema for the results. | [optional] 
 **include_location_fields** | **bool**| Flag to include location fields in the results. | [optional] 
 **include_links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchResultsTableResponse**](SearchResultsTableResponse.md)

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

# **searches_get_quick_search_specific_results_v2**
> QuickSearchResponse searches_get_quick_search_specific_results_v2(quick_search_specific_request, include_schema=include_schema, include_location_fields=include_location_fields, include_links=include_links)

Execute a Quick Search on a specific Business Object

Operation to execute a Quick Search for a specific Business Object ID. Use \"Get a Quick Search from a list of Business Object IDs\" to find values for specific search item options, such as NonFinalStateOption.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
quick_search_specific_request = pycherwell.QuickSearchSpecificRequest() # QuickSearchSpecificRequest | Request object containing the parameters for specific Business Object Quick Search execution.
include_schema = True # bool | Flag to include the schema for the results. (optional)
include_location_fields = True # bool | Flag to include location fields in the results. (optional)
include_links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Execute a Quick Search on a specific Business Object
    api_response = api_instance.searches_get_quick_search_specific_results_v2(quick_search_specific_request, include_schema=include_schema, include_location_fields=include_location_fields, include_links=include_links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_quick_search_specific_results_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_search_specific_request** | [**QuickSearchSpecificRequest**](QuickSearchSpecificRequest.md)| Request object containing the parameters for specific Business Object Quick Search execution. | 
 **include_schema** | **bool**| Flag to include the schema for the results. | [optional] 
 **include_location_fields** | **bool**| Flag to include location fields in the results. | [optional] 
 **include_links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**QuickSearchResponse**](QuickSearchResponse.md)

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

# **searches_get_search_items_by_association_scope_scope_owner_folder_v1**
> SearchItemResponse searches_get_search_items_by_association_scope_scope_owner_folder_v1(association, scope, scopeowner, folder, links=links)

Get all saved searches by Folder ID

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
scopeowner = 'scopeowner_example' # str | Use to filter results by scope owner ID.
folder = 'folder_example' # str | Use to filter results by Search Group folder ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by Folder ID
    api_response = api_instance.searches_get_search_items_by_association_scope_scope_owner_folder_v1(association, scope, scopeowner, folder, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_scope_owner_folder_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **scopeowner** | **str**| Use to filter results by scope owner ID. | 
 **folder** | **str**| Use to filter results by Search Group folder ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchItemResponse**](SearchItemResponse.md)

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

# **searches_get_search_items_by_association_scope_scope_owner_folder_v2**
> ManagerData searches_get_search_items_by_association_scope_scope_owner_folder_v2(association, scope, scopeowner, folder, links=links)

Get all saved searches by Folder ID

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
scopeowner = 'scopeowner_example' # str | Use to filter results by scope owner ID.
folder = 'folder_example' # str | Use to filter results by Search Group folder ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by Folder ID
    api_response = api_instance.searches_get_search_items_by_association_scope_scope_owner_folder_v2(association, scope, scopeowner, folder, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_scope_owner_folder_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **scopeowner** | **str**| Use to filter results by scope owner ID. | 
 **folder** | **str**| Use to filter results by Search Group folder ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

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

# **searches_get_search_items_by_association_scope_scope_owner_v1**
> SearchItemResponse searches_get_search_items_by_association_scope_scope_owner_v1(association, scope, scopeowner, links=links)

Get all saved searches by scope owner (sub scope)

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
scopeowner = 'scopeowner_example' # str | Use to filter results by scope owner ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by scope owner (sub scope)
    api_response = api_instance.searches_get_search_items_by_association_scope_scope_owner_v1(association, scope, scopeowner, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_scope_owner_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **scopeowner** | **str**| Use to filter results by scope owner ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchItemResponse**](SearchItemResponse.md)

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

# **searches_get_search_items_by_association_scope_scope_owner_v2**
> ManagerData searches_get_search_items_by_association_scope_scope_owner_v2(association, scope, scopeowner, links=links)

Get all saved searches by scope owner (sub scope)

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
scopeowner = 'scopeowner_example' # str | Use to filter results by scope owner ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by scope owner (sub scope)
    api_response = api_instance.searches_get_search_items_by_association_scope_scope_owner_v2(association, scope, scopeowner, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_scope_owner_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **scopeowner** | **str**| Use to filter results by scope owner ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

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

# **searches_get_search_items_by_association_scope_v1**
> SearchItemResponse searches_get_search_items_by_association_scope_v1(association, scope, links=links)

Get all saved searches by scope

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by scope
    api_response = api_instance.searches_get_search_items_by_association_scope_v1(association, scope, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchItemResponse**](SearchItemResponse.md)

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

# **searches_get_search_items_by_association_scope_v2**
> ManagerData searches_get_search_items_by_association_scope_v2(association, scope, links=links)

Get all saved searches by scope

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
scope = 'scope_example' # str | Use to filter results by scope name or ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by scope
    api_response = api_instance.searches_get_search_items_by_association_scope_v2(association, scope, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_scope_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **scope** | **str**| Use to filter results by scope name or ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

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

# **searches_get_search_items_by_association_v1**
> SearchItemResponse searches_get_search_items_by_association_v1(association, links=links)

Get all saved searches by Business Object association

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by Business Object association
    api_response = api_instance.searches_get_search_items_by_association_v1(association, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchItemResponse**](SearchItemResponse.md)

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

# **searches_get_search_items_by_association_v2**
> ManagerData searches_get_search_items_by_association_v2(association, links=links)

Get all saved searches by Business Object association

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Use to filter results by Business Object association ID.
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by Business Object association
    api_response = api_instance.searches_get_search_items_by_association_v2(association, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_by_association_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Use to filter results by Business Object association ID. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

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

# **searches_get_search_items_v1**
> SearchItemResponse searches_get_search_items_v1(links=links)

Get all saved searches by default Business Object association

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by default Business Object association
    api_response = api_instance.searches_get_search_items_v1(links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**SearchItemResponse**](SearchItemResponse.md)

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

# **searches_get_search_items_v2**
> ManagerData searches_get_search_items_v2(links=links)

Get all saved searches by default Business Object association

Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
links = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get all saved searches by default Business Object association
    api_response = api_instance.searches_get_search_items_v2(links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_items_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **links** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

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

# **searches_get_search_results_ad_hoc_v1**
> SearchResultsResponse searches_get_search_results_ad_hoc_v1(search_results_request)

Run an ad-hoc search

Operation that runs an ad-hoc Business Object search. To execute a search with Prompts, the PromptId and Value are required in the Prompt request object.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
search_results_request = pycherwell.SearchResultsRequest() # SearchResultsRequest | Request object to specify search parameters.

try:
    # Run an ad-hoc search
    api_response = api_instance.searches_get_search_results_ad_hoc_v1(search_results_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_ad_hoc_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_results_request** | [**SearchResultsRequest**](SearchResultsRequest.md)| Request object to specify search parameters. | 

### Return type

[**SearchResultsResponse**](SearchResultsResponse.md)

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

# **searches_get_search_results_by_id_v1**
> SearchResultsResponse searches_get_search_results_by_id_v1(association, scope, scopeowner, searchid, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize, includeschema=includeschema, results_as_simple_results_list=results_as_simple_results_list)

Run a saved search by internal ID

Operation that returns the paged results of a saved search. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresults ad-hoc http post operation.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Specify the Business Object association ID for the saved search.
scope = 'scope_example' # str | Specify the scope name or ID for the saved search.
scopeowner = 'scopeowner_example' # str | Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
searchid = 'searchid_example' # str | Specify the internal ID for the saved search. Use \"Run a saved search by name\" if you do not have the internal ID.
search_term = 'search_term_example' # str | Specify search text filter the results. Example: Use \"Service Request\" to filter Incident results to include only service requests. (optional)
pagenumber = 56 # int | Specify the page number of the result set to return. (optional)
pagesize = 56 # int | Specify the number of rows to return per page. (optional)
includeschema = True # bool | Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false. (optional)
results_as_simple_results_list = True # bool | Indicates if the results should be returned in a simple results list format or a table format. Default is a table format. (optional)

try:
    # Run a saved search by internal ID
    api_response = api_instance.searches_get_search_results_by_id_v1(association, scope, scopeowner, searchid, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize, includeschema=includeschema, results_as_simple_results_list=results_as_simple_results_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Specify the Business Object association ID for the saved search. | 
 **scope** | **str**| Specify the scope name or ID for the saved search. | 
 **scopeowner** | **str**| Specify the scope owner ID for the saved search. Use (None) when no scope owner exists. | 
 **searchid** | **str**| Specify the internal ID for the saved search. Use \&quot;Run a saved search by name\&quot; if you do not have the internal ID. | 
 **search_term** | **str**| Specify search text filter the results. Example: Use \&quot;Service Request\&quot; to filter Incident results to include only service requests. | [optional] 
 **pagenumber** | **int**| Specify the page number of the result set to return. | [optional] 
 **pagesize** | **int**| Specify the number of rows to return per page. | [optional] 
 **includeschema** | **bool**| Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false. | [optional] 
 **results_as_simple_results_list** | **bool**| Indicates if the results should be returned in a simple results list format or a table format. Default is a table format. | [optional] 

### Return type

[**SearchResultsResponse**](SearchResultsResponse.md)

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

# **searches_get_search_results_by_name_v1**
> SearchResultsResponse searches_get_search_results_by_name_v1(association, scope, scopeowner, searchname, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize, includeschema=includeschema, results_as_simple_results_list=results_as_simple_results_list)

Run a saved search by name

Operation that returns the paged results of a saved search. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresults ad-hoc http post operation.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Specify the Business Object association ID for the saved search.
scope = 'scope_example' # str | Specify the scope name or ID for the saved search.
scopeowner = 'scopeowner_example' # str | Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
searchname = 'searchname_example' # str | Specify the name of the saved search.
search_term = 'search_term_example' # str | Specify search text filter the results. Example: Use \"Service Request\" to filter Incident results to include only service requests. (optional)
pagenumber = 56 # int | Specify the page number of the result set to return. (optional)
pagesize = 56 # int | Specify the number of rows to return per page. (optional)
includeschema = True # bool | Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false. (optional)
results_as_simple_results_list = True # bool | Indicates if the results should be returned in a simple results list format or a table format. Default is a table format. (optional)

try:
    # Run a saved search by name
    api_response = api_instance.searches_get_search_results_by_name_v1(association, scope, scopeowner, searchname, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize, includeschema=includeschema, results_as_simple_results_list=results_as_simple_results_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_by_name_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Specify the Business Object association ID for the saved search. | 
 **scope** | **str**| Specify the scope name or ID for the saved search. | 
 **scopeowner** | **str**| Specify the scope owner ID for the saved search. Use (None) when no scope owner exists. | 
 **searchname** | **str**| Specify the name of the saved search. | 
 **search_term** | **str**| Specify search text filter the results. Example: Use \&quot;Service Request\&quot; to filter Incident results to include only service requests. | [optional] 
 **pagenumber** | **int**| Specify the page number of the result set to return. | [optional] 
 **pagesize** | **int**| Specify the number of rows to return per page. | [optional] 
 **includeschema** | **bool**| Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false. | [optional] 
 **results_as_simple_results_list** | **bool**| Indicates if the results should be returned in a simple results list format or a table format. Default is a table format. | [optional] 

### Return type

[**SearchResultsResponse**](SearchResultsResponse.md)

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

# **searches_get_search_results_export_ad_hoc_v1**
> str searches_get_search_results_export_ad_hoc_v1(export_search_results_request)

Export an ad-hoc search

Operation that returns an ad-hoc search in a specified export format: 0=CSV, 1=Excel, 2=Tab, 3=Word, 4=Custom Separator, 5=Simple JSON. To execute a search with Prompts, the PromptId and Value are required in the Prompt request object.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
export_search_results_request = pycherwell.ExportSearchResultsRequest() # ExportSearchResultsRequest | Request object to specify search parameters and export format.

try:
    # Export an ad-hoc search
    api_response = api_instance.searches_get_search_results_export_ad_hoc_v1(export_search_results_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_export_ad_hoc_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_search_results_request** | [**ExportSearchResultsRequest**](ExportSearchResultsRequest.md)| Request object to specify search parameters and export format. | 

### Return type

**str**

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

# **searches_get_search_results_export_by_id_v1**
> str searches_get_search_results_export_by_id_v1(association, scope, scopeowner, searchid, exportformat, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize)

Export a saved search by ID

Operation that returns the paged results of a saved search in a specified format. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresultsexport ad-hoc http post operation.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Specify the Business Object association ID for the saved search.
scope = 'scope_example' # str | Specify the scope name or ID for the saved search.
scopeowner = 'scopeowner_example' # str | Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
searchid = 'searchid_example' # str | Specify the internal ID for the saved search. Use \"Run a saved search by name\" if you do not have the internal ID.
exportformat = 'exportformat_example' # str | Specify the format of the export
search_term = 'search_term_example' # str | Specify search text filter the results. Example: Use \"Service Request\" to filter Incident results to include only service requests. (optional)
pagenumber = 56 # int | Specify the page number of the result set to return. (optional)
pagesize = 56 # int | Specify the number of rows to return per page. (optional)

try:
    # Export a saved search by ID
    api_response = api_instance.searches_get_search_results_export_by_id_v1(association, scope, scopeowner, searchid, exportformat, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_export_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Specify the Business Object association ID for the saved search. | 
 **scope** | **str**| Specify the scope name or ID for the saved search. | 
 **scopeowner** | **str**| Specify the scope owner ID for the saved search. Use (None) when no scope owner exists. | 
 **searchid** | **str**| Specify the internal ID for the saved search. Use \&quot;Run a saved search by name\&quot; if you do not have the internal ID. | 
 **exportformat** | **str**| Specify the format of the export | 
 **search_term** | **str**| Specify search text filter the results. Example: Use \&quot;Service Request\&quot; to filter Incident results to include only service requests. | [optional] 
 **pagenumber** | **int**| Specify the page number of the result set to return. | [optional] 
 **pagesize** | **int**| Specify the number of rows to return per page. | [optional] 

### Return type

**str**

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

# **searches_get_search_results_export_by_name_v1**
> str searches_get_search_results_export_by_name_v1(association, scope, scopeowner, searchname, exportformat, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize)

Export a saved search by name

Operation that returns the paged results of a saved search in a specified format. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresultsexport ad-hoc http post operation.</br></br>PromptType is a FieldSubType enum as described below:</br>FieldSubType</br>None = 0</br>Text = 1</br>Number = 2</br>DateTime = 3</br>Logical = 4</br>Binary = 5</br>DateOnly = 6</br>TimeOnly = 7</br>Json = 8</br>JsonArray = 9</br>Xml = 10</br>XmlCollection = 11</br>TimeValue = 12</br>

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.SearchesApi()
association = 'association_example' # str | Specify the Business Object association ID for the saved search.
scope = 'scope_example' # str | Specify the scope name or ID for the saved search.
scopeowner = 'scopeowner_example' # str | Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
searchname = 'searchname_example' # str | Specify the name of the saved search.
exportformat = 'exportformat_example' # str | Specify the format of the export
search_term = 'search_term_example' # str | Specify search text filter the results. Example: Use \"Service Request\" to filter Incident results to include only service requests. (optional)
pagenumber = 56 # int | Specify the page number of the result set to return. (optional)
pagesize = 56 # int | Specify the number of rows to return per page. (optional)

try:
    # Export a saved search by name
    api_response = api_instance.searches_get_search_results_export_by_name_v1(association, scope, scopeowner, searchname, exportformat, search_term=search_term, pagenumber=pagenumber, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchesApi->searches_get_search_results_export_by_name_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association** | **str**| Specify the Business Object association ID for the saved search. | 
 **scope** | **str**| Specify the scope name or ID for the saved search. | 
 **scopeowner** | **str**| Specify the scope owner ID for the saved search. Use (None) when no scope owner exists. | 
 **searchname** | **str**| Specify the name of the saved search. | 
 **exportformat** | **str**| Specify the format of the export | 
 **search_term** | **str**| Specify search text filter the results. Example: Use \&quot;Service Request\&quot; to filter Incident results to include only service requests. | [optional] 
 **pagenumber** | **int**| Specify the page number of the result set to return. | [optional] 
 **pagesize** | **int**| Specify the number of rows to return per page. | [optional] 

### Return type

**str**

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


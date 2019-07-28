# pycherwell.FormsApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1**](FormsApi.md#forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1) | **GET** /api/V1/getmobileformforbusob/busobid/{busobid}/publicid/{publicid} | Get mobile form by BusObId and Public ID
[**forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1**](FormsApi.md#forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1) | **GET** /api/V1/getmobileformforbusob/busobid/{busobid}/busobrecid/{busobrecid} | Get mobile form by Business Object ID and Business Object Record ID.
[**forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1**](FormsApi.md#forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1) | **GET** /api/V1/getmobileformforbusob/busobname/{busobname}/publicid/{publicid} | Get mobile form by Business Object name and Public ID
[**forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1**](FormsApi.md#forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1) | **GET** /api/V1/getmobileformforbusob/busobname/{busobname}/busobrecid/{busobrecid} | Get mobile form by Business Object name and record ID.


# **forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1**
> MobileFormResponse forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1(busobid, publicid, foredit=foredit, formid=formid)

Get mobile form by BusObId and Public ID

Operation that gets a mobile form for a specific Business Object by Business Object ID and Public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.FormsApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object Public ID.
foredit = True # bool | Flag to get the edit mode version of a form. (optional)
formid = 'formid_example' # str | Specify the form ID if the default is not desired. (optional)

try:
    # Get mobile form by BusObId and Public ID
    api_response = api_instance.forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1(busobid, publicid, foredit=foredit, formid=formid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->forms_get_mobile_form_for_bus_ob_by_id_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object Public ID. | 
 **foredit** | **bool**| Flag to get the edit mode version of a form. | [optional] 
 **formid** | **str**| Specify the form ID if the default is not desired. | [optional] 

### Return type

[**MobileFormResponse**](MobileFormResponse.md)

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

# **forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1**
> MobileFormResponse forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1(busobid, busobrecid, foredit=foredit, formid=formid)

Get mobile form by Business Object ID and Business Object Record ID.

Operation that gets a mobile form for a specific Business Object by Business Object ID and record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.FormsApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object Record ID.
foredit = True # bool | Flag to get the edit mode version of a form. (optional)
formid = 'formid_example' # str | Specify the form ID if the default is not desired. (optional)

try:
    # Get mobile form by Business Object ID and Business Object Record ID.
    api_response = api_instance.forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1(busobid, busobrecid, foredit=foredit, formid=formid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->forms_get_mobile_form_for_bus_ob_by_id_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object Record ID. | 
 **foredit** | **bool**| Flag to get the edit mode version of a form. | [optional] 
 **formid** | **str**| Specify the form ID if the default is not desired. | [optional] 

### Return type

[**MobileFormResponse**](MobileFormResponse.md)

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

# **forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1**
> MobileFormResponse forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1(busobname, publicid, foredit=foredit, formid=formid)

Get mobile form by Business Object name and Public ID

Operation that gets a mobile form for a specific Business Object by Business Object name and public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.FormsApi()
busobname = 'busobname_example' # str | Specify the Business Object name.
publicid = 'publicid_example' # str | Specify the Business Object public ID.
foredit = True # bool | Flag to get the edit mode version of a form. (optional)
formid = 'formid_example' # str | Specify the form ID if the default is not desired. (optional)

try:
    # Get mobile form by Business Object name and Public ID
    api_response = api_instance.forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1(busobname, publicid, foredit=foredit, formid=formid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->forms_get_mobile_form_for_bus_ob_by_name_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobname** | **str**| Specify the Business Object name. | 
 **publicid** | **str**| Specify the Business Object public ID. | 
 **foredit** | **bool**| Flag to get the edit mode version of a form. | [optional] 
 **formid** | **str**| Specify the form ID if the default is not desired. | [optional] 

### Return type

[**MobileFormResponse**](MobileFormResponse.md)

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

# **forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1**
> MobileFormResponse forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1(busobname, busobrecid, foredit=foredit, formid=formid)

Get mobile form by Business Object name and record ID.

Operation that gets a mobile form for a specific Business Object by Business Object name and record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.FormsApi()
busobname = 'busobname_example' # str | Specify the Business Object name.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.
foredit = True # bool | Flag to get the edit mode version of a form. (optional)
formid = 'formid_example' # str | Specify the form ID if the default is not desired. (optional)

try:
    # Get mobile form by Business Object name and record ID.
    api_response = api_instance.forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1(busobname, busobrecid, foredit=foredit, formid=formid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormsApi->forms_get_mobile_form_for_bus_ob_by_name_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobname** | **str**| Specify the Business Object name. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 
 **foredit** | **bool**| Flag to get the edit mode version of a form. | [optional] 
 **formid** | **str**| Specify the form ID if the default is not desired. | [optional] 

### Return type

[**MobileFormResponse**](MobileFormResponse.md)

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


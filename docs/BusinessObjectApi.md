# pycherwell.BusinessObjectApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**business_object_delete_business_object_batch_v1**](BusinessObjectApi.md#business_object_delete_business_object_batch_v1) | **POST** /api/V1/deletebusinessobjectbatch | Delete Business Objects in a batch
[**business_object_delete_business_object_by_public_id_v1**](BusinessObjectApi.md#business_object_delete_business_object_by_public_id_v1) | **DELETE** /api/V1/deletebusinessobject/busobid/{busobid}/publicid/{publicid} | Delete a Business Object by public ID
[**business_object_delete_business_object_by_rec_id_v1**](BusinessObjectApi.md#business_object_delete_business_object_by_rec_id_v1) | **DELETE** /api/V1/deletebusinessobject/busobid/{busobid}/busobrecid/{busobrecid} | Delete a Business Object by record ID
[**business_object_delete_related_business_object_by_public_id_v1**](BusinessObjectApi.md#business_object_delete_related_business_object_by_public_id_v1) | **DELETE** /api/V1/deleterelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/publicid/{publicid} | Delete a related Business Object by public ID
[**business_object_delete_related_business_object_by_rec_id_v1**](BusinessObjectApi.md#business_object_delete_related_business_object_by_rec_id_v1) | **DELETE** /api/V1/deleterelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobrecid/{busobrecid} | Delete a related Business Object by record ID
[**business_object_field_values_lookup_v1**](BusinessObjectApi.md#business_object_field_values_lookup_v1) | **POST** /api/V1/fieldvalueslookup | Get lookup values for fields
[**business_object_get_business_object_attachment_by_attachment_id_v1**](BusinessObjectApi.md#business_object_get_business_object_attachment_by_attachment_id_v1) | **GET** /api/V1/getbusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/busobrecid/{busobrecid} | Get an imported Business Object attachment
[**business_object_get_business_object_attachments_by_id_and_public_id_v1**](BusinessObjectApi.md#business_object_get_business_object_attachments_by_id_and_public_id_v1) | **GET** /api/V1/getbusinessobjectattachments/busobid/{busobid}/publicid/{publicid}/type/{type}/attachmenttype/{attachmenttype} | Get attachments by Business Object public ID
[**business_object_get_business_object_attachments_by_id_and_rec_id_v1**](BusinessObjectApi.md#business_object_get_business_object_attachments_by_id_and_rec_id_v1) | **GET** /api/V1/getbusinessobjectattachments/busobid/{busobid}/busobrecid/{busobrecid}/type/{type}/attachmenttype/{attachmenttype} | Get attachments by Business Object record ID
[**business_object_get_business_object_attachments_by_name_and_public_id_v1**](BusinessObjectApi.md#business_object_get_business_object_attachments_by_name_and_public_id_v1) | **GET** /api/V1/getbusinessobjectattachments/busobname/{busobname}/publicid/{publicid}/type/{type}/attachmenttype/{attachmenttype} | Get attachments by Business Object name and public ID
[**business_object_get_business_object_attachments_by_name_and_rec_id_v1**](BusinessObjectApi.md#business_object_get_business_object_attachments_by_name_and_rec_id_v1) | **GET** /api/V1/getbusinessobjectattachments/busobname/{busobname}/busobrecid/{busobrecid}/type/{type}/attachmenttype/{attachmenttype} | Get attachments by Business Object name and record ID
[**business_object_get_business_object_attachments_v1**](BusinessObjectApi.md#business_object_get_business_object_attachments_v1) | **POST** /api/V1/getbusinessobjectattachments | Get Business Object attachments by request object
[**business_object_get_business_object_batch_v1**](BusinessObjectApi.md#business_object_get_business_object_batch_v1) | **POST** /api/V1/getbusinessobjectbatch | Get a batch of Business Object records
[**business_object_get_business_object_by_public_id_v1**](BusinessObjectApi.md#business_object_get_business_object_by_public_id_v1) | **GET** /api/V1/getbusinessobject/busobid/{busobid}/publicid/{publicid} | Get a Business Object record
[**business_object_get_business_object_by_rec_id_v1**](BusinessObjectApi.md#business_object_get_business_object_by_rec_id_v1) | **GET** /api/V1/getbusinessobject/busobid/{busobid}/busobrecid/{busobrecid} | Get a Business Object record
[**business_object_get_business_object_by_scan_code_bus_ob_id_v1**](BusinessObjectApi.md#business_object_get_business_object_by_scan_code_bus_ob_id_v1) | **GET** /api/V1/getbusinessobject/scancode/{scanCode}/busobid/{busobid} | Get a Business Object by its scan code and Business Object ID
[**business_object_get_business_object_by_scan_code_bus_ob_name_v1**](BusinessObjectApi.md#business_object_get_business_object_by_scan_code_bus_ob_name_v1) | **GET** /api/V1/getbusinessobject/scancode/{scanCode}/busobname/{busobname} | Get a Business Object by its scan code and Business Object name
[**business_object_get_business_object_schema_v1**](BusinessObjectApi.md#business_object_get_business_object_schema_v1) | **GET** /api/V1/getbusinessobjectschema/busobid/{busobId} | Get a Business Object schema
[**business_object_get_business_object_summaries_v1**](BusinessObjectApi.md#business_object_get_business_object_summaries_v1) | **GET** /api/V1/getbusinessobjectsummaries/type/{type} | Get Business Object summaries by type
[**business_object_get_business_object_summary_by_id_v1**](BusinessObjectApi.md#business_object_get_business_object_summary_by_id_v1) | **GET** /api/V1/getbusinessobjectsummary/busobid/{busobid} | Get a Business Object summary by ID
[**business_object_get_business_object_summary_by_name_v1**](BusinessObjectApi.md#business_object_get_business_object_summary_by_name_v1) | **GET** /api/V1/getbusinessobjectsummary/busobname/{busobname} | Get a Business Object summary by name
[**business_object_get_business_object_template_v1**](BusinessObjectApi.md#business_object_get_business_object_template_v1) | **POST** /api/V1/getbusinessobjecttemplate | Get Business Object templates for create
[**business_object_get_related_business_object_by_request_v1**](BusinessObjectApi.md#business_object_get_related_business_object_by_request_v1) | **POST** /api/V1/getrelatedbusinessobject | Get related Business Objects using a request object
[**business_object_get_related_business_object_v1**](BusinessObjectApi.md#business_object_get_related_business_object_v1) | **GET** /api/V1/getrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid} | Get related Business Objects by ID
[**business_object_get_related_business_object_with_custom_grid_v1**](BusinessObjectApi.md#business_object_get_related_business_object_with_custom_grid_v1) | **GET** /api/V1/getrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/gridid/{gridid} | Get related Business Objects custom grid
[**business_object_link_related_business_object_by_rec_id_v1**](BusinessObjectApi.md#business_object_link_related_business_object_by_rec_id_v1) | **GET** /api/V1/linkrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobid/{busobid}/busobrecid/{busobrecid} | Link related Business Objects
[**business_object_remove_business_object_attachment_by_id_and_public_id_v1**](BusinessObjectApi.md#business_object_remove_business_object_attachment_by_id_and_public_id_v1) | **DELETE** /api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/publicid/{publicid} | Remove an attachment by Business Object ID and public ID
[**business_object_remove_business_object_attachment_by_id_and_rec_id_v1**](BusinessObjectApi.md#business_object_remove_business_object_attachment_by_id_and_rec_id_v1) | **DELETE** /api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/busobrecid/{busobrecid} | Remove an attachment by Business Object ID and record ID
[**business_object_remove_business_object_attachment_by_name_and_public_id_v1**](BusinessObjectApi.md#business_object_remove_business_object_attachment_by_name_and_public_id_v1) | **DELETE** /api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobname/{busobname}/publicid/{publicid} | Remove an attachment by Business Object name and public ID
[**business_object_remove_business_object_attachment_by_name_and_rec_id_v1**](BusinessObjectApi.md#business_object_remove_business_object_attachment_by_name_and_rec_id_v1) | **DELETE** /api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobname/{busobname}/busobrecid/{busobrecid} | Remove an attachment by Business Object name and record ID
[**business_object_save_business_object_attachment_bus_ob_v1**](BusinessObjectApi.md#business_object_save_business_object_attachment_bus_ob_v1) | **PUT** /api/V1/savebusinessobjectattachmentbusob | Attach a Business Object to a Business Object
[**business_object_save_business_object_attachment_link_v1**](BusinessObjectApi.md#business_object_save_business_object_attachment_link_v1) | **PUT** /api/V1/savebusinessobjectattachmentlink | Attach a file via UNC
[**business_object_save_business_object_attachment_url_v1**](BusinessObjectApi.md#business_object_save_business_object_attachment_url_v1) | **PUT** /api/V1/savebusinessobjectattachmenturl | Attach a URL path
[**business_object_save_business_object_batch_v1**](BusinessObjectApi.md#business_object_save_business_object_batch_v1) | **POST** /api/V1/savebusinessobjectbatch | Create or update a batch of Business Objects
[**business_object_save_business_object_v1**](BusinessObjectApi.md#business_object_save_business_object_v1) | **POST** /api/V1/savebusinessobject | Create or Update a Business Object
[**business_object_save_related_business_object_v1**](BusinessObjectApi.md#business_object_save_related_business_object_v1) | **POST** /api/V1/saverelatedbusinessobject | Create or update a related Business Object
[**business_object_un_link_related_business_object_by_rec_id_v1**](BusinessObjectApi.md#business_object_un_link_related_business_object_by_rec_id_v1) | **DELETE** /api/V1/unlinkrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobid/{busobid}/busobrecid/{busobrecid} | UnLink related Business Objects
[**business_object_upload_business_object_attachment_by_id_and_public_id_v1**](BusinessObjectApi.md#business_object_upload_business_object_attachment_by_id_and_public_id_v1) | **POST** /api/V1/uploadbusinessobjectattachment/filename/{filename}/busobid/{busobid}/publicid/{publicid}/offset/{offset}/totalsize/{totalsize} | Upload an attachment by Business Object ID and public ID
[**business_object_upload_business_object_attachment_by_id_and_rec_id_v1**](BusinessObjectApi.md#business_object_upload_business_object_attachment_by_id_and_rec_id_v1) | **POST** /api/V1/uploadbusinessobjectattachment/filename/{filename}/busobid/{busobid}/busobrecid/{busobrecid}/offset/{offset}/totalsize/{totalsize} | Upload an attachment by Business Object ID and record ID
[**business_object_upload_business_object_attachment_by_name_and_public_id_v1**](BusinessObjectApi.md#business_object_upload_business_object_attachment_by_name_and_public_id_v1) | **POST** /api/V1/uploadbusinessobjectattachment/filename/{filename}/busobname/{busobname}/publicid/{publicid}/offset/{offset}/totalsize/{totalsize} | Upload an attachment by Business Object name and public ID
[**business_object_upload_business_object_attachment_by_name_and_rec_id_v1**](BusinessObjectApi.md#business_object_upload_business_object_attachment_by_name_and_rec_id_v1) | **POST** /api/V1/uploadbusinessobjectattachment/filename/{filename}/busobname/{busobname}/busobrecid/{busobrecid}/offset/{offset}/totalsize/{totalsize} | Upload an attachment by Business Object name and record ID


# **business_object_delete_business_object_batch_v1**
> BatchDeleteResponse business_object_delete_business_object_batch_v1(batch_delete_request)

Delete Business Objects in a batch

Operation to delete a batch of Business Objects.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
batch_delete_request = pycherwell.BatchDeleteRequest() # BatchDeleteRequest | Specify an array of Business Object IDs and record IDs or public IDs. Use a flag to stop on error or continue on error.

try:
    # Delete Business Objects in a batch
    api_response = api_instance.business_object_delete_business_object_batch_v1(batch_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_delete_business_object_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_delete_request** | [**BatchDeleteRequest**](BatchDeleteRequest.md)| Specify an array of Business Object IDs and record IDs or public IDs. Use a flag to stop on error or continue on error. | 

### Return type

[**BatchDeleteResponse**](BatchDeleteResponse.md)

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

# **business_object_delete_business_object_by_public_id_v1**
> DeleteResponse business_object_delete_business_object_by_public_id_v1(busobid, publicid)

Delete a Business Object by public ID

Operation to delete a Business Object by Business Object ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object public ID.

try:
    # Delete a Business Object by public ID
    api_response = api_instance.business_object_delete_business_object_by_public_id_v1(busobid, publicid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_delete_business_object_by_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object public ID. | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

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

# **business_object_delete_business_object_by_rec_id_v1**
> DeleteResponse business_object_delete_business_object_by_rec_id_v1(busobid, busobrecid)

Delete a Business Object by record ID

Operation to delete a single Business Object.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str |  Specify the Business Object record ID.

try:
    # Delete a Business Object by record ID
    api_response = api_instance.business_object_delete_business_object_by_rec_id_v1(busobid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_delete_business_object_by_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**|  Specify the Business Object record ID. | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

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

# **business_object_delete_related_business_object_by_public_id_v1**
> RelatedBusinessObjectResponse business_object_delete_related_business_object_by_public_id_v1(parentbusobid, parentbusobrecid, relationshipid, publicid)

Delete a related Business Object by public ID

Operation to delete a related Business Object. (Use \"Unlink Related Business Object\" to unlink two Business Objects rather that deleting the related Business Object.)

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to delete.
publicid = 'publicid_example' # str | Specify the public ID for the related Business Object you want to delete. Use only for Business Objects with unique public IDs. Use \"Delete a related Business Object by record ID\" when public IDs are not unique.

try:
    # Delete a related Business Object by public ID
    api_response = api_instance.business_object_delete_related_business_object_by_public_id_v1(parentbusobid, parentbusobrecid, relationshipid, publicid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_delete_related_business_object_by_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to delete. | 
 **publicid** | **str**| Specify the public ID for the related Business Object you want to delete. Use only for Business Objects with unique public IDs. Use \&quot;Delete a related Business Object by record ID\&quot; when public IDs are not unique. | 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_delete_related_business_object_by_rec_id_v1**
> RelatedBusinessObjectResponse business_object_delete_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobrecid)

Delete a related Business Object by record ID

Operation to delete a related Business Object. (Use \"Unlink Related Business Object\" to unlink two Business Objects rather that deleting the related Business Object.)

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to delete.
busobrecid = 'busobrecid_example' # str | Specify the record ID for the related Business Object you want to delete.

try:
    # Delete a related Business Object by record ID
    api_response = api_instance.business_object_delete_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_delete_related_business_object_by_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to delete. | 
 **busobrecid** | **str**| Specify the record ID for the related Business Object you want to delete. | 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_field_values_lookup_v1**
> FieldValuesLookupResponse business_object_field_values_lookup_v1(field_values_lookup_request)

Get lookup values for fields

Operation to get potentially valid values for Business Object fields.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
field_values_lookup_request = pycherwell.FieldValuesLookupRequest() # FieldValuesLookupRequest | Request object that specifies the Business Object and fields for which values are to be returned.

try:
    # Get lookup values for fields
    api_response = api_instance.business_object_field_values_lookup_v1(field_values_lookup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_field_values_lookup_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_values_lookup_request** | [**FieldValuesLookupRequest**](FieldValuesLookupRequest.md)| Request object that specifies the Business Object and fields for which values are to be returned. | 

### Return type

[**FieldValuesLookupResponse**](FieldValuesLookupResponse.md)

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

# **business_object_get_business_object_attachment_by_attachment_id_v1**
> file business_object_get_business_object_attachment_by_attachment_id_v1(attachmentid, busobid, busobrecid)

Get an imported Business Object attachment

Operation to get a Business Object attachment that has been imported into the system.  HTTP Range Header can be used but is optional.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachmentid = 'attachmentid_example' # str | Specify the internal ID of the attachment record that contains information about the imported file.
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.

try:
    # Get an imported Business Object attachment
    api_response = api_instance.business_object_get_business_object_attachment_by_attachment_id_v1(attachmentid, busobid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachment_by_attachment_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachmentid** | **str**| Specify the internal ID of the attachment record that contains information about the imported file. | 
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_object_get_business_object_attachments_by_id_and_public_id_v1**
> AttachmentsResponse business_object_get_business_object_attachments_by_id_and_public_id_v1(busobid, publicid, type, attachmenttype, includelinks=includelinks)

Get attachments by Business Object public ID

Operation to get attachments for a Business Object by Business Object ID and public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object public ID for the record that contains the attachments.
type = 'type_example' # str | Record attachment type: </br></br>None - Not applicable to the REST API. </br></br>File - Linked files. </br></br>FileManagerFile - Imported files.</br></br>BusOb - Attached Business Objects. </br></br>History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.</br></br>Other - Not applicable to the REST API. </br>
attachmenttype = 'attachmenttype_example' # str | For file types, select the type of attachment: </br></br>Imported - Attachment was imported into database. </br></br>Linked - Attachment is linked to an external file. </br></br>URL - Attachment is a URL.
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get attachments by Business Object public ID
    api_response = api_instance.business_object_get_business_object_attachments_by_id_and_public_id_v1(busobid, publicid, type, attachmenttype, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachments_by_id_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object public ID for the record that contains the attachments. | 
 **type** | **str**| Record attachment type: &lt;/br&gt;&lt;/br&gt;None - Not applicable to the REST API. &lt;/br&gt;&lt;/br&gt;File - Linked files. &lt;/br&gt;&lt;/br&gt;FileManagerFile - Imported files.&lt;/br&gt;&lt;/br&gt;BusOb - Attached Business Objects. &lt;/br&gt;&lt;/br&gt;History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.&lt;/br&gt;&lt;/br&gt;Other - Not applicable to the REST API. &lt;/br&gt; | 
 **attachmenttype** | **str**| For file types, select the type of attachment: &lt;/br&gt;&lt;/br&gt;Imported - Attachment was imported into database. &lt;/br&gt;&lt;/br&gt;Linked - Attachment is linked to an external file. &lt;/br&gt;&lt;/br&gt;URL - Attachment is a URL. | 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_get_business_object_attachments_by_id_and_rec_id_v1**
> AttachmentsResponse business_object_get_business_object_attachments_by_id_and_rec_id_v1(busobid, busobrecid, type, attachmenttype, includelinks=includelinks)

Get attachments by Business Object record ID

Operation to get attachments for a Business Object by Business Object ID and record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.
type = 'type_example' # str | Record attachment type: </br></br>None - Not applicable to the REST API. </br></br>File - Linked files. </br></br>FileManagerFile - Imported files.</br></br>BusOb - Attached Business Objects. </br></br>History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.</br></br>Other - Not applicable to the REST API. </br>
attachmenttype = 'attachmenttype_example' # str | For file types, select the type of attachment: </br></br>Imported - Attachment was imported into database. </br></br>Linked - Attachment is linked to an external file. </br></br>URL - Attachment is a URL.
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get attachments by Business Object record ID
    api_response = api_instance.business_object_get_business_object_attachments_by_id_and_rec_id_v1(busobid, busobrecid, type, attachmenttype, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachments_by_id_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 
 **type** | **str**| Record attachment type: &lt;/br&gt;&lt;/br&gt;None - Not applicable to the REST API. &lt;/br&gt;&lt;/br&gt;File - Linked files. &lt;/br&gt;&lt;/br&gt;FileManagerFile - Imported files.&lt;/br&gt;&lt;/br&gt;BusOb - Attached Business Objects. &lt;/br&gt;&lt;/br&gt;History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.&lt;/br&gt;&lt;/br&gt;Other - Not applicable to the REST API. &lt;/br&gt; | 
 **attachmenttype** | **str**| For file types, select the type of attachment: &lt;/br&gt;&lt;/br&gt;Imported - Attachment was imported into database. &lt;/br&gt;&lt;/br&gt;Linked - Attachment is linked to an external file. &lt;/br&gt;&lt;/br&gt;URL - Attachment is a URL. | 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_get_business_object_attachments_by_name_and_public_id_v1**
> AttachmentsResponse business_object_get_business_object_attachments_by_name_and_public_id_v1(busobname, publicid, type, attachmenttype, includelinks=includelinks)

Get attachments by Business Object name and public ID

Operation to get attachments for a Business Object by Business Object Name and public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobname = 'busobname_example' # str | Specify the Business Object name.
publicid = 'publicid_example' # str | Specify the Business Object public ID for the record that contains the attachments.
type = 'type_example' # str | Record attachment type: </br></br>None - Not applicable to the REST API. </br></br>File - Linked files. </br></br>FileManagerFile - Imported files.</br></br>BusOb - Attached Business Objects. </br></br>History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.</br></br>Other - Not applicable to the REST API. </br>
attachmenttype = 'attachmenttype_example' # str | For file types, select the type of attachment: </br></br>Imported - Attachment was imported into database. </br></br>Linked - Attachment is linked to an external file. </br></br>URL - Attachment is a URL.
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get attachments by Business Object name and public ID
    api_response = api_instance.business_object_get_business_object_attachments_by_name_and_public_id_v1(busobname, publicid, type, attachmenttype, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachments_by_name_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobname** | **str**| Specify the Business Object name. | 
 **publicid** | **str**| Specify the Business Object public ID for the record that contains the attachments. | 
 **type** | **str**| Record attachment type: &lt;/br&gt;&lt;/br&gt;None - Not applicable to the REST API. &lt;/br&gt;&lt;/br&gt;File - Linked files. &lt;/br&gt;&lt;/br&gt;FileManagerFile - Imported files.&lt;/br&gt;&lt;/br&gt;BusOb - Attached Business Objects. &lt;/br&gt;&lt;/br&gt;History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.&lt;/br&gt;&lt;/br&gt;Other - Not applicable to the REST API. &lt;/br&gt; | 
 **attachmenttype** | **str**| For file types, select the type of attachment: &lt;/br&gt;&lt;/br&gt;Imported - Attachment was imported into database. &lt;/br&gt;&lt;/br&gt;Linked - Attachment is linked to an external file. &lt;/br&gt;&lt;/br&gt;URL - Attachment is a URL. | 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_get_business_object_attachments_by_name_and_rec_id_v1**
> AttachmentsResponse business_object_get_business_object_attachments_by_name_and_rec_id_v1(busobname, busobrecid, type, attachmenttype, includelinks=includelinks)

Get attachments by Business Object name and record ID

Operation to get attachments for a Business Object by name and record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobname = 'busobname_example' # str | Specify the Business Object name.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.
type = 'type_example' # str | Record attachment type: </br></br>None - Not applicable to the REST API. </br></br>File - Linked files. </br></br>FileManagerFile - Imported files.</br></br>BusOb - Attached Business Objects. </br></br>History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.</br></br>Other - Not applicable to the REST API. </br>
attachmenttype = 'attachmenttype_example' # str | For file types, select the type of attachment: </br></br>Imported - Attachment was imported into database. </br></br>Linked - Attachment is linked to an external file. </br></br>URL - Attachment is a URL.
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get attachments by Business Object name and record ID
    api_response = api_instance.business_object_get_business_object_attachments_by_name_and_rec_id_v1(busobname, busobrecid, type, attachmenttype, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachments_by_name_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobname** | **str**| Specify the Business Object name. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 
 **type** | **str**| Record attachment type: &lt;/br&gt;&lt;/br&gt;None - Not applicable to the REST API. &lt;/br&gt;&lt;/br&gt;File - Linked files. &lt;/br&gt;&lt;/br&gt;FileManagerFile - Imported files.&lt;/br&gt;&lt;/br&gt;BusOb - Attached Business Objects. &lt;/br&gt;&lt;/br&gt;History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.&lt;/br&gt;&lt;/br&gt;Other - Not applicable to the REST API. &lt;/br&gt; | 
 **attachmenttype** | **str**| For file types, select the type of attachment: &lt;/br&gt;&lt;/br&gt;Imported - Attachment was imported into database. &lt;/br&gt;&lt;/br&gt;Linked - Attachment is linked to an external file. &lt;/br&gt;&lt;/br&gt;URL - Attachment is a URL. | 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_get_business_object_attachments_v1**
> AttachmentsResponse business_object_get_business_object_attachments_v1(attachments_request)

Get Business Object attachments by request object

Operation to get attachments for a Business Object by attachments request object.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachments_request = pycherwell.AttachmentsRequest() # AttachmentsRequest | Object with all the parameters to request an attachments list. You can also request a list of types to get more than just one type at a time.

try:
    # Get Business Object attachments by request object
    api_response = api_instance.business_object_get_business_object_attachments_v1(attachments_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_attachments_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_request** | [**AttachmentsRequest**](AttachmentsRequest.md)| Object with all the parameters to request an attachments list. You can also request a list of types to get more than just one type at a time. | 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_get_business_object_batch_v1**
> BatchReadResponse business_object_get_business_object_batch_v1(batch_read_request)

Get a batch of Business Object records

Operation that returns a batch of Business Object records that includes a list of field record IDs, display names, and values for each record.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
batch_read_request = pycherwell.BatchReadRequest() # BatchReadRequest | Specify an array of Business Object IDs, record IDs, or public IDs. Use a flag to stop on error or continue on error.

try:
    # Get a batch of Business Object records
    api_response = api_instance.business_object_get_business_object_batch_v1(batch_read_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_read_request** | [**BatchReadRequest**](BatchReadRequest.md)| Specify an array of Business Object IDs, record IDs, or public IDs. Use a flag to stop on error or continue on error. | 

### Return type

[**BatchReadResponse**](BatchReadResponse.md)

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

# **business_object_get_business_object_by_public_id_v1**
> ReadResponse business_object_get_business_object_by_public_id_v1(busobid, publicid)

Get a Business Object record

Operation that returns a Business Object record that includes a list of fields and their record IDs, names, and set values.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object public ID.

try:
    # Get a Business Object record
    api_response = api_instance.business_object_get_business_object_by_public_id_v1(busobid, publicid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_by_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object public ID. | 

### Return type

[**ReadResponse**](ReadResponse.md)

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

# **business_object_get_business_object_by_rec_id_v1**
> ReadResponse business_object_get_business_object_by_rec_id_v1(busobid, busobrecid)

Get a Business Object record

Operation that returns a Business Object record that includes a list of fields and their record IDs, names, and set values.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.

try:
    # Get a Business Object record
    api_response = api_instance.business_object_get_business_object_by_rec_id_v1(busobid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_by_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 

### Return type

[**ReadResponse**](ReadResponse.md)

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

# **business_object_get_business_object_by_scan_code_bus_ob_id_v1**
> BarcodeLookupResponse business_object_get_business_object_by_scan_code_bus_ob_id_v1(scan_code, busobid)

Get a Business Object by its scan code and Business Object ID

Operation to get a Business Object based on its associated scan code and Business Object ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
scan_code = 'scan_code_example' # str | The scan code for a Business Object record.
busobid = 'busobid_example' # str | The Business Object ID.

try:
    # Get a Business Object by its scan code and Business Object ID
    api_response = api_instance.business_object_get_business_object_by_scan_code_bus_ob_id_v1(scan_code, busobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_by_scan_code_bus_ob_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_code** | **str**| The scan code for a Business Object record. | 
 **busobid** | **str**| The Business Object ID. | 

### Return type

[**BarcodeLookupResponse**](BarcodeLookupResponse.md)

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

# **business_object_get_business_object_by_scan_code_bus_ob_name_v1**
> BarcodeLookupResponse business_object_get_business_object_by_scan_code_bus_ob_name_v1(scan_code, busobname)

Get a Business Object by its scan code and Business Object name

Operation to get a Business Object based on its associated scan code and Business Object name.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
scan_code = 'scan_code_example' # str | The scan code for a Business Object record.
busobname = 'busobname_example' # str | The Business Bbject name.

try:
    # Get a Business Object by its scan code and Business Object name
    api_response = api_instance.business_object_get_business_object_by_scan_code_bus_ob_name_v1(scan_code, busobname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_by_scan_code_bus_ob_name_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_code** | **str**| The scan code for a Business Object record. | 
 **busobname** | **str**| The Business Bbject name. | 

### Return type

[**BarcodeLookupResponse**](BarcodeLookupResponse.md)

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

# **business_object_get_business_object_schema_v1**
> SchemaResponse business_object_get_business_object_schema_v1(busob_id, includerelationships=includerelationships)

Get a Business Object schema

Operation that returns the schema for a Business Object and, optionally, its related Business Objects.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busob_id = 'busob_id_example' # str | Specify the Business Object ID.
includerelationships = True # bool | Flag to include schemas for related Business Object. Default is false. (optional)

try:
    # Get a Business Object schema
    api_response = api_instance.business_object_get_business_object_schema_v1(busob_id, includerelationships=includerelationships)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_schema_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busob_id** | **str**| Specify the Business Object ID. | 
 **includerelationships** | **bool**| Flag to include schemas for related Business Object. Default is false. | [optional] 

### Return type

[**SchemaResponse**](SchemaResponse.md)

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

# **business_object_get_business_object_summaries_v1**
> list[Summary] business_object_get_business_object_summaries_v1(type)

Get Business Object summaries by type

Operation that returns a list of Business Object summaries by type (Major, Supporting, Lookup, Groups, and All). 

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
type = 'type_example' # str | Use to show:<br />All - All objects<br />Major - Major objects only<br />Supporting - Supporting objects only<br />Lookup - Lookup objects only<br />Groups - Groups only

try:
    # Get Business Object summaries by type
    api_response = api_instance.business_object_get_business_object_summaries_v1(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_summaries_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Use to show:&lt;br /&gt;All - All objects&lt;br /&gt;Major - Major objects only&lt;br /&gt;Supporting - Supporting objects only&lt;br /&gt;Lookup - Lookup objects only&lt;br /&gt;Groups - Groups only | 

### Return type

[**list[Summary]**](Summary.md)

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

# **business_object_get_business_object_summary_by_id_v1**
> list[Summary] business_object_get_business_object_summary_by_id_v1(busobid)

Get a Business Object summary by ID

Operation that returns a single Business Object summary by ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobid = 'busobid_example' # str | Specify a Business Object ID to get its summary.

try:
    # Get a Business Object summary by ID
    api_response = api_instance.business_object_get_business_object_summary_by_id_v1(busobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_summary_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobid** | **str**| Specify a Business Object ID to get its summary. | 

### Return type

[**list[Summary]**](Summary.md)

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

# **business_object_get_business_object_summary_by_name_v1**
> list[Summary] business_object_get_business_object_summary_by_name_v1(busobname)

Get a Business Object summary by name

Operation that returns a single Business Object summary by name.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
busobname = 'busobname_example' # str | Specify a Business Object name to get its summary.

try:
    # Get a Business Object summary by name
    api_response = api_instance.business_object_get_business_object_summary_by_name_v1(busobname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_summary_by_name_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busobname** | **str**| Specify a Business Object name to get its summary. | 

### Return type

[**list[Summary]**](Summary.md)

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

# **business_object_get_business_object_template_v1**
> TemplateResponse business_object_get_business_object_template_v1(template_request)

Get Business Object templates for create

Operation that returns a template to create Business Objects.  The template includes placeholders for field values. You can then send the template with these values to the Business Object Save operation.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
template_request = pycherwell.TemplateRequest() # TemplateRequest | Specify the Business Object ID. Use true to include all required fields or all fields. Specify an optional fields list by adding field names in a comma-delimited list [\"field1\", \"field2\"]. 

try:
    # Get Business Object templates for create
    api_response = api_instance.business_object_get_business_object_template_v1(template_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_business_object_template_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_request** | [**TemplateRequest**](TemplateRequest.md)| Specify the Business Object ID. Use true to include all required fields or all fields. Specify an optional fields list by adding field names in a comma-delimited list [\&quot;field1\&quot;, \&quot;field2\&quot;].  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

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

# **business_object_get_related_business_object_by_request_v1**
> RelatedBusinessObjectResponse business_object_get_related_business_object_by_request_v1(related_business_object_request, includelinks=includelinks)

Get related Business Objects using a request object

Operation to get related Business Objects for a specific relationship. Specify a list of fields to include in the response. The order of parameter usage and overrides is: all fields set to true overrides default overrides;  custom grid overrides field list settings.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
related_business_object_request = pycherwell.RelatedBusinessObjectRequest() # RelatedBusinessObjectRequest | Request object containing all the possible parameters to get related Business Objects.
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get related Business Objects using a request object
    api_response = api_instance.business_object_get_related_business_object_by_request_v1(related_business_object_request, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_related_business_object_by_request_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **related_business_object_request** | [**RelatedBusinessObjectRequest**](RelatedBusinessObjectRequest.md)| Request object containing all the possible parameters to get related Business Objects. | 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_get_related_business_object_v1**
> RelatedBusinessObjectResponse business_object_get_related_business_object_v1(parentbusobid, parentbusobrecid, relationshipid, page_number=page_number, page_size=page_size, allfields=allfields, usedefaultgrid=usedefaultgrid, includelinks=includelinks)

Get related Business Objects by ID

Operation to get the related objects for a Business Object relationship specifying all fields or default grid as the field to return.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object.
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to return.
page_number = 56 # int | Specify the page number of the result set to return. (optional)
page_size = 56 # int | Specify the number of rows to return per page. (optional)
allfields = True # bool | Flag to include all related Business Object fields.  Default is true if not supplied.  If true, then UseDefaultGrid is not used. (optional)
usedefaultgrid = True # bool | Flag to trigger the use of the related Business Objects default grid for the list of fields to return. (optional)
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get related Business Objects by ID
    api_response = api_instance.business_object_get_related_business_object_v1(parentbusobid, parentbusobrecid, relationshipid, page_number=page_number, page_size=page_size, allfields=allfields, usedefaultgrid=usedefaultgrid, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_related_business_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object. | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to return. | 
 **page_number** | **int**| Specify the page number of the result set to return. | [optional] 
 **page_size** | **int**| Specify the number of rows to return per page. | [optional] 
 **allfields** | **bool**| Flag to include all related Business Object fields.  Default is true if not supplied.  If true, then UseDefaultGrid is not used. | [optional] 
 **usedefaultgrid** | **bool**| Flag to trigger the use of the related Business Objects default grid for the list of fields to return. | [optional] 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_get_related_business_object_with_custom_grid_v1**
> RelatedBusinessObjectResponse business_object_get_related_business_object_with_custom_grid_v1(parentbusobid, parentbusobrecid, relationshipid, gridid, page_number=page_number, page_size=page_size, includelinks=includelinks)

Get related Business Objects custom grid

Operation to get related Business Objects for a specific relationship. Specify a custom grid ID as the fields to return.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object.
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to return.
gridid = 'gridid_example' # str | Specify the ID for the custom grid that contains the field list.
page_number = 56 # int | Specify the page number of the result set to return. (optional)
page_size = 56 # int | Specify the number of rows to return per page. (optional)
includelinks = True # bool | Flag to include hyperlinks in results. Default is false.  (optional)

try:
    # Get related Business Objects custom grid
    api_response = api_instance.business_object_get_related_business_object_with_custom_grid_v1(parentbusobid, parentbusobrecid, relationshipid, gridid, page_number=page_number, page_size=page_size, includelinks=includelinks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_get_related_business_object_with_custom_grid_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object. | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to return. | 
 **gridid** | **str**| Specify the ID for the custom grid that contains the field list. | 
 **page_number** | **int**| Specify the page number of the result set to return. | [optional] 
 **page_size** | **int**| Specify the number of rows to return per page. | [optional] 
 **includelinks** | **bool**| Flag to include hyperlinks in results. Default is false.  | [optional] 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_link_related_business_object_by_rec_id_v1**
> RelatedBusinessObjectResponse business_object_link_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobid, busobrecid)

Link related Business Objects

Operation to link related Business Objects. 

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object.
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to link.
busobid = 'busobid_example' # str | Specify the Business Object ID of the Business Object to be linked.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID of the Business Object to be linked.

try:
    # Link related Business Objects
    api_response = api_instance.business_object_link_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_link_related_business_object_by_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object. | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to link. | 
 **busobid** | **str**| Specify the Business Object ID of the Business Object to be linked. | 
 **busobrecid** | **str**| Specify the Business Object record ID of the Business Object to be linked. | 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_remove_business_object_attachment_by_id_and_public_id_v1**
> business_object_remove_business_object_attachment_by_id_and_public_id_v1(attachmentid, busobid, publicid)

Remove an attachment by Business Object ID and public ID

Operation to remove an attachment from a Business Object using the attachment record ID, Business Object ID, and Business Object public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachmentid = 'attachmentid_example' # str | Specify the internal ID of the attachment record.
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object public ID.

try:
    # Remove an attachment by Business Object ID and public ID
    api_instance.business_object_remove_business_object_attachment_by_id_and_public_id_v1(attachmentid, busobid, publicid)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_remove_business_object_attachment_by_id_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachmentid** | **str**| Specify the internal ID of the attachment record. | 
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object public ID. | 

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

# **business_object_remove_business_object_attachment_by_id_and_rec_id_v1**
> business_object_remove_business_object_attachment_by_id_and_rec_id_v1(attachmentid, busobid, busobrecid)

Remove an attachment by Business Object ID and record ID

Operation to remove an attachment from a Business Object using the attachment record ID, Business Object ID, and Business Object record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachmentid = 'attachmentid_example' # str | Specify the internal ID of the attachment record.
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.

try:
    # Remove an attachment by Business Object ID and record ID
    api_instance.business_object_remove_business_object_attachment_by_id_and_rec_id_v1(attachmentid, busobid, busobrecid)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_remove_business_object_attachment_by_id_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachmentid** | **str**| Specify the internal ID of the attachment record. | 
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 

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

# **business_object_remove_business_object_attachment_by_name_and_public_id_v1**
> business_object_remove_business_object_attachment_by_name_and_public_id_v1(attachmentid, busobname, publicid)

Remove an attachment by Business Object name and public ID

Operation to remove an attachment from a Business Object using the attachment record ID, Business Object name, and Business Object record ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachmentid = 'attachmentid_example' # str | Specify the internal ID of the attachment record.
busobname = 'busobname_example' # str | Specify the Business Object name.
publicid = 'publicid_example' # str | Specify the Business Object public ID.

try:
    # Remove an attachment by Business Object name and public ID
    api_instance.business_object_remove_business_object_attachment_by_name_and_public_id_v1(attachmentid, busobname, publicid)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_remove_business_object_attachment_by_name_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachmentid** | **str**| Specify the internal ID of the attachment record. | 
 **busobname** | **str**| Specify the Business Object name. | 
 **publicid** | **str**| Specify the Business Object public ID. | 

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

# **business_object_remove_business_object_attachment_by_name_and_rec_id_v1**
> business_object_remove_business_object_attachment_by_name_and_rec_id_v1(attachmentid, busobname, busobrecid)

Remove an attachment by Business Object name and record ID

Operation to remove an attachment from a Business Object using the attachment record ID, Business Object name, and Business Object public ID.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
attachmentid = 'attachmentid_example' # str | Specify the internal ID of the attachment record.
busobname = 'busobname_example' # str | Specify the Business Object name.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID.

try:
    # Remove an attachment by Business Object name and record ID
    api_instance.business_object_remove_business_object_attachment_by_name_and_rec_id_v1(attachmentid, busobname, busobrecid)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_remove_business_object_attachment_by_name_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachmentid** | **str**| Specify the internal ID of the attachment record. | 
 **busobname** | **str**| Specify the Business Object name. | 
 **busobrecid** | **str**| Specify the Business Object record ID. | 

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

# **business_object_save_business_object_attachment_bus_ob_v1**
> AttachmentsResponse business_object_save_business_object_attachment_bus_ob_v1(save_bus_ob_attachment_request)

Attach a Business Object to a Business Object

Operation to attach a Business Object to a Business Object. This links the Business Object but does not create a relationship between the two. (Use \"Link Related Business Objects\" to create a relationship.)

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
save_bus_ob_attachment_request = pycherwell.SaveBusObAttachmentRequest() # SaveBusObAttachmentRequest | Request object used to specify the Business Objects to attach. You can use Business Object name or ID and Business Object record ID or public ID.

try:
    # Attach a Business Object to a Business Object
    api_response = api_instance.business_object_save_business_object_attachment_bus_ob_v1(save_bus_ob_attachment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_business_object_attachment_bus_ob_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_bus_ob_attachment_request** | [**SaveBusObAttachmentRequest**](SaveBusObAttachmentRequest.md)| Request object used to specify the Business Objects to attach. You can use Business Object name or ID and Business Object record ID or public ID. | 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_save_business_object_attachment_link_v1**
> AttachmentsResponse business_object_save_business_object_attachment_link_v1(save_link_attachment_request)

Attach a file via UNC

Operation to attach a file to a Business Object via a path (UNC recommended).

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
save_link_attachment_request = pycherwell.SaveLinkAttachmentRequest() # SaveLinkAttachmentRequest | Request object used to specify the file path (UNC recommended) and the Business Object. You can use Business Object name or ID and Business Object record ID or public ID.

try:
    # Attach a file via UNC
    api_response = api_instance.business_object_save_business_object_attachment_link_v1(save_link_attachment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_business_object_attachment_link_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_link_attachment_request** | [**SaveLinkAttachmentRequest**](SaveLinkAttachmentRequest.md)| Request object used to specify the file path (UNC recommended) and the Business Object. You can use Business Object name or ID and Business Object record ID or public ID. | 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_save_business_object_attachment_url_v1**
> AttachmentsResponse business_object_save_business_object_attachment_url_v1(save_url_attachment_request)

Attach a URL path

Operation to attach a URL path to a Business Object.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
save_url_attachment_request = pycherwell.SaveUrlAttachmentRequest() # SaveUrlAttachmentRequest | Request object used to specify the URL path and Business Object. You can use Business Object name or ID and Business Object record ID or public ID.

try:
    # Attach a URL path
    api_response = api_instance.business_object_save_business_object_attachment_url_v1(save_url_attachment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_business_object_attachment_url_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_url_attachment_request** | [**SaveUrlAttachmentRequest**](SaveUrlAttachmentRequest.md)| Request object used to specify the URL path and Business Object. You can use Business Object name or ID and Business Object record ID or public ID. | 

### Return type

[**AttachmentsResponse**](AttachmentsResponse.md)

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

# **business_object_save_business_object_batch_v1**
> BatchSaveResponse business_object_save_business_object_batch_v1(batch_save_request)

Create or update a batch of Business Objects

Operation that creates or updates an array of Business Objects in a batch. To update, specify record ID or public ID. To create, leave record ID and public ID empty.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
batch_save_request = pycherwell.BatchSaveRequest() # BatchSaveRequest | Specify the array of Business Object templates. 

try:
    # Create or update a batch of Business Objects
    api_response = api_instance.business_object_save_business_object_batch_v1(batch_save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_business_object_batch_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_save_request** | [**BatchSaveRequest**](BatchSaveRequest.md)| Specify the array of Business Object templates.  | 

### Return type

[**BatchSaveResponse**](BatchSaveResponse.md)

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

# **business_object_save_business_object_v1**
> SaveResponse business_object_save_business_object_v1(save_request)

Create or Update a Business Object

Operation that creates a new Business Object or updates an existing Business Object. To create, leave record ID and public ID empty. Upon creating or saving, a cache key is returned to use for subsequent requests. If the object is not found in the cache with said cache key, specify record ID or public ID to save and return a new cache key. Set persist = true, to actually save the Business Object to disk, persist = false will just cache it.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
save_request = pycherwell.SaveRequest() # SaveRequest | Specify a list of fields from a Business Object template. 

try:
    # Create or Update a Business Object
    api_response = api_instance.business_object_save_business_object_v1(save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_business_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_request** | [**SaveRequest**](SaveRequest.md)| Specify a list of fields from a Business Object template.  | 

### Return type

[**SaveResponse**](SaveResponse.md)

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

# **business_object_save_related_business_object_v1**
> RelatedSaveResponse business_object_save_related_business_object_v1(related_save_request)

Create or update a related Business Object

Operation that creates or updates a related Business Object. To update, specify record ID or public ID. To create, leave record ID and public ID empty.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
related_save_request = pycherwell.RelatedSaveRequest() # RelatedSaveRequest | Request object specifying the parent the Business Object, the Relationship, and field values for the Business Object to create or update. 

try:
    # Create or update a related Business Object
    api_response = api_instance.business_object_save_related_business_object_v1(related_save_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_save_related_business_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **related_save_request** | [**RelatedSaveRequest**](RelatedSaveRequest.md)| Request object specifying the parent the Business Object, the Relationship, and field values for the Business Object to create or update.  | 

### Return type

[**RelatedSaveResponse**](RelatedSaveResponse.md)

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

# **business_object_un_link_related_business_object_by_rec_id_v1**
> RelatedBusinessObjectResponse business_object_un_link_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobid, busobrecid)

UnLink related Business Objects

Operation to unlink related Business Objects.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
parentbusobid = 'parentbusobid_example' # str | Specify the Business Object ID for the parent Business Object.
parentbusobrecid = 'parentbusobrecid_example' # str | Specify the record ID for the parent Business Object.
relationshipid = 'relationshipid_example' # str | Specify the Relationship ID for the related Business Object you want to unlink.
busobid = 'busobid_example' # str | Specify the Business Object ID of the Business Object to be unlinked.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID of the Business Object to be unlinked.

try:
    # UnLink related Business Objects
    api_response = api_instance.business_object_un_link_related_business_object_by_rec_id_v1(parentbusobid, parentbusobrecid, relationshipid, busobid, busobrecid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_un_link_related_business_object_by_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentbusobid** | **str**| Specify the Business Object ID for the parent Business Object. | 
 **parentbusobrecid** | **str**| Specify the record ID for the parent Business Object. | 
 **relationshipid** | **str**| Specify the Relationship ID for the related Business Object you want to unlink. | 
 **busobid** | **str**| Specify the Business Object ID of the Business Object to be unlinked. | 
 **busobrecid** | **str**| Specify the Business Object record ID of the Business Object to be unlinked. | 

### Return type

[**RelatedBusinessObjectResponse**](RelatedBusinessObjectResponse.md)

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

# **business_object_upload_business_object_attachment_by_id_and_public_id_v1**
> str business_object_upload_business_object_attachment_by_id_and_public_id_v1(filename, busobid, publicid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)

Upload an attachment by Business Object ID and public ID

Operation to upload an attachment to a Business Object record using a Business Object ID and public ID. The body of the request is the byte array of the file part being uploaded.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
filename = 'filename_example' # str | Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
busobid = 'busobid_example' # str | Specify the Business Object ID.
publicid = 'publicid_example' # str | Specify the Business Object public ID  to attach the file to.
offset = 56 # int | The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
totalsize = 56 # int | The entire file size in bytes.
body = '/path/to/file' # file | 
attachmentid = 'attachmentid_example' # str | Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. (optional)
displaytext = 'displaytext_example' # str | Specify the attachment name, which is the display text for the attachment record. (optional)

try:
    # Upload an attachment by Business Object ID and public ID
    api_response = api_instance.business_object_upload_business_object_attachment_by_id_and_public_id_v1(filename, busobid, publicid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_upload_business_object_attachment_by_id_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Specify the name of the file being uploaded. If no attachment name is provided, the file name is used. | 
 **busobid** | **str**| Specify the Business Object ID. | 
 **publicid** | **str**| Specify the Business Object public ID  to attach the file to. | 
 **offset** | **int**| The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero. | 
 **totalsize** | **int**| The entire file size in bytes. | 
 **body** | **file**|  | 
 **attachmentid** | **str**| Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. | [optional] 
 **displaytext** | **str**| Specify the attachment name, which is the display text for the attachment record. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_object_upload_business_object_attachment_by_id_and_rec_id_v1**
> str business_object_upload_business_object_attachment_by_id_and_rec_id_v1(filename, busobid, busobrecid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)

Upload an attachment by Business Object ID and record ID

Operation to upload an attachment to a Business Object record using a Business Object ID and record ID. The body of the request is the byte array of the file part being uploaded.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
filename = 'filename_example' # str | Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
busobid = 'busobid_example' # str | Specify the Business Object ID.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID to attach the file to.
offset = 56 # int | The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
totalsize = 56 # int | The entire file size in bytes.
body = '/path/to/file' # file | 
attachmentid = 'attachmentid_example' # str | Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. (optional)
displaytext = 'displaytext_example' # str | Specify the attachment name, which is the display text for the attachment record. (optional)

try:
    # Upload an attachment by Business Object ID and record ID
    api_response = api_instance.business_object_upload_business_object_attachment_by_id_and_rec_id_v1(filename, busobid, busobrecid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_upload_business_object_attachment_by_id_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Specify the name of the file being uploaded. If no attachment name is provided, the file name is used. | 
 **busobid** | **str**| Specify the Business Object ID. | 
 **busobrecid** | **str**| Specify the Business Object record ID to attach the file to. | 
 **offset** | **int**| The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero. | 
 **totalsize** | **int**| The entire file size in bytes. | 
 **body** | **file**|  | 
 **attachmentid** | **str**| Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. | [optional] 
 **displaytext** | **str**| Specify the attachment name, which is the display text for the attachment record. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_object_upload_business_object_attachment_by_name_and_public_id_v1**
> str business_object_upload_business_object_attachment_by_name_and_public_id_v1(filename, busobname, publicid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)

Upload an attachment by Business Object name and public ID

Operation to upload an attachment to a Business Object record using a Business Object name and public ID. The body of the request is the byte array of the file part being uploaded.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
filename = 'filename_example' # str | Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
busobname = 'busobname_example' # str | Specify the Business Object name.
publicid = 'publicid_example' # str | Specify the Business Object public ID  to attach the file to.
offset = 56 # int | The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
totalsize = 56 # int | The entire file size in bytes.
body = '/path/to/file' # file | 
attachmentid = 'attachmentid_example' # str | Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. (optional)
displaytext = 'displaytext_example' # str | Specify the attachment name, which is the display text for the attachment record. (optional)

try:
    # Upload an attachment by Business Object name and public ID
    api_response = api_instance.business_object_upload_business_object_attachment_by_name_and_public_id_v1(filename, busobname, publicid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_upload_business_object_attachment_by_name_and_public_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Specify the name of the file being uploaded. If no attachment name is provided, the file name is used. | 
 **busobname** | **str**| Specify the Business Object name. | 
 **publicid** | **str**| Specify the Business Object public ID  to attach the file to. | 
 **offset** | **int**| The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero. | 
 **totalsize** | **int**| The entire file size in bytes. | 
 **body** | **file**|  | 
 **attachmentid** | **str**| Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. | [optional] 
 **displaytext** | **str**| Specify the attachment name, which is the display text for the attachment record. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **business_object_upload_business_object_attachment_by_name_and_rec_id_v1**
> str business_object_upload_business_object_attachment_by_name_and_rec_id_v1(filename, busobname, busobrecid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)

Upload an attachment by Business Object name and record ID

Operation to upload an attachment to a Business Object record using a Business Object name and record ID. The body of the request is the byte array of the file part being uploaded.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.BusinessObjectApi()
filename = 'filename_example' # str | Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
busobname = 'busobname_example' # str | Specify the Business Object name.
busobrecid = 'busobrecid_example' # str | Specify the Business Object record ID to attach the file to.
offset = 56 # int | The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
totalsize = 56 # int | The entire file size in bytes.
body = '/path/to/file' # file | 
attachmentid = 'attachmentid_example' # str | Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. (optional)
displaytext = 'displaytext_example' # str | Specify the attachment name, which is the display text for the attachment record. (optional)

try:
    # Upload an attachment by Business Object name and record ID
    api_response = api_instance.business_object_upload_business_object_attachment_by_name_and_rec_id_v1(filename, busobname, busobrecid, offset, totalsize, body, attachmentid=attachmentid, displaytext=displaytext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessObjectApi->business_object_upload_business_object_attachment_by_name_and_rec_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Specify the name of the file being uploaded. If no attachment name is provided, the file name is used. | 
 **busobname** | **str**| Specify the Business Object name. | 
 **busobrecid** | **str**| Specify the Business Object record ID to attach the file to. | 
 **offset** | **int**| The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero. | 
 **totalsize** | **int**| The entire file size in bytes. | 
 **body** | **file**|  | 
 **attachmentid** | **str**| Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded. | [optional] 
 **displaytext** | **str**| Specify the attachment name, which is the display text for the attachment record. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


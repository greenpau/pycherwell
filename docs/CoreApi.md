# pycherwell.CoreApi

All URIs are relative to *https://demo.cherwellondemand.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_delete_gallery_image_by_stand_in_key_v1**](CoreApi.md#core_delete_gallery_image_by_stand_in_key_v1) | **DELETE** /api/V1/deletegalleryimage/standinkey/{standinkey} | Delete a gallery image
[**core_get_gallery_image_v1**](CoreApi.md#core_get_gallery_image_v1) | **GET** /api/V1/getgalleryimage/name/{name} | Get built-in images
[**core_get_gallery_images_folder_v1**](CoreApi.md#core_get_gallery_images_folder_v1) | **GET** /api/V1/getgalleryimages/scope/{scope}/scopeowner/{scopeowner}/folder/{folder} | Get gallery images by scope, scopeowner, and folder
[**core_get_gallery_images_scope_owner_v1**](CoreApi.md#core_get_gallery_images_scope_owner_v1) | **GET** /api/V1/getgalleryimages/scope/{scope}/scopeowner/{scopeowner} | Get gallery images by scope and scopeowner
[**core_get_gallery_images_scope_v1**](CoreApi.md#core_get_gallery_images_scope_v1) | **GET** /api/V1/getgalleryimages/scope/{scope} | Get gallery images by scope
[**core_get_gallery_images_v1**](CoreApi.md#core_get_gallery_images_v1) | **GET** /api/V1/getgalleryimages | Get all gallery images
[**core_get_stored_value_v1**](CoreApi.md#core_get_stored_value_v1) | **GET** /api/V1/getstoredvalue/standinkey/{standInKey} | Get a  stored value
[**core_get_stored_values_folder_v1**](CoreApi.md#core_get_stored_values_folder_v1) | **GET** /api/V1/storedvalues/scope/{scope}/scopeowner/{scopeowner}/folder/{folder} | Get stored values by folder
[**core_get_stored_values_scope_owner_v1**](CoreApi.md#core_get_stored_values_scope_owner_v1) | **GET** /api/V1/storedvalues/scope/{scope}/scopeowner/{scopeowner} | Get stored values by scope owner
[**core_get_stored_values_scope_v1**](CoreApi.md#core_get_stored_values_scope_v1) | **GET** /api/V1/storedvalues/scope/{scope} | Get stored values by scope
[**core_get_stored_values_v1**](CoreApi.md#core_get_stored_values_v1) | **GET** /api/V1/storedvalues | Gets all the stored values in the system
[**core_get_views_v1**](CoreApi.md#core_get_views_v1) | **GET** /api/V1/getviews | Get a list of the views
[**core_save_gallery_image_v1**](CoreApi.md#core_save_gallery_image_v1) | **POST** /api/V1/savegalleryimage | Create or update a gallery image
[**core_save_stored_value_v1**](CoreApi.md#core_save_stored_value_v1) | **POST** /api/V1/savestoredvalue | Create or update a stored value
[**core_set_culture_v1**](CoreApi.md#core_set_culture_v1) | **PUT** /api/V1/setculture/culturecode/{culturecode} | Set the culture for the current user


# **core_delete_gallery_image_by_stand_in_key_v1**
> core_delete_gallery_image_by_stand_in_key_v1(standinkey)

Delete a gallery image

Endpoint to delete a gallery image.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
standinkey = 'standinkey_example' # str | The StandIn key for the gallery image to delete.

try:
    # Delete a gallery image
    api_instance.core_delete_gallery_image_by_stand_in_key_v1(standinkey)
except ApiException as e:
    print("Exception when calling CoreApi->core_delete_gallery_image_by_stand_in_key_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standinkey** | **str**| The StandIn key for the gallery image to delete. | 

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

# **core_get_gallery_image_v1**
> str core_get_gallery_image_v1(name, width=width, height=height)

Get built-in images

Operation that gets built-in images. If you are requesting an icon (.ico), you can specify width and height.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
name = 'name_example' # str | Image name and folder location in the Image Manager. Parameter must begin with \"[PlugIn]Images;\" and then a period-separated list of folders. Example: \"[PlugIn]Images;Images.Common.Cherwell.ico\".
width = 56 # int | Specify the width (icons only). (optional)
height = 56 # int | Specify the height (icons only). (optional)

try:
    # Get built-in images
    api_response = api_instance.core_get_gallery_image_v1(name, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_gallery_image_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name and folder location in the Image Manager. Parameter must begin with \&quot;[PlugIn]Images;\&quot; and then a period-separated list of folders. Example: \&quot;[PlugIn]Images;Images.Common.Cherwell.ico\&quot;. | 
 **width** | **int**| Specify the width (icons only). | [optional] 
 **height** | **int**| Specify the height (icons only). | [optional] 

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

# **core_get_gallery_images_folder_v1**
> ManagerData core_get_gallery_images_folder_v1(scope, scopeowner, folder, links=links)

Get gallery images by scope, scopeowner, and folder

Get gallery images for the specified scope, scopeowner, and folder.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope to get gallery images for.
scopeowner = 'scopeowner_example' # str | the scopeowner to get gallery images for.
folder = 'folder_example' # str | The folder to get gallery images for.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get gallery images by scope, scopeowner, and folder
    api_response = api_instance.core_get_gallery_images_folder_v1(scope, scopeowner, folder, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_gallery_images_folder_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get gallery images for. | 
 **scopeowner** | **str**| the scopeowner to get gallery images for. | 
 **folder** | **str**| The folder to get gallery images for. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_gallery_images_scope_owner_v1**
> ManagerData core_get_gallery_images_scope_owner_v1(scope, scopeowner, links=links)

Get gallery images by scope and scopeowner

Get all gallery images for the specified scope and scope owner.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope to get gallery images for.
scopeowner = 'scopeowner_example' # str | The scopeowner to get gallery images for.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get gallery images by scope and scopeowner
    api_response = api_instance.core_get_gallery_images_scope_owner_v1(scope, scopeowner, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_gallery_images_scope_owner_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get gallery images for. | 
 **scopeowner** | **str**| The scopeowner to get gallery images for. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_gallery_images_scope_v1**
> ManagerData core_get_gallery_images_scope_v1(scope, links=links)

Get gallery images by scope

Get all gallery images for the specified scope.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope to get the images for.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get gallery images by scope
    api_response = api_instance.core_get_gallery_images_scope_v1(scope, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_gallery_images_scope_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to get the images for. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_gallery_images_v1**
> ManagerData core_get_gallery_images_v1(links=links)

Get all gallery images

Get all the gallery images in the system.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get all gallery images
    api_response = api_instance.core_get_gallery_images_v1(links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_gallery_images_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_stored_value_v1**
> StoredValueResponse core_get_stored_value_v1(stand_in_key)

Get a  stored value

Get a stored value by its StandIn key.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
stand_in_key = 'stand_in_key_example' # str | The StandIn key for the Stored Value you would like to retrieve.

try:
    # Get a  stored value
    api_response = api_instance.core_get_stored_value_v1(stand_in_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_stored_value_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stand_in_key** | **str**| The StandIn key for the Stored Value you would like to retrieve. | 

### Return type

[**StoredValueResponse**](StoredValueResponse.md)

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

# **core_get_stored_values_folder_v1**
> ManagerData core_get_stored_values_folder_v1(scope, scopeowner, folder, links=links)

Get stored values by folder

Get stored values for the specified folder.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope for which to get stored values.
scopeowner = 'scopeowner_example' # str | The scope owner for which to get stored values.
folder = 'folder_example' # str | The folder for which to get stored values.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get stored values by folder
    api_response = api_instance.core_get_stored_values_folder_v1(scope, scopeowner, folder, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_stored_values_folder_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope for which to get stored values. | 
 **scopeowner** | **str**| The scope owner for which to get stored values. | 
 **folder** | **str**| The folder for which to get stored values. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_stored_values_scope_owner_v1**
> ManagerData core_get_stored_values_scope_owner_v1(scope, scopeowner, links=links)

Get stored values by scope owner

Get stored values for the specified scope and scope owner.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope for which to get stored values.
scopeowner = 'scopeowner_example' # str | The scope owner for which to get stored values.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get stored values by scope owner
    api_response = api_instance.core_get_stored_values_scope_owner_v1(scope, scopeowner, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_stored_values_scope_owner_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope for which to get stored values. | 
 **scopeowner** | **str**| The scope owner for which to get stored values. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_stored_values_scope_v1**
> ManagerData core_get_stored_values_scope_v1(scope, links=links)

Get stored values by scope

Get all the stored values for the specified scope.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
scope = 'scope_example' # str | The scope for which to get stored values.
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Get stored values by scope
    api_response = api_instance.core_get_stored_values_scope_v1(scope, links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_stored_values_scope_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope for which to get stored values. | 
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_stored_values_v1**
> ManagerData core_get_stored_values_v1(links=links)

Gets all the stored values in the system

Get all the stored values in the system.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
links = True # bool | Flag to include hyperlinks in results. Default is false. (optional)

try:
    # Gets all the stored values in the system
    api_response = api_instance.core_get_stored_values_v1(links=links)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_stored_values_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **links** | **bool**| Flag to include hyperlinks in results. Default is false. | [optional] 

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

# **core_get_views_v1**
> ViewsResponse core_get_views_v1()

Get a list of the views

Operation to get a list of views that are configured in the system.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()

try:
    # Get a list of the views
    api_response = api_instance.core_get_views_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_get_views_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ViewsResponse**](ViewsResponse.md)

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

# **core_save_gallery_image_v1**
> SaveGalleryImageResponse core_save_gallery_image_v1(save_gallery_image_request)

Create or update a gallery image

Endpoint to Create or update a gallery image. To create a new gallery image leave the StandIn key blank. To update a gallery image provide the StandIn key of the gallery image you want to update.</br>There are three different ImageTypes allowed: Imported, Url, and File. To use the Imported image type, provide the filename in the Name property, with extension, and provide the image data in a Base64 encoded format in the Base64EncodedImageData property. The max file size is 512k.</br>To use the Url image type,  provide the full network share path to the file in the Name property, ie: \"\\\\\\\\\\\\\\\\networkshare\\\\\\somefolder\\\\\\somefile.jpg\". If the file is not accessible to all users it will not visible to all users.</br>To use the File image type, provide the full path to the file in the Name property, ie: \"C:\\\\\\somefolder\\\\\\somfile.jpg\". If the file is not accessible to all users it will not visible to all users.</br>When creating or updating an image, Name and ImageType are always required, and if the image type is \"Imported\", then the Base64EncodedImageData is also required. </br>scope, scopeowner, and folder can all be updated independently.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
save_gallery_image_request = pycherwell.SaveGalleryImageRequest() # SaveGalleryImageRequest | To create a new gallery image leave the StandIn key blank. To update a gallery image provide the StandIn key of the gallery image you want to update.</br>There are three different ImageTypes allowed: Imported, Url, and File. To use the Imported image type, provide the filename in the Name property, with extension, and provide the image data in a Base64 encoded format in the Base64EncodedImageData property. The max file size is 512k.</br>To use the Url image type,  provide the full network share path to the file in the Name property, ie: \"\\\\\\\\\\\\\\\\networkshare\\\\\\somefolder\\\\\\somefile.jpg\". If the file is not accessible to all users it will not visible to all users.</br>To use the File image type, provide the full path to the file in the Name property, ie: \"C:\\\\\\somefolder\\\\\\somfile.jpg\". If the file is not accessible to all users it will not visible to all users.</br>When creating or updating an image, Name and ImageType are always required, and if the image type is \"Imported\", then the Base64EncodedImageData is also required. </br>scope, scopeowner, and folder can all be updated independently.

try:
    # Create or update a gallery image
    api_response = api_instance.core_save_gallery_image_v1(save_gallery_image_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_save_gallery_image_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_gallery_image_request** | [**SaveGalleryImageRequest**](SaveGalleryImageRequest.md)| To create a new gallery image leave the StandIn key blank. To update a gallery image provide the StandIn key of the gallery image you want to update.&lt;/br&gt;There are three different ImageTypes allowed: Imported, Url, and File. To use the Imported image type, provide the filename in the Name property, with extension, and provide the image data in a Base64 encoded format in the Base64EncodedImageData property. The max file size is 512k.&lt;/br&gt;To use the Url image type,  provide the full network share path to the file in the Name property, ie: \&quot;\\\\\\\\\\\\\\\\networkshare\\\\\\somefolder\\\\\\somefile.jpg\&quot;. If the file is not accessible to all users it will not visible to all users.&lt;/br&gt;To use the File image type, provide the full path to the file in the Name property, ie: \&quot;C:\\\\\\somefolder\\\\\\somfile.jpg\&quot;. If the file is not accessible to all users it will not visible to all users.&lt;/br&gt;When creating or updating an image, Name and ImageType are always required, and if the image type is \&quot;Imported\&quot;, then the Base64EncodedImageData is also required. &lt;/br&gt;scope, scopeowner, and folder can all be updated independently. | 

### Return type

[**SaveGalleryImageResponse**](SaveGalleryImageResponse.md)

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

# **core_save_stored_value_v1**
> StoredValueResponse core_save_stored_value_v1(save_stored_value_request)

Create or update a stored value

Operation to create or update a stored value. To update, specify the StandIn key for the stored value to update. To create leave StandIn key blank, and provide a name, a scope, a type, and a value.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
save_stored_value_request = pycherwell.SaveStoredValueRequest() # SaveStoredValueRequest | The stored value to create or update. To update include the StandIn key for the associated stored value. To create, name, scope, type, and value are required.

try:
    # Create or update a stored value
    api_response = api_instance.core_save_stored_value_v1(save_stored_value_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_save_stored_value_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_stored_value_request** | [**SaveStoredValueRequest**](SaveStoredValueRequest.md)| The stored value to create or update. To update include the StandIn key for the associated stored value. To create, name, scope, type, and value are required. | 

### Return type

[**StoredValueResponse**](StoredValueResponse.md)

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

# **core_set_culture_v1**
> str core_set_culture_v1(culturecode)

Set the culture for the current user

Operation to update the current users culture by culture code. This returns a new access token that has the updated information in it.

### Example

```python
from __future__ import print_function
import time
import pycherwell
from pycherwell.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pycherwell.CoreApi()
culturecode = 'culturecode_example' # str | The culture code to set for the current user.

try:
    # Set the culture for the current user
    api_response = api_instance.core_set_culture_v1(culturecode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->core_set_culture_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **culturecode** | **str**| The culture code to set for the current user. | 

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


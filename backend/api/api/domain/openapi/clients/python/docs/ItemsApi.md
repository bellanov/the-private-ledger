# openapi_client.ItemsApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item**](ItemsApi.md#create_item) | **POST** /items | Create an item
[**delete_item**](ItemsApi.md#delete_item) | **DELETE** /items/{itemId} | Delete an item
[**get_item**](ItemsApi.md#get_item) | **GET** /items/{itemId} | Get an item
[**list_items**](ItemsApi.md#list_items) | **GET** /items | List all items


# **create_item**
> Item create_item(item_input)

Create an item

Creates a new item.

### Example


```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.models.item_input import ItemInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    item_input = openapi_client.ItemInput() # ItemInput | 

    try:
        # Create an item
        api_response = api_instance.create_item(item_input)
        print("The response of ItemsApi->create_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->create_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_input** | [**ItemInput**](ItemInput.md)|  | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Item created successfully. |  -  |
**400** | Bad request. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(item_id)

Delete an item

Deletes a single item by its ID.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | The unique identifier of the item.

    try:
        # Delete an item
        api_instance.delete_item(item_id)
    except Exception as e:
        print("Exception when calling ItemsApi->delete_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The unique identifier of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Item deleted successfully. |  -  |
**404** | Item not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Item get_item(item_id)

Get an item

Returns a single item by its ID.

### Example


```python
import openapi_client
from openapi_client.models.item import Item
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    item_id = 'item_id_example' # str | The unique identifier of the item.

    try:
        # Get an item
        api_response = api_instance.get_item(item_id)
        print("The response of ItemsApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The unique identifier of the item. | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested item. |  -  |
**404** | Item not found. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ItemList list_items(limit=limit)

List all items

Returns a paginated list of all items.

### Example


```python
import openapi_client
from openapi_client.models.item_list import ItemList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ItemsApi(api_client)
    limit = 20 # int | Maximum number of items to return. (optional) (default to 20)

    try:
        # List all items
        api_response = api_instance.list_items(limit=limit)
        print("The response of ItemsApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of items to return. | [optional] [default to 20]

### Return type

[**ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of items. |  -  |
**400** | Bad request. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


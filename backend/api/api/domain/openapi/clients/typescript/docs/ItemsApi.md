# .ItemsApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createItem**](ItemsApi.md#createItem) | **POST** /items | Create an item
[**deleteItem**](ItemsApi.md#deleteItem) | **DELETE** /items/{itemId} | Delete an item
[**getItem**](ItemsApi.md#getItem) | **GET** /items/{itemId} | Get an item
[**listItems**](ItemsApi.md#listItems) | **GET** /items | List all items


# **createItem**
> Item createItem(itemInput)

Creates a new item.

### Example


```typescript
import { createConfiguration, ItemsApi } from '';
import type { ItemsApiCreateItemRequest } from '';

const configuration = createConfiguration();
const apiInstance = new ItemsApi(configuration);

const request: ItemsApiCreateItemRequest = {
  
  itemInput: {
    name: "New Item",
    description: "This is a new item.",
  },
};

const data = await apiInstance.createItem(request);
console.log('API called successfully. Returned data:', data);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemInput** | **ItemInput**|  |


### Return type

**Item**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **deleteItem**
> void deleteItem()

Deletes a single item by its ID.

### Example


```typescript
import { createConfiguration, ItemsApi } from '';
import type { ItemsApiDeleteItemRequest } from '';

const configuration = createConfiguration();
const apiInstance = new ItemsApi(configuration);

const request: ItemsApiDeleteItemRequest = {
    // The unique identifier of the item.
  itemId: "itemId_example",
};

const data = await apiInstance.deleteItem(request);
console.log('API called successfully. Returned data:', data);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | [**string**] | The unique identifier of the item. | defaults to undefined


### Return type

**void**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **getItem**
> Item getItem()

Returns a single item by its ID.

### Example


```typescript
import { createConfiguration, ItemsApi } from '';
import type { ItemsApiGetItemRequest } from '';

const configuration = createConfiguration();
const apiInstance = new ItemsApi(configuration);

const request: ItemsApiGetItemRequest = {
    // The unique identifier of the item.
  itemId: "itemId_example",
};

const data = await apiInstance.getItem(request);
console.log('API called successfully. Returned data:', data);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | [**string**] | The unique identifier of the item. | defaults to undefined


### Return type

**Item**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **listItems**
> ItemList listItems()

Returns a paginated list of all items.

### Example


```typescript
import { createConfiguration, ItemsApi } from '';
import type { ItemsApiListItemsRequest } from '';

const configuration = createConfiguration();
const apiInstance = new ItemsApi(configuration);

const request: ItemsApiListItemsRequest = {
    // Maximum number of items to return. (optional)
  limit: 20,
};

const data = await apiInstance.listItems(request);
console.log('API called successfully. Returned data:', data);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**number**] | Maximum number of items to return. | (optional) defaults to 20


### Return type

**ItemList**

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

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)



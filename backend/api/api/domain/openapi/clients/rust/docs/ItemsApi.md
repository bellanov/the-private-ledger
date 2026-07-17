# \ItemsApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item**](ItemsApi.md#create_item) | **POST** /items | Create an item
[**delete_item**](ItemsApi.md#delete_item) | **DELETE** /items/{itemId} | Delete an item
[**get_item**](ItemsApi.md#get_item) | **GET** /items/{itemId} | Get an item
[**list_items**](ItemsApi.md#list_items) | **GET** /items | List all items



## create_item

> models::Item create_item(item_input)
Create an item

Creates a new item.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_input** | [**ItemInput**](ItemInput.md) |  | [required] |

### Return type

[**models::Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_item

> delete_item(item_id)
Delete an item

Deletes a single item by its ID.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_id** | **String** | The unique identifier of the item. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_item

> models::Item get_item(item_id)
Get an item

Returns a single item by its ID.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**item_id** | **String** | The unique identifier of the item. | [required] |

### Return type

[**models::Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## list_items

> models::ItemList list_items(limit)
List all items

Returns a paginated list of all items.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**limit** | Option<**i32**> | Maximum number of items to return. |  |[default to 20]

### Return type

[**models::ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


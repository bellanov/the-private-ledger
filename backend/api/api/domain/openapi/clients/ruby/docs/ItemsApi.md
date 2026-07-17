# OpenapiClient::ItemsApi

All URIs are relative to *https://api.example.com/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_item**](ItemsApi.md#create_item) | **POST** /items | Create an item |
| [**delete_item**](ItemsApi.md#delete_item) | **DELETE** /items/{itemId} | Delete an item |
| [**get_item**](ItemsApi.md#get_item) | **GET** /items/{itemId} | Get an item |
| [**list_items**](ItemsApi.md#list_items) | **GET** /items | List all items |


## create_item

> <Item> create_item(item_input)

Create an item

Creates a new item.

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::ItemsApi.new
item_input = OpenapiClient::ItemInput.new({name: 'New Item'}) # ItemInput | 

begin
  # Create an item
  result = api_instance.create_item(item_input)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->create_item: #{e}"
end
```

#### Using the create_item_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Item>, Integer, Hash)> create_item_with_http_info(item_input)

```ruby
begin
  # Create an item
  data, status_code, headers = api_instance.create_item_with_http_info(item_input)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Item>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->create_item_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **item_input** | [**ItemInput**](ItemInput.md) |  |  |

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_item

> delete_item(item_id)

Delete an item

Deletes a single item by its ID.

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::ItemsApi.new
item_id = 'item_id_example' # String | The unique identifier of the item.

begin
  # Delete an item
  api_instance.delete_item(item_id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->delete_item: #{e}"
end
```

#### Using the delete_item_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_item_with_http_info(item_id)

```ruby
begin
  # Delete an item
  data, status_code, headers = api_instance.delete_item_with_http_info(item_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->delete_item_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **item_id** | **String** | The unique identifier of the item. |  |

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_item

> <Item> get_item(item_id)

Get an item

Returns a single item by its ID.

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::ItemsApi.new
item_id = 'item_id_example' # String | The unique identifier of the item.

begin
  # Get an item
  result = api_instance.get_item(item_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->get_item: #{e}"
end
```

#### Using the get_item_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Item>, Integer, Hash)> get_item_with_http_info(item_id)

```ruby
begin
  # Get an item
  data, status_code, headers = api_instance.get_item_with_http_info(item_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Item>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->get_item_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **item_id** | **String** | The unique identifier of the item. |  |

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_items

> <ItemList> list_items(opts)

List all items

Returns a paginated list of all items.

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::ItemsApi.new
opts = {
  limit: 56 # Integer | Maximum number of items to return.
}

begin
  # List all items
  result = api_instance.list_items(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->list_items: #{e}"
end
```

#### Using the list_items_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItemList>, Integer, Hash)> list_items_with_http_info(opts)

```ruby
begin
  # List all items
  data, status_code, headers = api_instance.list_items_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItemList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ItemsApi->list_items_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **limit** | **Integer** | Maximum number of items to return. | [optional][default to 20] |

### Return type

[**ItemList**](ItemList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


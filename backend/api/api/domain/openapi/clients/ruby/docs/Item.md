# OpenapiClient::Item

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The unique identifier of the item. |  |
| **name** | **String** | The name of the item. |  |
| **description** | **String** | An optional description of the item. | [optional] |
| **created_at** | **Time** | The timestamp when the item was created. | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Item.new(
  id: abc123,
  name: Sample Item,
  description: This is a sample item.,
  created_at: 2024-01-01T00:00Z
)
```


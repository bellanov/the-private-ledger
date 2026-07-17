# OpenapiClient::ItemList

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;Item&gt;**](Item.md) | The list of items. |  |
| **total** | **Integer** | The total number of items available. | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::ItemList.new(
  items: null,
  total: 42
)
```


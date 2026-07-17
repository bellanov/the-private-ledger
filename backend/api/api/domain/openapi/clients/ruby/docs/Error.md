# OpenapiClient::Error

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **Integer** | The error code. |  |
| **message** | **String** | A human-readable error message. |  |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Error.new(
  code: 400,
  message: Bad request.
)
```


# ItemsApi

All URIs are relative to *https://api.example.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createItem**](ItemsApi.md#createItem) | **POST** /items | Create an item |
| [**deleteItem**](ItemsApi.md#deleteItem) | **DELETE** /items/{itemId} | Delete an item |
| [**getItem**](ItemsApi.md#getItem) | **GET** /items/{itemId} | Get an item |
| [**listItems**](ItemsApi.md#listItems) | **GET** /items | List all items |


<a id="createItem"></a>
# **createItem**
> Item createItem(itemInput)

Create an item

Creates a new item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.example.com/v1");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    ItemInput itemInput = new ItemInput(); // ItemInput | 
    try {
      Item result = apiInstance.createItem(itemInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#createItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemInput** | [**ItemInput**](ItemInput.md)|  | |

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
| **201** | Item created successfully. |  -  |
| **400** | Bad request. |  -  |
| **500** | Internal server error. |  -  |

<a id="deleteItem"></a>
# **deleteItem**
> deleteItem(itemId)

Delete an item

Deletes a single item by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.example.com/v1");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String itemId = "itemId_example"; // String | The unique identifier of the item.
    try {
      apiInstance.deleteItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#deleteItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| The unique identifier of the item. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Item deleted successfully. |  -  |
| **404** | Item not found. |  -  |
| **500** | Internal server error. |  -  |

<a id="getItem"></a>
# **getItem**
> Item getItem(itemId)

Get an item

Returns a single item by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.example.com/v1");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String itemId = "itemId_example"; // String | The unique identifier of the item.
    try {
      Item result = apiInstance.getItem(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#getItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| The unique identifier of the item. | |

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
| **200** | The requested item. |  -  |
| **404** | Item not found. |  -  |
| **500** | Internal server error. |  -  |

<a id="listItems"></a>
# **listItems**
> ItemList listItems(limit)

List all items

Returns a paginated list of all items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.example.com/v1");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    Integer limit = 20; // Integer | Maximum number of items to return.
    try {
      ItemList result = apiInstance.listItems(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#listItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Maximum number of items to return. | [optional] [default to 20] |

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
| **200** | A list of items. |  -  |
| **400** | Bad request. |  -  |
| **500** | Internal server error. |  -  |


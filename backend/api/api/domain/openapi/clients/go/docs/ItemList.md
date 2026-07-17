# ItemList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]Item**](Item.md) | The list of items. | 
**Total** | Pointer to **int32** | The total number of items available. | [optional] 

## Methods

### NewItemList

`func NewItemList(items []Item, ) *ItemList`

NewItemList instantiates a new ItemList object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemListWithDefaults

`func NewItemListWithDefaults() *ItemList`

NewItemListWithDefaults instantiates a new ItemList object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *ItemList) GetItems() []Item`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *ItemList) GetItemsOk() (*[]Item, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *ItemList) SetItems(v []Item)`

SetItems sets Items field to given value.


### GetTotal

`func (o *ItemList) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ItemList) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ItemList) SetTotal(v int32)`

SetTotal sets Total field to given value.

### HasTotal

`func (o *ItemList) HasTotal() bool`

HasTotal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



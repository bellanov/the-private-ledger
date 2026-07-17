import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration, ConfigurationOptions } from '../configuration'
import type { Middleware } from '../middleware';

import { Item } from '../models/Item';
import { ItemInput } from '../models/ItemInput';
import { ItemList } from '../models/ItemList';
import { ModelError } from '../models/ModelError';

import { ObservableItemsApi } from "./ObservableAPI";
import { ItemsApiRequestFactory, ItemsApiResponseProcessor} from "../apis/ItemsApi";

export interface ItemsApiCreateItemRequest {
    /**
     * 
     * @type ItemInput
     * @memberof ItemsApicreateItem
     */
    itemInput: ItemInput
}

export interface ItemsApiDeleteItemRequest {
    /**
     * The unique identifier of the item.
     * Defaults to: undefined
     * @type string
     * @memberof ItemsApideleteItem
     */
    itemId: string
}

export interface ItemsApiGetItemRequest {
    /**
     * The unique identifier of the item.
     * Defaults to: undefined
     * @type string
     * @memberof ItemsApigetItem
     */
    itemId: string
}

export interface ItemsApiListItemsRequest {
    /**
     * Maximum number of items to return.
     * Minimum: 1
     * Maximum: 100
     * Defaults to: 20
     * @type number
     * @memberof ItemsApilistItems
     */
    limit?: number
}

export class ObjectItemsApi {
    private api: ObservableItemsApi

    public constructor(configuration: Configuration, requestFactory?: ItemsApiRequestFactory, responseProcessor?: ItemsApiResponseProcessor) {
        this.api = new ObservableItemsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Creates a new item.
     * Create an item
     * @param param the request object
     */
    public createItemWithHttpInfo(param: ItemsApiCreateItemRequest, options?: ConfigurationOptions): Promise<HttpInfo<Item>> {
        return this.api.createItemWithHttpInfo(param.itemInput,  options).toPromise();
    }

    /**
     * Creates a new item.
     * Create an item
     * @param param the request object
     */
    public createItem(param: ItemsApiCreateItemRequest, options?: ConfigurationOptions): Promise<Item> {
        return this.api.createItem(param.itemInput,  options).toPromise();
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param param the request object
     */
    public deleteItemWithHttpInfo(param: ItemsApiDeleteItemRequest, options?: ConfigurationOptions): Promise<HttpInfo<void>> {
        return this.api.deleteItemWithHttpInfo(param.itemId,  options).toPromise();
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param param the request object
     */
    public deleteItem(param: ItemsApiDeleteItemRequest, options?: ConfigurationOptions): Promise<void> {
        return this.api.deleteItem(param.itemId,  options).toPromise();
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param param the request object
     */
    public getItemWithHttpInfo(param: ItemsApiGetItemRequest, options?: ConfigurationOptions): Promise<HttpInfo<Item>> {
        return this.api.getItemWithHttpInfo(param.itemId,  options).toPromise();
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param param the request object
     */
    public getItem(param: ItemsApiGetItemRequest, options?: ConfigurationOptions): Promise<Item> {
        return this.api.getItem(param.itemId,  options).toPromise();
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param param the request object
     */
    public listItemsWithHttpInfo(param: ItemsApiListItemsRequest = {}, options?: ConfigurationOptions): Promise<HttpInfo<ItemList>> {
        return this.api.listItemsWithHttpInfo(param.limit,  options).toPromise();
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param param the request object
     */
    public listItems(param: ItemsApiListItemsRequest = {}, options?: ConfigurationOptions): Promise<ItemList> {
        return this.api.listItems(param.limit,  options).toPromise();
    }

}

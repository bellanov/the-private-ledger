import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration, PromiseConfigurationOptions, wrapOptions } from '../configuration'
import { PromiseMiddleware, Middleware, PromiseMiddlewareWrapper } from '../middleware';

import { Item } from '../models/Item';
import { ItemInput } from '../models/ItemInput';
import { ItemList } from '../models/ItemList';
import { ModelError } from '../models/ModelError';
import { ObservableItemsApi } from './ObservableAPI';

import { ItemsApiRequestFactory, ItemsApiResponseProcessor} from "../apis/ItemsApi";
export class PromiseItemsApi {
    private api: ObservableItemsApi

    public constructor(
        configuration: Configuration,
        requestFactory?: ItemsApiRequestFactory,
        responseProcessor?: ItemsApiResponseProcessor
    ) {
        this.api = new ObservableItemsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Creates a new item.
     * Create an item
     * @param itemInput
     */
    public createItemWithHttpInfo(itemInput: ItemInput, _options?: PromiseConfigurationOptions): Promise<HttpInfo<Item>> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.createItemWithHttpInfo(itemInput, observableOptions);
        return result.toPromise();
    }

    /**
     * Creates a new item.
     * Create an item
     * @param itemInput
     */
    public createItem(itemInput: ItemInput, _options?: PromiseConfigurationOptions): Promise<Item> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.createItem(itemInput, observableOptions);
        return result.toPromise();
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param itemId The unique identifier of the item.
     */
    public deleteItemWithHttpInfo(itemId: string, _options?: PromiseConfigurationOptions): Promise<HttpInfo<void>> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.deleteItemWithHttpInfo(itemId, observableOptions);
        return result.toPromise();
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param itemId The unique identifier of the item.
     */
    public deleteItem(itemId: string, _options?: PromiseConfigurationOptions): Promise<void> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.deleteItem(itemId, observableOptions);
        return result.toPromise();
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param itemId The unique identifier of the item.
     */
    public getItemWithHttpInfo(itemId: string, _options?: PromiseConfigurationOptions): Promise<HttpInfo<Item>> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.getItemWithHttpInfo(itemId, observableOptions);
        return result.toPromise();
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param itemId The unique identifier of the item.
     */
    public getItem(itemId: string, _options?: PromiseConfigurationOptions): Promise<Item> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.getItem(itemId, observableOptions);
        return result.toPromise();
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param [limit] Maximum number of items to return.
     */
    public listItemsWithHttpInfo(limit?: number, _options?: PromiseConfigurationOptions): Promise<HttpInfo<ItemList>> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.listItemsWithHttpInfo(limit, observableOptions);
        return result.toPromise();
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param [limit] Maximum number of items to return.
     */
    public listItems(limit?: number, _options?: PromiseConfigurationOptions): Promise<ItemList> {
        const observableOptions = wrapOptions(_options);
        const result = this.api.listItems(limit, observableOptions);
        return result.toPromise();
    }


}




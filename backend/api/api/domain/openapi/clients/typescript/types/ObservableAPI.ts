import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration, ConfigurationOptions, mergeConfiguration } from '../configuration'
import type { Middleware } from '../middleware';
import { Observable, of, from } from '../rxjsStub';
import {mergeMap, map} from  '../rxjsStub';
import { Item } from '../models/Item';
import { ItemInput } from '../models/ItemInput';
import { ItemList } from '../models/ItemList';
import { ModelError } from '../models/ModelError';

import { ItemsApiRequestFactory, ItemsApiResponseProcessor} from "../apis/ItemsApi";
export class ObservableItemsApi {
    private requestFactory: ItemsApiRequestFactory;
    private responseProcessor: ItemsApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: ItemsApiRequestFactory,
        responseProcessor?: ItemsApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new ItemsApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new ItemsApiResponseProcessor();
    }

    /**
     * Creates a new item.
     * Create an item
     * @param itemInput
     */
    public createItemWithHttpInfo(itemInput: ItemInput, _options?: ConfigurationOptions): Observable<HttpInfo<Item>> {
        const _config = mergeConfiguration(this.configuration, _options);

        const requestContextPromise = this.requestFactory.createItem(itemInput, _config);
        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (const middleware of _config.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => _config.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (const middleware of _config.middleware.reverse()) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.createItemWithHttpInfo(rsp)));
            }));
    }

    /**
     * Creates a new item.
     * Create an item
     * @param itemInput
     */
    public createItem(itemInput: ItemInput, _options?: ConfigurationOptions): Observable<Item> {
        return this.createItemWithHttpInfo(itemInput, _options).pipe(map((apiResponse: HttpInfo<Item>) => apiResponse.data));
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param itemId The unique identifier of the item.
     */
    public deleteItemWithHttpInfo(itemId: string, _options?: ConfigurationOptions): Observable<HttpInfo<void>> {
        const _config = mergeConfiguration(this.configuration, _options);

        const requestContextPromise = this.requestFactory.deleteItem(itemId, _config);
        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (const middleware of _config.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => _config.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (const middleware of _config.middleware.reverse()) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.deleteItemWithHttpInfo(rsp)));
            }));
    }

    /**
     * Deletes a single item by its ID.
     * Delete an item
     * @param itemId The unique identifier of the item.
     */
    public deleteItem(itemId: string, _options?: ConfigurationOptions): Observable<void> {
        return this.deleteItemWithHttpInfo(itemId, _options).pipe(map((apiResponse: HttpInfo<void>) => apiResponse.data));
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param itemId The unique identifier of the item.
     */
    public getItemWithHttpInfo(itemId: string, _options?: ConfigurationOptions): Observable<HttpInfo<Item>> {
        const _config = mergeConfiguration(this.configuration, _options);

        const requestContextPromise = this.requestFactory.getItem(itemId, _config);
        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (const middleware of _config.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => _config.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (const middleware of _config.middleware.reverse()) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getItemWithHttpInfo(rsp)));
            }));
    }

    /**
     * Returns a single item by its ID.
     * Get an item
     * @param itemId The unique identifier of the item.
     */
    public getItem(itemId: string, _options?: ConfigurationOptions): Observable<Item> {
        return this.getItemWithHttpInfo(itemId, _options).pipe(map((apiResponse: HttpInfo<Item>) => apiResponse.data));
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param [limit] Maximum number of items to return.
     */
    public listItemsWithHttpInfo(limit?: number, _options?: ConfigurationOptions): Observable<HttpInfo<ItemList>> {
        const _config = mergeConfiguration(this.configuration, _options);

        const requestContextPromise = this.requestFactory.listItems(limit, _config);
        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (const middleware of _config.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => _config.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (const middleware of _config.middleware.reverse()) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.listItemsWithHttpInfo(rsp)));
            }));
    }

    /**
     * Returns a paginated list of all items.
     * List all items
     * @param [limit] Maximum number of items to return.
     */
    public listItems(limit?: number, _options?: ConfigurationOptions): Observable<ItemList> {
        return this.listItemsWithHttpInfo(limit, _options).pipe(map((apiResponse: HttpInfo<ItemList>) => apiResponse.data));
    }

}

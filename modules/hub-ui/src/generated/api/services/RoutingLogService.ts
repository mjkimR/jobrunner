/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_RoutingLogRead_ } from '../models/PaginatedList_RoutingLogRead_';
import type { RoutingLogCreate } from '../models/RoutingLogCreate';
import type { RoutingLogRead } from '../models/RoutingLogRead';
import type { RoutingLogUpdate } from '../models/RoutingLogUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class RoutingLogService {
    /**
     * Create Routing Log
     * @param requestBody
     * @returns RoutingLogRead Successful Response
     * @throws ApiError
     */
    public static createRoutingLogApiV1RoutingLogsPost(
        requestBody: RoutingLogCreate,
    ): CancelablePromise<RoutingLogRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/routing_logs',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Routing Logs
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_RoutingLogRead_ Successful Response
     * @throws ApiError
     */
    public static getRoutingLogsApiV1RoutingLogsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_RoutingLogRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/routing_logs',
            query: {
                'offset': offset,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Routing Log
     * @param routingLogId
     * @returns RoutingLogRead Successful Response
     * @throws ApiError
     */
    public static getRoutingLogApiV1RoutingLogsRoutingLogIdGet(
        routingLogId: string,
    ): CancelablePromise<RoutingLogRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/routing_logs/{routing_log_id}',
            path: {
                'routing_log_id': routingLogId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Routing Log
     * @param routingLogId
     * @param requestBody
     * @returns RoutingLogRead Successful Response
     * @throws ApiError
     */
    public static updateRoutingLogApiV1RoutingLogsRoutingLogIdPut(
        routingLogId: string,
        requestBody: RoutingLogUpdate,
    ): CancelablePromise<RoutingLogRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/routing_logs/{routing_log_id}',
            path: {
                'routing_log_id': routingLogId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Routing Log
     * @param routingLogId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteRoutingLogApiV1RoutingLogsRoutingLogIdDelete(
        routingLogId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/routing_logs/{routing_log_id}',
            path: {
                'routing_log_id': routingLogId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

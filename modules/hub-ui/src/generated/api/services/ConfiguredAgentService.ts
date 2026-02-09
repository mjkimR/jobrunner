/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ConfiguredAgentCreate } from '../models/ConfiguredAgentCreate';
import type { ConfiguredAgentRead } from '../models/ConfiguredAgentRead';
import type { ConfiguredAgentUpdate } from '../models/ConfiguredAgentUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_ConfiguredAgentRead_ } from '../models/PaginatedList_ConfiguredAgentRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ConfiguredAgentService {
    /**
     * Create Configured Agent
     * @param requestBody
     * @returns ConfiguredAgentRead Successful Response
     * @throws ApiError
     */
    public static createConfiguredAgentApiV1ConfiguredAgentsPost(
        requestBody: ConfiguredAgentCreate,
    ): CancelablePromise<ConfiguredAgentRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/configured_agents',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Configured Agents
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_ConfiguredAgentRead_ Successful Response
     * @throws ApiError
     */
    public static getConfiguredAgentsApiV1ConfiguredAgentsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_ConfiguredAgentRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/configured_agents',
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
     * Get Configured Agent
     * @param configuredAgentId
     * @returns ConfiguredAgentRead Successful Response
     * @throws ApiError
     */
    public static getConfiguredAgentApiV1ConfiguredAgentsConfiguredAgentIdGet(
        configuredAgentId: string,
    ): CancelablePromise<ConfiguredAgentRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/configured_agents/{configured_agent_id}',
            path: {
                'configured_agent_id': configuredAgentId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Configured Agent
     * @param configuredAgentId
     * @param requestBody
     * @returns ConfiguredAgentRead Successful Response
     * @throws ApiError
     */
    public static updateConfiguredAgentApiV1ConfiguredAgentsConfiguredAgentIdPut(
        configuredAgentId: string,
        requestBody: ConfiguredAgentUpdate,
    ): CancelablePromise<ConfiguredAgentRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/configured_agents/{configured_agent_id}',
            path: {
                'configured_agent_id': configuredAgentId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Configured Agent
     * @param configuredAgentId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteConfiguredAgentApiV1ConfiguredAgentsConfiguredAgentIdDelete(
        configuredAgentId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/configured_agents/{configured_agent_id}',
            path: {
                'configured_agent_id': configuredAgentId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AIModelGroupCreate } from '../models/AIModelGroupCreate';
import type { AIModelGroupRead } from '../models/AIModelGroupRead';
import type { AIModelGroupUpdate } from '../models/AIModelGroupUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AIModelGroupRead_ } from '../models/PaginatedList_AIModelGroupRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AiModelGroupService {
    /**
     * Create Ai Model Group
     * @param requestBody
     * @returns AIModelGroupRead Successful Response
     * @throws ApiError
     */
    public static createAiModelGroupApiV1AiModelGroupsPost(
        requestBody: AIModelGroupCreate,
    ): CancelablePromise<AIModelGroupRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/ai_model_groups',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Ai Model Groups
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AIModelGroupRead_ Successful Response
     * @throws ApiError
     */
    public static getAiModelGroupsApiV1AiModelGroupsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AIModelGroupRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_groups',
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
     * Get Ai Model Group
     * @param aiModelGroupId
     * @returns AIModelGroupRead Successful Response
     * @throws ApiError
     */
    public static getAiModelGroupApiV1AiModelGroupsAiModelGroupIdGet(
        aiModelGroupId: string,
    ): CancelablePromise<AIModelGroupRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_groups/{ai_model_group_id}',
            path: {
                'ai_model_group_id': aiModelGroupId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Ai Model Group
     * @param aiModelGroupId
     * @param requestBody
     * @returns AIModelGroupRead Successful Response
     * @throws ApiError
     */
    public static updateAiModelGroupApiV1AiModelGroupsAiModelGroupIdPut(
        aiModelGroupId: string,
        requestBody: AIModelGroupUpdate,
    ): CancelablePromise<AIModelGroupRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/ai_model_groups/{ai_model_group_id}',
            path: {
                'ai_model_group_id': aiModelGroupId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Ai Model Group
     * @param aiModelGroupId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAiModelGroupApiV1AiModelGroupsAiModelGroupIdDelete(
        aiModelGroupId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/ai_model_groups/{ai_model_group_id}',
            path: {
                'ai_model_group_id': aiModelGroupId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AIModelAliasCreate } from '../models/AIModelAliasCreate';
import type { AIModelAliasRead } from '../models/AIModelAliasRead';
import type { AIModelAliasUpdate } from '../models/AIModelAliasUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AIModelAliasRead_ } from '../models/PaginatedList_AIModelAliasRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AiModelAliasService {
    /**
     * Create Ai Model Alias
     * @param requestBody
     * @returns AIModelAliasRead Successful Response
     * @throws ApiError
     */
    public static createAiModelAliasApiV1AiModelAliasesPost(
        requestBody: AIModelAliasCreate,
    ): CancelablePromise<AIModelAliasRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/ai_model_aliases',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Ai Model Aliases
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AIModelAliasRead_ Successful Response
     * @throws ApiError
     */
    public static getAiModelAliasesApiV1AiModelAliasesGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AIModelAliasRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_aliases',
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
     * Get Ai Model Alias
     * @param aiModelAliasId
     * @returns AIModelAliasRead Successful Response
     * @throws ApiError
     */
    public static getAiModelAliasApiV1AiModelAliasesAiModelAliasIdGet(
        aiModelAliasId: string,
    ): CancelablePromise<AIModelAliasRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_aliases/{ai_model_alias_id}',
            path: {
                'ai_model_alias_id': aiModelAliasId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Ai Model Alias
     * @param aiModelAliasId
     * @param requestBody
     * @returns AIModelAliasRead Successful Response
     * @throws ApiError
     */
    public static updateAiModelAliasApiV1AiModelAliasesAiModelAliasIdPut(
        aiModelAliasId: string,
        requestBody: AIModelAliasUpdate,
    ): CancelablePromise<AIModelAliasRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/ai_model_aliases/{ai_model_alias_id}',
            path: {
                'ai_model_alias_id': aiModelAliasId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Ai Model Alias
     * @param aiModelAliasId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAiModelAliasApiV1AiModelAliasesAiModelAliasIdDelete(
        aiModelAliasId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/ai_model_aliases/{ai_model_alias_id}',
            path: {
                'ai_model_alias_id': aiModelAliasId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

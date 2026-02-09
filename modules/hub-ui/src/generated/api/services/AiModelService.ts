/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AIModelCreate } from '../models/AIModelCreate';
import type { AIModelRead } from '../models/AIModelRead';
import type { AIModelUpdate } from '../models/AIModelUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AIModelRead_ } from '../models/PaginatedList_AIModelRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AiModelService {
    /**
     * Create Ai Model
     * @param requestBody
     * @returns AIModelRead Successful Response
     * @throws ApiError
     */
    public static createAiModelApiV1AiModelsPost(
        requestBody: AIModelCreate,
    ): CancelablePromise<AIModelRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/ai_models',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Ai Models
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AIModelRead_ Successful Response
     * @throws ApiError
     */
    public static getAiModelsApiV1AiModelsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AIModelRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_models',
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
     * Get Ai Model
     * @param aiModelId
     * @returns AIModelRead Successful Response
     * @throws ApiError
     */
    public static getAiModelApiV1AiModelsAiModelIdGet(
        aiModelId: string,
    ): CancelablePromise<AIModelRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_models/{ai_model_id}',
            path: {
                'ai_model_id': aiModelId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Ai Model
     * @param aiModelId
     * @param requestBody
     * @returns AIModelRead Successful Response
     * @throws ApiError
     */
    public static updateAiModelApiV1AiModelsAiModelIdPut(
        aiModelId: string,
        requestBody: AIModelUpdate,
    ): CancelablePromise<AIModelRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/ai_models/{ai_model_id}',
            path: {
                'ai_model_id': aiModelId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Ai Model
     * @param aiModelId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAiModelApiV1AiModelsAiModelIdDelete(
        aiModelId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/ai_models/{ai_model_id}',
            path: {
                'ai_model_id': aiModelId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

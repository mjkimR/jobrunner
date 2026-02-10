/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AIModelCatalogCreate } from '../models/AIModelCatalogCreate';
import type { AIModelCatalogRead } from '../models/AIModelCatalogRead';
import type { Body_upload_yaml_ai_model_catalog_api_v1_ai_model_catalogs_upload_yaml_post } from '../models/Body_upload_yaml_ai_model_catalog_api_v1_ai_model_catalogs_upload_yaml_post';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AIModelCatalogRead_ } from '../models/PaginatedList_AIModelCatalogRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AiModelCatalogService {
    /**
     * Create Ai Model Catalog
     * @param requestBody
     * @returns AIModelCatalogRead Successful Response
     * @throws ApiError
     */
    public static createAiModelCatalogApiV1AiModelCatalogsPost(
        requestBody: AIModelCatalogCreate,
    ): CancelablePromise<AIModelCatalogRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/ai_model_catalogs',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Ai Model Catalogs
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AIModelCatalogRead_ Successful Response
     * @throws ApiError
     */
    public static getAiModelCatalogsApiV1AiModelCatalogsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AIModelCatalogRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_catalogs',
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
     * Upload Yaml Ai Model Catalog
     * @param formData
     * @returns AIModelCatalogRead Successful Response
     * @throws ApiError
     */
    public static uploadYamlAiModelCatalogApiV1AiModelCatalogsUploadYamlPost(
        formData: Body_upload_yaml_ai_model_catalog_api_v1_ai_model_catalogs_upload_yaml_post,
    ): CancelablePromise<AIModelCatalogRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/ai_model_catalogs/upload_yaml',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Download Yaml Ai Model Catalog
     * @param aiModelCatalogId
     * @returns any Successful Response
     * @throws ApiError
     */
    public static downloadYamlAiModelCatalogApiV1AiModelCatalogsDownloadYamlGet(
        aiModelCatalogId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_catalogs/download_yaml',
            query: {
                'ai_model_catalog_id': aiModelCatalogId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Download Yaml Latest Ai Model Catalog
     * @returns any Successful Response
     * @throws ApiError
     */
    public static downloadYamlLatestAiModelCatalogApiV1AiModelCatalogsDownloadYamlLatestGet(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_catalogs/download_yaml/latest',
        });
    }
    /**
     * Get Latest Ai Model Catalog
     * @returns AIModelCatalogRead Successful Response
     * @throws ApiError
     */
    public static getLatestAiModelCatalogApiV1AiModelCatalogsLatestGet(): CancelablePromise<AIModelCatalogRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_catalogs/latest',
        });
    }
    /**
     * Get Ai Model Catalog
     * @param aiModelCatalogId
     * @returns AIModelCatalogRead Successful Response
     * @throws ApiError
     */
    public static getAiModelCatalogApiV1AiModelCatalogsAiModelCatalogIdGet(
        aiModelCatalogId: string,
    ): CancelablePromise<AIModelCatalogRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/ai_model_catalogs/{ai_model_catalog_id}',
            path: {
                'ai_model_catalog_id': aiModelCatalogId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Ai Model Catalog
     * @param aiModelCatalogId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAiModelCatalogApiV1AiModelCatalogsAiModelCatalogIdDelete(
        aiModelCatalogId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/ai_model_catalogs/{ai_model_catalog_id}',
            path: {
                'ai_model_catalog_id': aiModelCatalogId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

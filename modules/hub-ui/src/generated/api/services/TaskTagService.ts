/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_TaskTagRead_ } from '../models/PaginatedList_TaskTagRead_';
import type { TaskTagCreate } from '../models/TaskTagCreate';
import type { TaskTagRead } from '../models/TaskTagRead';
import type { TaskTagUpdate } from '../models/TaskTagUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TaskTagService {
    /**
     * Create Task Tag
     * @param requestBody
     * @returns TaskTagRead Successful Response
     * @throws ApiError
     */
    public static createTaskTagApiV1TaskTagsPost(
        requestBody: TaskTagCreate,
    ): CancelablePromise<TaskTagRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/task_tags',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Task Tags
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_TaskTagRead_ Successful Response
     * @throws ApiError
     */
    public static getTaskTagsApiV1TaskTagsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_TaskTagRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/task_tags',
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
     * Get Task Tag
     * @param taskTagId
     * @returns TaskTagRead Successful Response
     * @throws ApiError
     */
    public static getTaskTagApiV1TaskTagsTaskTagIdGet(
        taskTagId: string,
    ): CancelablePromise<TaskTagRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/task_tags/{task_tag_id}',
            path: {
                'task_tag_id': taskTagId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Task Tag
     * @param taskTagId
     * @param requestBody
     * @returns TaskTagRead Successful Response
     * @throws ApiError
     */
    public static updateTaskTagApiV1TaskTagsTaskTagIdPut(
        taskTagId: string,
        requestBody: TaskTagUpdate,
    ): CancelablePromise<TaskTagRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/task_tags/{task_tag_id}',
            path: {
                'task_tag_id': taskTagId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Task Tag
     * @param taskTagId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteTaskTagApiV1TaskTagsTaskTagIdDelete(
        taskTagId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/task_tags/{task_tag_id}',
            path: {
                'task_tag_id': taskTagId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

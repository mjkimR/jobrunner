/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_TaskHistoryRead_ } from '../models/PaginatedList_TaskHistoryRead_';
import type { TaskHistoryCreate } from '../models/TaskHistoryCreate';
import type { TaskHistoryRead } from '../models/TaskHistoryRead';
import type { TaskHistoryUpdate } from '../models/TaskHistoryUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TaskHistorieService {
    /**
     * Create Task History
     * @param requestBody
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static createTaskHistoryApiV1TaskHistoriesPost(
        requestBody: TaskHistoryCreate,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/task_histories',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Task Histories
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_TaskHistoryRead_ Successful Response
     * @throws ApiError
     */
    public static getTaskHistoriesApiV1TaskHistoriesGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_TaskHistoryRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/task_histories',
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
     * Get Task History
     * @param taskHistoryId
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static getTaskHistoryApiV1TaskHistoriesTaskHistoryIdGet(
        taskHistoryId: string,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/task_histories/{task_history_id}',
            path: {
                'task_history_id': taskHistoryId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Task History
     * @param taskHistoryId
     * @param requestBody
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static updateTaskHistoryApiV1TaskHistoriesTaskHistoryIdPut(
        taskHistoryId: string,
        requestBody: TaskHistoryUpdate,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/task_histories/{task_history_id}',
            path: {
                'task_history_id': taskHistoryId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Task History
     * @param taskHistoryId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteTaskHistoryApiV1TaskHistoriesTaskHistoryIdDelete(
        taskHistoryId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/task_histories/{task_history_id}',
            path: {
                'task_history_id': taskHistoryId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

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
export class TaskHistoriesService {
    /**
     * Create Task History
     * @param workspaceId
     * @param requestBody
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static createTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesPost(
        workspaceId: string,
        requestBody: TaskHistoryCreate,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/workspace/{workspace_id}/task_histories',
            path: {
                'workspace_id': workspaceId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Task Histories
     * @param workspaceId
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_TaskHistoryRead_ Successful Response
     * @throws ApiError
     */
    public static getTaskHistoriesApiV1WorkspaceWorkspaceIdTaskHistoriesGet(
        workspaceId: string,
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_TaskHistoryRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspace/{workspace_id}/task_histories',
            path: {
                'workspace_id': workspaceId,
            },
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
     * @param workspaceId
     * @param taskHistoryId
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static getTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesTaskHistoryIdGet(
        workspaceId: string,
        taskHistoryId: string,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspace/{workspace_id}/task_histories/{task_history_id}',
            path: {
                'workspace_id': workspaceId,
                'task_history_id': taskHistoryId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Task History
     * @param workspaceId
     * @param taskHistoryId
     * @param requestBody
     * @returns TaskHistoryRead Successful Response
     * @throws ApiError
     */
    public static updateTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesTaskHistoryIdPut(
        workspaceId: string,
        taskHistoryId: string,
        requestBody: TaskHistoryUpdate,
    ): CancelablePromise<TaskHistoryRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/workspace/{workspace_id}/task_histories/{task_history_id}',
            path: {
                'workspace_id': workspaceId,
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
     * @param workspaceId
     * @param taskHistoryId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesTaskHistoryIdDelete(
        workspaceId: string,
        taskHistoryId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/workspace/{workspace_id}/task_histories/{task_history_id}',
            path: {
                'workspace_id': workspaceId,
                'task_history_id': taskHistoryId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

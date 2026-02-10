/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_TaskRead_ } from '../models/PaginatedList_TaskRead_';
import type { TaskCreate } from '../models/TaskCreate';
import type { TaskRead } from '../models/TaskRead';
import type { TaskUpdate } from '../models/TaskUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class TaskService {
    /**
     * Create Task
     * @param workspaceId
     * @param requestBody
     * @returns TaskRead Successful Response
     * @throws ApiError
     */
    public static createTaskApiV1WorkspaceWorkspaceIdTasksPost(
        workspaceId: string,
        requestBody: TaskCreate,
    ): CancelablePromise<TaskRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/workspace/{workspace_id}/tasks',
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
     * Get Tasks
     * @param workspaceId
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_TaskRead_ Successful Response
     * @throws ApiError
     */
    public static getTasksApiV1WorkspaceWorkspaceIdTasksGet(
        workspaceId: string,
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_TaskRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspace/{workspace_id}/tasks',
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
     * Get Task
     * @param workspaceId
     * @param taskId
     * @returns TaskRead Successful Response
     * @throws ApiError
     */
    public static getTaskApiV1WorkspaceWorkspaceIdTasksTaskIdGet(
        workspaceId: string,
        taskId: string,
    ): CancelablePromise<TaskRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspace/{workspace_id}/tasks/{task_id}',
            path: {
                'workspace_id': workspaceId,
                'task_id': taskId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Task
     * @param workspaceId
     * @param taskId
     * @param requestBody
     * @returns TaskRead Successful Response
     * @throws ApiError
     */
    public static updateTaskApiV1WorkspaceWorkspaceIdTasksTaskIdPut(
        workspaceId: string,
        taskId: string,
        requestBody: TaskUpdate,
    ): CancelablePromise<TaskRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/workspace/{workspace_id}/tasks/{task_id}',
            path: {
                'workspace_id': workspaceId,
                'task_id': taskId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Task
     * @param workspaceId
     * @param taskId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteTaskApiV1WorkspaceWorkspaceIdTasksTaskIdDelete(
        workspaceId: string,
        taskId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/workspace/{workspace_id}/tasks/{task_id}',
            path: {
                'workspace_id': workspaceId,
                'task_id': taskId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

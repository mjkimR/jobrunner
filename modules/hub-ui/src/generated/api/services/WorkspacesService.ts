/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_WorkspaceRead_ } from '../models/PaginatedList_WorkspaceRead_';
import type { WorkspaceCreate } from '../models/WorkspaceCreate';
import type { WorkspaceRead } from '../models/WorkspaceRead';
import type { WorkspaceUpdate } from '../models/WorkspaceUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class WorkspacesService {
    /**
     * Create Workspace
     * @param requestBody
     * @returns WorkspaceRead Successful Response
     * @throws ApiError
     */
    public static createWorkspaceApiV1WorkspacesPost(
        requestBody: WorkspaceCreate,
    ): CancelablePromise<WorkspaceRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/workspaces',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Workspaces
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_WorkspaceRead_ Successful Response
     * @throws ApiError
     */
    public static getWorkspacesApiV1WorkspacesGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_WorkspaceRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspaces',
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
     * Get Workspace
     * @param workspaceId
     * @returns WorkspaceRead Successful Response
     * @throws ApiError
     */
    public static getWorkspaceApiV1WorkspacesWorkspaceIdGet(
        workspaceId: string,
    ): CancelablePromise<WorkspaceRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspaces/{workspace_id}',
            path: {
                'workspace_id': workspaceId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Workspace
     * @param workspaceId
     * @param requestBody
     * @returns WorkspaceRead Successful Response
     * @throws ApiError
     */
    public static updateWorkspaceApiV1WorkspacesWorkspaceIdPut(
        workspaceId: string,
        requestBody: WorkspaceUpdate,
    ): CancelablePromise<WorkspaceRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/workspaces/{workspace_id}',
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
     * Delete Workspace
     * @param workspaceId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteWorkspaceApiV1WorkspacesWorkspaceIdDelete(
        workspaceId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/workspaces/{workspace_id}',
            path: {
                'workspace_id': workspaceId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

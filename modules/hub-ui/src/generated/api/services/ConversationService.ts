/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ConversationCreate } from '../models/ConversationCreate';
import type { ConversationRead } from '../models/ConversationRead';
import type { ConversationUpdate } from '../models/ConversationUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_ConversationRead_ } from '../models/PaginatedList_ConversationRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ConversationService {
    /**
     * Create Conversation
     * @param workspaceId
     * @param requestBody
     * @returns ConversationRead Successful Response
     * @throws ApiError
     */
    public static createConversationApiV1WorkspacesWorkspaceIdConversationsPost(
        workspaceId: string,
        requestBody: ConversationCreate,
    ): CancelablePromise<ConversationRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/workspaces/{workspace_id}/conversations',
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
     * Get Conversations
     * @param workspaceId
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_ConversationRead_ Successful Response
     * @throws ApiError
     */
    public static getConversationsApiV1WorkspacesWorkspaceIdConversationsGet(
        workspaceId: string,
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_ConversationRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspaces/{workspace_id}/conversations',
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
     * Get Conversation
     * @param workspaceId
     * @param conversationId
     * @returns ConversationRead Successful Response
     * @throws ApiError
     */
    public static getConversationApiV1WorkspacesWorkspaceIdConversationsConversationIdGet(
        workspaceId: string,
        conversationId: string,
    ): CancelablePromise<ConversationRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/workspaces/{workspace_id}/conversations/{conversation_id}',
            path: {
                'workspace_id': workspaceId,
                'conversation_id': conversationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Conversation
     * @param workspaceId
     * @param conversationId
     * @param requestBody
     * @returns ConversationRead Successful Response
     * @throws ApiError
     */
    public static updateConversationApiV1WorkspacesWorkspaceIdConversationsConversationIdPut(
        workspaceId: string,
        conversationId: string,
        requestBody: ConversationUpdate,
    ): CancelablePromise<ConversationRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/workspaces/{workspace_id}/conversations/{conversation_id}',
            path: {
                'workspace_id': workspaceId,
                'conversation_id': conversationId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Conversation
     * @param workspaceId
     * @param conversationId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteConversationApiV1WorkspacesWorkspaceIdConversationsConversationIdDelete(
        workspaceId: string,
        conversationId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/workspaces/{workspace_id}/conversations/{conversation_id}',
            path: {
                'workspace_id': workspaceId,
                'conversation_id': conversationId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

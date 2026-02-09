/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_UserMessageRead_ } from '../models/PaginatedList_UserMessageRead_';
import type { UserMessageCreate } from '../models/UserMessageCreate';
import type { UserMessageRead } from '../models/UserMessageRead';
import type { UserMessageUpdate } from '../models/UserMessageUpdate';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class UserMessageService {
    /**
     * Create User Message
     * @param requestBody
     * @returns UserMessageRead Successful Response
     * @throws ApiError
     */
    public static createUserMessageApiV1UserMessagesPost(
        requestBody: UserMessageCreate,
    ): CancelablePromise<UserMessageRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/user_messages',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get User Messages
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_UserMessageRead_ Successful Response
     * @throws ApiError
     */
    public static getUserMessagesApiV1UserMessagesGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_UserMessageRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/user_messages',
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
     * Get User Message
     * @param userMessageId
     * @returns UserMessageRead Successful Response
     * @throws ApiError
     */
    public static getUserMessageApiV1UserMessagesUserMessageIdGet(
        userMessageId: string,
    ): CancelablePromise<UserMessageRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/user_messages/{user_message_id}',
            path: {
                'user_message_id': userMessageId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update User Message
     * @param userMessageId
     * @param requestBody
     * @returns UserMessageRead Successful Response
     * @throws ApiError
     */
    public static updateUserMessageApiV1UserMessagesUserMessageIdPut(
        userMessageId: string,
        requestBody: UserMessageUpdate,
    ): CancelablePromise<UserMessageRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/user_messages/{user_message_id}',
            path: {
                'user_message_id': userMessageId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete User Message
     * @param userMessageId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteUserMessageApiV1UserMessagesUserMessageIdDelete(
        userMessageId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/user_messages/{user_message_id}',
            path: {
                'user_message_id': userMessageId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

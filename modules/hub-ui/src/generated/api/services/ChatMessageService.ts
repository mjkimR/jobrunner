/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ChatMessageCreate } from '../models/ChatMessageCreate';
import type { ChatMessageRead } from '../models/ChatMessageRead';
import type { ChatMessageUpdate } from '../models/ChatMessageUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_ChatMessageRead_ } from '../models/PaginatedList_ChatMessageRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ChatMessageService {
    /**
     * Create Chat Message
     * @param requestBody
     * @returns ChatMessageRead Successful Response
     * @throws ApiError
     */
    public static createChatMessageApiV1ChatMessagesPost(
        requestBody: ChatMessageCreate,
    ): CancelablePromise<ChatMessageRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/chat_messages',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Chat Messages
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_ChatMessageRead_ Successful Response
     * @throws ApiError
     */
    public static getChatMessagesApiV1ChatMessagesGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_ChatMessageRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/chat_messages',
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
     * Get Chat Message
     * @param chatMessageId
     * @returns ChatMessageRead Successful Response
     * @throws ApiError
     */
    public static getChatMessageApiV1ChatMessagesChatMessageIdGet(
        chatMessageId: string,
    ): CancelablePromise<ChatMessageRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/chat_messages/{chat_message_id}',
            path: {
                'chat_message_id': chatMessageId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Chat Message
     * @param chatMessageId
     * @param requestBody
     * @returns ChatMessageRead Successful Response
     * @throws ApiError
     */
    public static updateChatMessageApiV1ChatMessagesChatMessageIdPut(
        chatMessageId: string,
        requestBody: ChatMessageUpdate,
    ): CancelablePromise<ChatMessageRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/chat_messages/{chat_message_id}',
            path: {
                'chat_message_id': chatMessageId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Chat Message
     * @param chatMessageId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteChatMessageApiV1ChatMessagesChatMessageIdDelete(
        chatMessageId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/chat_messages/{chat_message_id}',
            path: {
                'chat_message_id': chatMessageId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

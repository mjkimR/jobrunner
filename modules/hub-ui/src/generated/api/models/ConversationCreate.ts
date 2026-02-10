/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new Conversation.
 */
export type ConversationCreate = {
    /**
     * Workspace ID
     */
    workspace_id: string;
    /**
     * Conversation Title
     */
    title?: (string | null);
    /**
     * Chat Channel
     */
    channel?: string;
    /**
     * Conversation Status
     */
    status?: string;
    /**
     * Conversation Context
     */
    context?: Record<string, any>;
};


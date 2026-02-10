/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading Conversation data.
 */
export type ConversationRead = {
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
    created_at: string;
    updated_at: string;
    id: string;
    /**
     * Started At
     */
    started_at: string;
    /**
     * Ended At
     */
    ended_at?: (string | null);
};


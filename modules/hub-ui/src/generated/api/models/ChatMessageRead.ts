/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading Chat Message data.
 */
export type ChatMessageRead = {
    /**
     * Conversation ID
     */
    conversation_id: string;
    /**
     * Role (user, assistant, system)
     */
    role: string;
    /**
     * Message Content
     */
    content: string;
    /**
     * Content Type
     */
    content_type?: string;
    /**
     * Metadata
     */
    metadata?: Record<string, any>;
    /**
     * Agent Execution ID (if applicable)
     */
    agent_execution_id?: (string | null);
    created_at: string;
    updated_at: string;
    id: string;
};


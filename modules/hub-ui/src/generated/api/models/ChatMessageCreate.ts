/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new Chat Message.
 */
export type ChatMessageCreate = {
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
};


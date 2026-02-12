/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new ConfiguredAgent.
 */
export type ConfiguredAgentCreate = {
    /**
     * Agent Name
     */
    name: string;
    /**
     * Agent Description
     */
    description?: (string | null);
    /**
     * Model Name (from Catalog)
     */
    model_name: string;
    /**
     * System Prompt
     */
    system_prompt?: (string | null);
    /**
     * Configuration
     */
    config?: Record<string, (string | number | boolean | Record<string, any> | null)>;
    /**
     * Active Status
     */
    is_active?: boolean;
    /**
     * List of Skill IDs
     */
    skill_ids?: Array<string>;
    /**
     * List of MCP IDs
     */
    mcp_ids?: Array<string>;
};


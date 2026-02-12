/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for updating ConfiguredAgent.
 */
export type ConfiguredAgentUpdate = {
    /**
     * Agent Name
     */
    name?: (string | null);
    /**
     * Agent Description
     */
    description?: (string | null);
    /**
     * Model Name
     */
    model_name?: (string | null);
    /**
     * System Prompt
     */
    system_prompt?: (string | null);
    /**
     * Configuration
     */
    config?: (Record<string, (string | number | boolean | Record<string, any> | null)> | null);
    /**
     * Active Status
     */
    is_active?: (boolean | null);
    /**
     * List of Skill IDs
     */
    skill_ids?: (Array<string> | null);
    /**
     * List of MCP IDs
     */
    mcp_ids?: (Array<string> | null);
};


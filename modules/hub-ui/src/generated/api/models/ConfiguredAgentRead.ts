/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentMCPRead } from './AgentMCPRead';
import type { AgentSkillRead } from './AgentSkillRead';
/**
 * Schema for reading ConfiguredAgent data.
 */
export type ConfiguredAgentRead = {
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
    config?: Record<string, any>;
    /**
     * Active Status
     */
    is_active?: boolean;
    created_at: string;
    updated_at: string;
    id: string;
    /**
     * Linked Skills
     */
    skills?: Array<AgentSkillRead>;
    /**
     * Linked MCPs
     */
    mcps?: Array<AgentMCPRead>;
};


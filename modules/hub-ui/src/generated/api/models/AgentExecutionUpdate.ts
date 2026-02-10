/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentExecutionStatus } from './AgentExecutionStatus';
/**
 * Schema for updating AgentExecution.
 */
export type AgentExecutionUpdate = {
    /**
     * Execution status
     */
    status?: (AgentExecutionStatus | null);
    /**
     * Output data
     */
    output_data?: (Record<string, any> | null);
    /**
     * Error message
     */
    error_message?: (string | null);
    /**
     * Start timestamp
     */
    started_at?: (string | null);
    /**
     * Completion timestamp
     */
    completed_at?: (string | null);
    /**
     * Token usage data
     */
    token_usage?: (Record<string, any> | null);
    /**
     * Dagster Run ID
     */
    dagster_run_id?: (string | null);
};


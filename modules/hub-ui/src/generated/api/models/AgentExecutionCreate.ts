/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentExecutionStatus } from './AgentExecutionStatus';
import type { AgentExecutionType } from './AgentExecutionType';
import type { AgentType } from './AgentType';
/**
 * Schema for creating a new AgentExecution.
 */
export type AgentExecutionCreate = {
    /**
     * Type of agent (configured or graph)
     */
    agent_type: AgentType;
    /**
     * Configured Agent ID
     */
    configured_agent_id?: (string | null);
    /**
     * Graph Agent Name
     */
    graph_agent_name?: (string | null);
    /**
     * Associated Task ID
     */
    task_id?: (string | null);
    /**
     * Type of execution
     */
    execution_type: AgentExecutionType;
    /**
     * Execution status
     */
    status?: AgentExecutionStatus;
    /**
     * Input data
     */
    input_data?: (Record<string, any> | null);
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


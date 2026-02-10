/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new RoutingLog.
 */
export type RoutingLogCreate = {
    /**
     * Message ID
     */
    message_id: string;
    /**
     * Routing Result
     */
    routing_result: string;
    /**
     * Confidence Score
     */
    confidence?: (number | null);
    /**
     * Routing Reasoning
     */
    reasoning?: (string | null);
    /**
     * Target Task ID
     */
    target_task_id?: (string | null);
    /**
     * Target Agent ID
     */
    target_agent_id?: (string | null);
};


/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading TaskHistory data.
 */
export type TaskHistoryRead = {
    id: string;
    /**
     * Associated task ID
     */
    task_id: string;
    /**
     * Type of history event
     */
    event_type: string;
    /**
     * Previous value
     */
    previous_value?: (string | null);
    /**
     * New value
     */
    new_value: string;
    /**
     * Assigned agent ID
     */
    assigned_agent_id?: (string | null);
    /**
     * Who made the change
     */
    changed_by: string;
    /**
     * Optional comment
     */
    comment?: (string | null);
    /**
     * Event timestamp
     */
    created_at: string;
};


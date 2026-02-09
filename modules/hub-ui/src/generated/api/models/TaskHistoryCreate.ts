/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new TaskHistory entry.
 */
export type TaskHistoryCreate = {
    /**
     * Associated task ID
     */
    task_id: string;
    /**
     * Type of history event
     */
    event_type: 'status_change' | 'assignment' | 'queue_change' | 'priority_change';
    /**
     * Previous value
     */
    previous_value?: (string | null);
    /**
     * New value
     */
    new_value: string;
    /**
     * Assigned agent ID (for assignment events)
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
};


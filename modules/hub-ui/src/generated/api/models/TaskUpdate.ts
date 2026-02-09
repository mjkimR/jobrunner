/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for updating an existing Task.
 */
export type TaskUpdate = {
    /**
     * Task title
     */
    title?: (string | null);
    /**
     * Task description
     */
    description?: (string | null);
    /**
     * Task status
     */
    status?: ('pending' | 'in_progress' | 'review' | 'done' | 'cancelled' | null);
    /**
     * Priority level
     */
    priority?: ('low' | 'normal' | 'high' | 'critical' | null);
    /**
     * Urgency level
     */
    urgency?: ('low' | 'normal' | 'high' | 'critical' | null);
    /**
     * Complexity level
     */
    complexity?: ('simple' | 'moderate' | 'complex' | null);
    /**
     * Target queue
     */
    queue?: (string | null);
    /**
     * Parent task ID
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source?: ('user' | 'host_agent' | 'gateway' | 'workflow' | 'system' | null);
    /**
     * External reference
     */
    external_ref?: (string | null);
    /**
     * Due date
     */
    due_date?: (string | null);
    /**
     * Completion time
     */
    completed_at?: (string | null);
    /**
     * Result summary
     */
    result_summary?: (string | null);
    /**
     * List of tag names
     */
    tags?: (Array<string> | null);
};


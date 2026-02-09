/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading Task data.
 */
export type TaskRead = {
    created_at: string;
    updated_at: string;
    id: string;
    /**
     * Task title
     */
    title: string;
    /**
     * Task description
     */
    description?: (string | null);
    /**
     * Task status
     */
    status: string;
    /**
     * Priority level
     */
    priority: string;
    /**
     * Urgency level
     */
    urgency: string;
    /**
     * Complexity level
     */
    complexity: string;
    /**
     * Target queue
     */
    queue: string;
    /**
     * Parent task ID
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source: string;
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
};


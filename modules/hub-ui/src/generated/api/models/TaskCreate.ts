/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new Task.
 */
export type TaskCreate = {
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
    status?: 'pending' | 'in_progress' | 'review' | 'done' | 'cancelled';
    /**
     * Priority level
     */
    priority?: 'low' | 'normal' | 'high' | 'critical';
    /**
     * Urgency level (for routing)
     */
    urgency?: 'low' | 'normal' | 'high' | 'critical';
    /**
     * Complexity level (for routing)
     */
    complexity?: 'simple' | 'moderate' | 'complex';
    /**
     * Target queue
     */
    queue?: string;
    /**
     * Parent task ID for subtasks
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source?: 'user' | 'host_agent' | 'gateway' | 'workflow' | 'system';
    /**
     * External reference (e.g., GitHub Issue URL)
     */
    external_ref?: (string | null);
    /**
     * Due date
     */
    due_date?: (string | null);
    /**
     * List of tag names
     */
    tags?: Array<string>;
};


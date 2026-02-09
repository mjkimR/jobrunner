/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TaskComplexity } from './TaskComplexity';
import type { TaskPriority } from './TaskPriority';
import type { TaskQueue } from './TaskQueue';
import type { TaskSource } from './TaskSource';
import type { TaskStatus } from './TaskStatus';
import type { TaskUrgency } from './TaskUrgency';
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
    status?: (TaskStatus | null);
    /**
     * Priority level
     */
    priority?: (TaskPriority | null);
    /**
     * Urgency level
     */
    urgency?: (TaskUrgency | null);
    /**
     * Complexity level
     */
    complexity?: (TaskComplexity | null);
    /**
     * Target queue
     */
    queue?: (TaskQueue | null);
    /**
     * Parent task ID
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source?: (TaskSource | null);
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


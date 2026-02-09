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
    status: TaskStatus;
    /**
     * Priority level
     */
    priority: TaskPriority;
    /**
     * Urgency level
     */
    urgency: TaskUrgency;
    /**
     * Complexity level
     */
    complexity: TaskComplexity;
    /**
     * Target queue
     */
    queue: TaskQueue;
    /**
     * Parent task ID
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source: TaskSource;
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


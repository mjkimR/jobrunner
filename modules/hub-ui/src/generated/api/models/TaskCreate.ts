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
    status?: TaskStatus;
    /**
     * Priority level
     */
    priority?: TaskPriority;
    /**
     * Urgency level (for routing)
     */
    urgency?: TaskUrgency;
    /**
     * Complexity level (for routing)
     */
    complexity?: TaskComplexity;
    /**
     * Target queue
     */
    queue?: TaskQueue;
    /**
     * Parent task ID for subtasks
     */
    parent_task_id?: (string | null);
    /**
     * Task creation source
     */
    source?: TaskSource;
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


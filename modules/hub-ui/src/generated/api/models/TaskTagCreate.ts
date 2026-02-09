/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new TaskTag.
 */
export type TaskTagCreate = {
    /**
     * Tag name (unique)
     */
    name: string;
    /**
     * Tag description
     */
    description?: (string | null);
    /**
     * Hex color code (#RRGGBB)
     */
    color?: (string | null);
};


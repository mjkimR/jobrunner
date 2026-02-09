/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading TaskTag data.
 */
export type TaskTagRead = {
    created_at: string;
    updated_at: string;
    id: string;
    /**
     * Tag name
     */
    name: string;
    /**
     * Tag description
     */
    description?: (string | null);
    /**
     * Hex color code
     */
    color?: (string | null);
};


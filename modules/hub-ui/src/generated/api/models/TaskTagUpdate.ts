/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for updating an existing TaskTag.
 */
export type TaskTagUpdate = {
    /**
     * Tag name (unique)
     */
    name?: (string | null);
    /**
     * Tag description
     */
    description?: (string | null);
    /**
     * Hex color code (#RRGGBB)
     */
    color?: (string | null);
};


/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type WorkspaceUpdate = {
    /**
     * The name of the workspace.
     */
    name?: (string | null);
    /**
     * The alias (api-friendly identifier) of the workspace.
     */
    alias?: (string | null);
    /**
     * A description of the workspace.
     */
    description?: (string | null);
    /**
     * JSONB settings for the workspace.
     */
    meta?: (Record<string, any> | null);
    /**
     * Whether the workspace is active.
     */
    is_active?: (boolean | null);
    /**
     * Whether the workspace is the default workspace.
     */
    is_default?: (boolean | null);
};


/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type WorkspaceCreate = {
    /**
     * The name of the workspace.
     */
    name: string;
    /**
     * The alias (api-friendly identifier) of the workspace.
     */
    alias: string;
    /**
     * A description of the workspace.
     */
    description?: (string | null);
    /**
     * JSONB settings for the workspace.
     */
    meta?: Record<string, any>;
    /**
     * Whether the workspace is active.
     */
    is_active?: boolean;
    /**
     * Whether the workspace is the default workspace.
     */
    is_default?: boolean;
};


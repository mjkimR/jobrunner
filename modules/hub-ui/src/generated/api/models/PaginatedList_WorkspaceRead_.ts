/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { WorkspaceRead } from './WorkspaceRead';
export type PaginatedList_WorkspaceRead_ = {
    items: Array<WorkspaceRead>;
    total_count?: (number | null);
    offset?: number;
    limit?: (number | null);
    /**
     * Check if the current page is the last page
     */
    readonly last: (boolean | null);
    readonly first: boolean;
};


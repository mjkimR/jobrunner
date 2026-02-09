/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { RoutingLogRead } from './RoutingLogRead';
export type PaginatedList_RoutingLogRead_ = {
    items: Array<RoutingLogRead>;
    total_count?: (number | null);
    offset?: number;
    limit?: (number | null);
    /**
     * Check if the current page is the last page
     */
    readonly last: (boolean | null);
    readonly first: boolean;
};


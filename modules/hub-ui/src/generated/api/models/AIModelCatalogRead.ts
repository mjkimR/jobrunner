/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading AI Model data.
 */
export type AIModelCatalogRead = {
    created_at: string;
    updated_at: string;
    id: string;
    /**
     * Catalog version
     */
    version: number;
    /**
     * YAML catalog data as JSON
     */
    data: Record<string, any>;
};


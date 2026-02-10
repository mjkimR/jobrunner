/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading AgentMCP data.
 */
export type AgentMCPRead = {
    /**
     * MCP Server Name
     */
    name: string;
    /**
     * MCP Server Description
     */
    description?: (string | null);
    /**
     * MCP Endpoint (URI or Command)
     */
    mcp_endpoint: string;
    /**
     * Version
     */
    version?: string;
    /**
     * Active status
     */
    is_active?: boolean;
    created_at: string;
    updated_at: string;
    id: string;
};


/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new AgentMCP entry.
 */
export type AgentMCPCreate = {
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
};


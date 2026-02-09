/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentMCPCreate } from '../models/AgentMCPCreate';
import type { AgentMCPRead } from '../models/AgentMCPRead';
import type { AgentMCPUpdate } from '../models/AgentMCPUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AgentMCPRead_ } from '../models/PaginatedList_AgentMCPRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AgentMcpService {
    /**
     * Create Agent Mcp
     * @param requestBody
     * @returns AgentMCPRead Successful Response
     * @throws ApiError
     */
    public static createAgentMcpApiV1AgentMcpsPost(
        requestBody: AgentMCPCreate,
    ): CancelablePromise<AgentMCPRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/agent_mcps',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Agent Mcps
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AgentMCPRead_ Successful Response
     * @throws ApiError
     */
    public static getAgentMcpsApiV1AgentMcpsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AgentMCPRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_mcps',
            query: {
                'offset': offset,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Agent Mcp
     * @param agentMcpId
     * @returns AgentMCPRead Successful Response
     * @throws ApiError
     */
    public static getAgentMcpApiV1AgentMcpsAgentMcpIdGet(
        agentMcpId: string,
    ): CancelablePromise<AgentMCPRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_mcps/{agent_mcp_id}',
            path: {
                'agent_mcp_id': agentMcpId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Agent Mcp
     * @param agentMcpId
     * @param requestBody
     * @returns AgentMCPRead Successful Response
     * @throws ApiError
     */
    public static updateAgentMcpApiV1AgentMcpsAgentMcpIdPut(
        agentMcpId: string,
        requestBody: AgentMCPUpdate,
    ): CancelablePromise<AgentMCPRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/agent_mcps/{agent_mcp_id}',
            path: {
                'agent_mcp_id': agentMcpId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Agent Mcp
     * @param agentMcpId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAgentMcpApiV1AgentMcpsAgentMcpIdDelete(
        agentMcpId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/agent_mcps/{agent_mcp_id}',
            path: {
                'agent_mcp_id': agentMcpId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

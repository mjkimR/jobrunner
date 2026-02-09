/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentExecutionCreate } from '../models/AgentExecutionCreate';
import type { AgentExecutionRead } from '../models/AgentExecutionRead';
import type { AgentExecutionUpdate } from '../models/AgentExecutionUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AgentExecutionRead_ } from '../models/PaginatedList_AgentExecutionRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AgentExecutionService {
    /**
     * Create Agent Execution
     * @param requestBody
     * @returns AgentExecutionRead Successful Response
     * @throws ApiError
     */
    public static createAgentExecutionApiV1AgentExecutionsPost(
        requestBody: AgentExecutionCreate,
    ): CancelablePromise<AgentExecutionRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/agent_executions',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Agent Executions
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AgentExecutionRead_ Successful Response
     * @throws ApiError
     */
    public static getAgentExecutionsApiV1AgentExecutionsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AgentExecutionRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_executions',
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
     * Get Agent Execution
     * @param agentExecutionId
     * @returns AgentExecutionRead Successful Response
     * @throws ApiError
     */
    public static getAgentExecutionApiV1AgentExecutionsAgentExecutionIdGet(
        agentExecutionId: string,
    ): CancelablePromise<AgentExecutionRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_executions/{agent_execution_id}',
            path: {
                'agent_execution_id': agentExecutionId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Agent Execution
     * @param agentExecutionId
     * @param requestBody
     * @returns AgentExecutionRead Successful Response
     * @throws ApiError
     */
    public static updateAgentExecutionApiV1AgentExecutionsAgentExecutionIdPut(
        agentExecutionId: string,
        requestBody: AgentExecutionUpdate,
    ): CancelablePromise<AgentExecutionRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/agent_executions/{agent_execution_id}',
            path: {
                'agent_execution_id': agentExecutionId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Agent Execution
     * @param agentExecutionId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAgentExecutionApiV1AgentExecutionsAgentExecutionIdDelete(
        agentExecutionId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/agent_executions/{agent_execution_id}',
            path: {
                'agent_execution_id': agentExecutionId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

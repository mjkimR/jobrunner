/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AgentSkillCreate } from '../models/AgentSkillCreate';
import type { AgentSkillRead } from '../models/AgentSkillRead';
import type { AgentSkillUpdate } from '../models/AgentSkillUpdate';
import type { DeleteResponse } from '../models/DeleteResponse';
import type { PaginatedList_AgentSkillRead_ } from '../models/PaginatedList_AgentSkillRead_';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class AgentSkillService {
    /**
     * Create Agent Skill
     * @param requestBody
     * @returns AgentSkillRead Successful Response
     * @throws ApiError
     */
    public static createAgentSkillApiV1AgentSkillsPost(
        requestBody: AgentSkillCreate,
    ): CancelablePromise<AgentSkillRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/agent_skills',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Agent Skills
     * @param offset offset for pagination
     * @param limit limit for pagination
     * @returns PaginatedList_AgentSkillRead_ Successful Response
     * @throws ApiError
     */
    public static getAgentSkillsApiV1AgentSkillsGet(
        offset?: number,
        limit: number = 100,
    ): CancelablePromise<PaginatedList_AgentSkillRead_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_skills',
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
     * Get Agent Skill
     * @param agentSkillId
     * @returns AgentSkillRead Successful Response
     * @throws ApiError
     */
    public static getAgentSkillApiV1AgentSkillsAgentSkillIdGet(
        agentSkillId: string,
    ): CancelablePromise<AgentSkillRead> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/agent_skills/{agent_skill_id}',
            path: {
                'agent_skill_id': agentSkillId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Agent Skill
     * @param agentSkillId
     * @param requestBody
     * @returns AgentSkillRead Successful Response
     * @throws ApiError
     */
    public static updateAgentSkillApiV1AgentSkillsAgentSkillIdPut(
        agentSkillId: string,
        requestBody: AgentSkillUpdate,
    ): CancelablePromise<AgentSkillRead> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/agent_skills/{agent_skill_id}',
            path: {
                'agent_skill_id': agentSkillId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Agent Skill
     * @param agentSkillId
     * @returns DeleteResponse Successful Response
     * @throws ApiError
     */
    public static deleteAgentSkillApiV1AgentSkillsAgentSkillIdDelete(
        agentSkillId: string,
    ): CancelablePromise<DeleteResponse> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/agent_skills/{agent_skill_id}',
            path: {
                'agent_skill_id': agentSkillId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}

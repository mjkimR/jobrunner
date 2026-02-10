/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for reading AgentSkill data.
 */
export type AgentSkillRead = {
    /**
     * Skill Name
     */
    name: string;
    /**
     * Skill Description
     */
    description?: (string | null);
    /**
     * Skill Path (SKILL.md)
     */
    skill_path: string;
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


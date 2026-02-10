/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
/**
 * Schema for creating a new AgentSkill entry.
 */
export type AgentSkillCreate = {
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
};


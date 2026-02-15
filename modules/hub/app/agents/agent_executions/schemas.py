"""AgentExecution Schemas for Hub Module.

Pydantic schemas for AgentExecution CRUD operations.
"""

import datetime
from typing import Any
from uuid import UUID

from app.agents.agent_executions.enum import AgentExecutionStatus, AgentExecutionType, AgentType
from app_base.base.schemas.mixin import UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentExecutionBase(BaseModel):
    """Base schema for AgentExecution."""

    agent_type: AgentType = Field(..., description="Type of agent (configured or graph)")
    configured_agent_id: UUID | None = Field(default=None, description="Configured Agent ID")
    graph_agent_name: str | None = Field(default=None, max_length=100, description="Graph Agent Name")
    task_id: UUID | None = Field(default=None, description="Associated Task ID")
    execution_type: AgentExecutionType = Field(..., description="Type of execution")
    status: AgentExecutionStatus = Field(default=AgentExecutionStatus.PENDING, description="Execution status")
    input_data: dict[str, Any] | None = Field(default=None, description="Input data")
    output_data: dict[str, Any] | None = Field(default=None, description="Output data")
    error_message: str | None = Field(default=None, description="Error message")
    started_at: datetime.datetime | None = Field(default=None, description="Start timestamp")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion timestamp")
    token_usage: dict[str, Any] | None = Field(default=None, description="Token usage data")
    run_id: str | None = Field(default=None, max_length=100, description="Run ID")


class AgentExecutionCreate(AgentExecutionBase):
    """Schema for creating a new AgentExecution."""

    pass


class AgentExecutionUpdate(BaseModel):
    """Schema for updating AgentExecution."""

    status: AgentExecutionStatus | None = Field(default=None, description="Execution status")
    output_data: dict[str, Any] | None = Field(default=None, description="Output data")
    error_message: str | None = Field(default=None, description="Error message")
    started_at: datetime.datetime | None = Field(default=None, description="Start timestamp")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion timestamp")
    token_usage: dict[str, Any] | None = Field(default=None, description="Token usage data")
    run_id: str | None = Field(default=None, max_length=100, description="Run ID")


class AgentExecutionRead(UUIDSchemaMixin, AgentExecutionBase):
    """Schema for reading AgentExecution data."""

    created_at: datetime.datetime = Field(..., description="Creation timestamp")
    updated_at: datetime.datetime = Field(..., description="Last update timestamp")

    model_config = ConfigDict(from_attributes=True)

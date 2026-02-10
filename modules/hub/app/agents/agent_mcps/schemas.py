"""AgentMCP Schemas for Hub Module.

Pydantic schemas for AgentMCP CRUD operations.
"""

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentMCPBase(BaseModel):
    """Base schema for AgentMCP."""

    name: str = Field(..., max_length=100, description="MCP Server Name")
    description: str | None = Field(default=None, description="MCP Server Description")
    mcp_endpoint: str = Field(..., max_length=500, description="MCP Endpoint (URI or Command)")
    version: str = Field(default="1.0.0", max_length=20, description="Version")
    is_active: bool = Field(default=True, description="Active status")


class AgentMCPCreate(AgentMCPBase):
    """Schema for creating a new AgentMCP entry."""

    pass


class AgentMCPUpdate(AgentMCPBase):
    """Schema for updating AgentMCP."""

    name: str | None = Field(default=None, max_length=100, description="MCP Server Name")
    description: str | None = Field(default=None, description="MCP Server Description")
    mcp_endpoint: str | None = Field(default=None, max_length=500, description="MCP Endpoint")
    version: str | None = Field(default=None, max_length=20, description="Version")
    is_active: bool | None = Field(default=None, description="Active status")


class AgentMCPRead(UUIDSchemaMixin, TimestampSchemaMixin, AgentMCPBase):
    """Schema for reading AgentMCP data."""

    model_config = ConfigDict(from_attributes=True)

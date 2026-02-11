"""AgentExecution Model for Hub Module.

AgentExecution: History of agent executions.
DB Schema Reference: docs/specification/DB_SCHEMA.md#2.4
"""

import datetime
from typing import TYPE_CHECKING, Any, Optional
from uuid import UUID

from app.agents.agent_executions.enum import AgentExecutionStatus
from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.agents.configured_agents.models import ConfiguredAgent
    from app.tasks.tasks.models import Task


class AgentExecution(Base, UUIDMixin, TimestampMixin):
    """Agent execution record."""

    __tablename__ = "agent_executions"

    # Agent info
    agent_type: Mapped[str] = mapped_column(String(50), nullable=False)
    configured_agent_id: Mapped[UUID | None] = mapped_column(ForeignKey("configured_agents.id"), nullable=True)
    graph_agent_name: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Context
    task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id"), nullable=True)
    execution_type: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default=AgentExecutionStatus.PENDING)

    # Data
    input_data: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    output_data: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timing
    started_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Usage
    token_usage: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    dagster_run_id: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Relationships
    configured_agent: Mapped[Optional["ConfiguredAgent"]] = relationship("ConfiguredAgent")
    task: Mapped[Optional["Task"]] = relationship("Task")

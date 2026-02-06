from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from app.features.rule_executions.models import RuleExecutionStatus
from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin


class RuleExecutionCreate(BaseModel):
    rule_id: Any = Field(description="The rule id being executed.")
    status: RuleExecutionStatus = Field(description="Execution status.")
    executed_at: datetime = Field(description="Execution start time (timezone-aware).")

    log_summary: str | None = Field(default=None, description="Short log summary.")
    artifact_path: str | None = Field(
        default=None, description="Artifact path in storage."
    )


class RuleExecutionUpdate(BaseModel):
    status: RuleExecutionStatus | None = Field(
        default=None, description="Execution status."
    )
    log_summary: str | None = Field(default=None, description="Short log summary.")
    artifact_path: str | None = Field(
        default=None, description="Artifact path in storage."
    )


class RuleExecutionRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    rule_id: Any = Field(..., description="The rule id being executed.")
    status: RuleExecutionStatus = Field(..., description="Execution status.")
    executed_at: datetime = Field(
        ..., description="Execution start time (timezone-aware)."
    )

    log_summary: str | None = Field(default=None, description="Short log summary.")
    artifact_path: str | None = Field(
        default=None, description="Artifact path in storage."
    )

    model_config = ConfigDict(from_attributes=True)

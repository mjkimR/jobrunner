from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin


class RuleCreate(BaseModel):
    name: str = Field(description="The name of the rule.")
    schedule: str = Field(description="Cron expression.")
    execution_script_path: str = Field(
        description="Relative path to the execution script."
    )
    next_run_at: datetime = Field(
        description="Next scheduled run time (timezone-aware)."
    )

    is_active: bool = Field(default=True, description="Whether the rule is active.")
    payload: dict[str, Any] = Field(
        default_factory=dict, description="Payload passed to the script."
    )
    on_success: dict[str, Any] | None = Field(
        default=None, description="Callback config on success."
    )
    on_failure: dict[str, Any] | None = Field(
        default=None, description="Callback config on failure."
    )


class RuleUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the rule.")
    schedule: str | None = Field(default=None, description="Cron expression.")
    execution_script_path: str | None = Field(
        default=None, description="Relative path to the execution script."
    )
    next_run_at: datetime | None = Field(
        default=None, description="Next scheduled run time (timezone-aware)."
    )

    is_active: bool | None = Field(
        default=None, description="Whether the rule is active."
    )
    payload: dict[str, Any] | None = Field(
        default=None, description="Payload passed to the script."
    )
    on_success: dict[str, Any] | None = Field(
        default=None, description="Callback config on success."
    )
    on_failure: dict[str, Any] | None = Field(
        default=None, description="Callback config on failure."
    )


class RuleRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the rule.")
    schedule: str = Field(..., description="Cron expression.")
    execution_script_path: str = Field(
        ..., description="Relative path to the execution script."
    )
    next_run_at: datetime = Field(
        ..., description="Next scheduled run time (timezone-aware)."
    )

    is_active: bool = Field(..., description="Whether the rule is active.")
    payload: dict[str, Any] = Field(..., description="Payload passed to the script.")
    on_success: dict[str, Any] | None = Field(
        default=None, description="Callback config on success."
    )
    on_failure: dict[str, Any] | None = Field(
        default=None, description="Callback config on failure."
    )

    model_config = ConfigDict(from_attributes=True)

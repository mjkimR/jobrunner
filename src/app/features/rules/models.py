from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, DateTime, Index, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin


class Rule(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "rules"

    name: Mapped[str] = mapped_column(Text, nullable=False)
    schedule: Mapped[str] = mapped_column(Text, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    payload: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)

    execution_script_path: Mapped[str] = mapped_column(Text, nullable=False)
    on_success: Mapped[dict[str, Any] | None] = mapped_column(JSONB, nullable=True)
    on_failure: Mapped[dict[str, Any] | None] = mapped_column(JSONB, nullable=True)

    next_run_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, index=True
    )

    executions = relationship(
        "RuleExecution",
        back_populates="rule",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    __table_args__ = (
        Index("ix_rules_is_active_next_run_at", is_active, next_run_at),
    )

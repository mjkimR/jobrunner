from app.common.database import JSON_VARIANT
from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Boolean, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Workspace(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "workspaces"
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    alias: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    meta: Mapped[dict] = mapped_column(JSON_VARIANT, nullable=False, default={})
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    __table_args__ = (
        # Partial unique index: only one workspace can have is_default=True
        Index(
            "ix_workspaces_is_default_unique",
            "is_default",
            unique=True,
            postgresql_where=is_default.is_(True),
            sqlite_where=is_default.is_(True),
        ),
    )

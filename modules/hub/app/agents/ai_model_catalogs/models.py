"""AI Model Catalog Model for Hub Module.

AIModelCatalog: AI model catalog storage.
DB Schema Reference: docs/specification/DB_SCHEMA.md#2.1
"""

from app.common.database import JSON_VARIANT
from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class AIModelCatalog(Base, UUIDMixin, TimestampMixin):
    """AI Model Catalog entity storing the entire YAML content."""

    __tablename__ = "ai_model_catalogs"

    version: Mapped[int] = mapped_column(Integer, nullable=False)
    data: Mapped[dict] = mapped_column(JSON_VARIANT, nullable=False)

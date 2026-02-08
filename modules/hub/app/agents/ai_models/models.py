from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class AIModel(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ai_models"
    name: Mapped[str] = mapped_column()

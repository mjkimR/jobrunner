from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class TaskTag(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "task_tags"
    name: Mapped[str] = mapped_column()

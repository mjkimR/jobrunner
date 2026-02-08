from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class TaskHistory(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "task_histories"
    name: Mapped[str] = mapped_column()

from sqlalchemy.orm import Mapped, mapped_column

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin


class Task(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "tasks"
    name: Mapped[str] = mapped_column()

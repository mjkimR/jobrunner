"""TaskTag Repository for Hub Module."""

from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
from app_base.base.repos.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class TaskTagRepository(BaseRepository[TaskTag, TaskTagCreate, TaskTagUpdate]):
    """Repository for TaskTag CRUD operations."""

    model = TaskTag

    async def get_by_name(self, session: AsyncSession, name: str) -> TaskTag | None:
        """Get a tag by name."""
        return await self.get(session, where=self.model.name == name)

"""TaskTag Repository for Hub Module."""

from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
from app_base.base.repos.base import BaseRepository


class TaskTagRepository(BaseRepository[TaskTag, TaskTagCreate, TaskTagUpdate]):
    """Repository for TaskTag CRUD operations."""

    model = TaskTag

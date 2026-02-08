"""TaskHistory Repository for Hub Module."""

from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryUpdate
from app_base.base.repos.base import BaseRepository


class TaskHistoryRepository(BaseRepository[TaskHistory, TaskHistoryCreate, TaskHistoryUpdate]):
    """Repository for TaskHistory CRUD operations."""

    model = TaskHistory

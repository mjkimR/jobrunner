"""Task Repository for Hub Module."""

from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate, TaskUpdate
from app_base.base.repos.base import BaseRepository


class TaskRepository(BaseRepository[Task, TaskCreate, TaskUpdate]):
    """Repository for Task CRUD operations."""

    model = Task

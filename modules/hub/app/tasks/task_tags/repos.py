from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
from app_base.base.repos.base import BaseRepository


class TaskTagRepository(BaseRepository[TaskTag, TaskTagCreate, TaskTagUpdate]):
    model = TaskTag

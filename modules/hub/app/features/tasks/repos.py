from app_base.base.repos.base import BaseRepository
from app.features.tasks.models import Task
from app.features.tasks.schemas import TaskCreate, TaskUpdate


class TaskRepository(BaseRepository[Task, TaskCreate, TaskUpdate]):
    model = Task

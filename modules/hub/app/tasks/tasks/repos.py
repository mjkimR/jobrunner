from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate, TaskUpdate
from app_base.base.repos.base import BaseRepository


class TaskRepository(BaseRepository[Task, TaskCreate, TaskUpdate]):
    model = Task

from typing import Annotated

from fastapi import Depends

from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app.features.tasks.models import Task
from app.features.tasks.repos import TaskRepository
from app.features.tasks.schemas import TaskCreate, TaskUpdate


class TaskService(
    BaseCreateServiceMixin[TaskRepository, Task, TaskCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[TaskRepository, Task, BaseContextKwargs],
    BaseGetServiceMixin[TaskRepository, Task, BaseContextKwargs],
    BaseUpdateServiceMixin[TaskRepository, Task, TaskUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[TaskRepository, Task, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[TaskRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> TaskRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs

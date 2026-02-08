"""TaskHistory Service for Hub Module."""

from typing import Annotated

from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.repos import TaskHistoryRepository
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class TaskHistoryService(
    BaseCreateServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[TaskHistoryRepository, TaskHistory, BaseContextKwargs],
    BaseGetServiceMixin[TaskHistoryRepository, TaskHistory, BaseContextKwargs],
    BaseUpdateServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[TaskHistoryRepository, TaskHistory, BaseContextKwargs],
):
    """Service for TaskHistory business logic."""

    def __init__(self, repo: Annotated[TaskHistoryRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> TaskHistoryRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs

from typing import Annotated

from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class TaskTagService(
    BaseCreateServiceMixin[TaskTagRepository, TaskTag, TaskTagCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
    BaseGetServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
    BaseUpdateServiceMixin[TaskTagRepository, TaskTag, TaskTagUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[TaskTagRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> TaskTagRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs

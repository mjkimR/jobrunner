"""TaskHistory Service for Hub Module."""

from typing import Annotated

from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.repos import TaskHistoryRepository
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryUpdate
from app_base.base.repos.base import BaseRepository
from app_base.base.services.base import (
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app_base.base.services.nested_resource_hook import NestedResourceContextKwargs, NestedResourceHooksMixin
from fastapi import Depends


class TaskHistoryContextKwargs(NestedResourceContextKwargs):
    pass


class TaskHistoryService(
    NestedResourceHooksMixin,
    BaseCreateServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryCreate, TaskHistoryContextKwargs],
    BaseGetMultiServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryContextKwargs],
    BaseGetServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryContextKwargs],
    BaseUpdateServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryUpdate, TaskHistoryContextKwargs],
    BaseDeleteServiceMixin[TaskHistoryRepository, TaskHistory, TaskHistoryContextKwargs],
):
    """Service for TaskHistory business logic."""

    def __init__(
        self,
        repo: Annotated[TaskHistoryRepository, Depends()],
        repo_workspace: Annotated[WorkspaceRepository, Depends()],
    ):
        self._repo = repo
        self._parent_repo = repo_workspace

    @property
    def repo(self) -> TaskHistoryRepository:
        return self._repo

    @property
    def parent_repo(self) -> BaseRepository:
        return self._parent_repo

    @property
    def context_model(self):
        return TaskHistoryContextKwargs

    @property
    def fk_name(self) -> str:
        return "workspace_id"

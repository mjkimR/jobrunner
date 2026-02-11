"""Task Service for Hub Module."""

from typing import Annotated

from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.schemas import TaskDbCreate, TaskDbUpdate
from app_base.base.repos.base import BaseRepository
from app_base.base.services.base import (
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app_base.base.services.exists_check_hook import ExistsCheckHooksMixin
from app_base.base.services.nested_resource_hook import NestedResourceContextKwargs, NestedResourceHooksMixin
from fastapi import Depends


class TaskContextKwargs(NestedResourceContextKwargs):
    pass


class TaskService(
    NestedResourceHooksMixin,  # Relationship with Workspace
    ExistsCheckHooksMixin,  # Ensure existence checks before operations
    BaseCreateServiceMixin[TaskRepository, Task, TaskDbCreate, TaskContextKwargs],
    BaseGetMultiServiceMixin[TaskRepository, Task, TaskContextKwargs],
    BaseGetServiceMixin[TaskRepository, Task, TaskContextKwargs],
    BaseUpdateServiceMixin[TaskRepository, Task, TaskDbUpdate, TaskContextKwargs],
    BaseDeleteServiceMixin[TaskRepository, Task, TaskContextKwargs],
):
    """Service for Task business logic."""

    def __init__(
        self,
        repo: Annotated[TaskRepository, Depends()],
        repo_workspace: Annotated[WorkspaceRepository, Depends()],
    ):
        self._repo = repo
        self._parent_repo = repo_workspace

    @property
    def repo(self) -> TaskRepository:
        return self._repo

    @property
    def parent_repo(self) -> BaseRepository:
        return self._parent_repo

    @property
    def context_model(self):
        return TaskContextKwargs

    @property
    def fk_name(self) -> str:
        return "workspace_id"

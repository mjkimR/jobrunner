"""TaskTag Service for Hub Module."""

from typing import Annotated, Union

from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
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
from app_base.base.services.unique_constraints_hook import UniqueConstraintHooksMixin
from fastapi import Depends
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession


class TaskTagContextKwargs(NestedResourceContextKwargs):
    pass


class TaskTagService(
    NestedResourceHooksMixin,  # Relationship with Workspace
    UniqueConstraintHooksMixin,  # Ensure unique constraints before create/update
    ExistsCheckHooksMixin,  # Ensure existence checks before operations
    BaseCreateServiceMixin[TaskTagRepository, TaskTag, TaskTagCreate, TaskTagContextKwargs],
    BaseGetMultiServiceMixin[TaskTagRepository, TaskTag, TaskTagContextKwargs],
    BaseGetServiceMixin[TaskTagRepository, TaskTag, TaskTagContextKwargs],
    BaseUpdateServiceMixin[TaskTagRepository, TaskTag, TaskTagUpdate, TaskTagContextKwargs],
    BaseDeleteServiceMixin[TaskTagRepository, TaskTag, TaskTagContextKwargs],
):
    """Service for TaskTag business logic."""

    def __init__(
        self, repo: Annotated[TaskTagRepository, Depends()], repo_workspace: Annotated[WorkspaceRepository, Depends()]
    ):
        self._repo = repo
        self._parent_repo = repo_workspace

    @property
    def repo(self) -> TaskTagRepository:
        return self._repo

    @property
    def parent_repo(self) -> BaseRepository:
        return self._parent_repo

    @property
    def context_model(self):
        return TaskTagContextKwargs

    @property
    def fk_name(self) -> str:
        return "workspace_id"

    async def _unique_constraints(
        self,
        obj_data: Union[TaskTagCreate, TaskTagUpdate],
        context: TaskTagContextKwargs,
    ):
        if obj_data.name is not None:
            yield (
                and_(self.repo.model.name == obj_data.name, self.repo.model.workspace_id == context["parent_id"]),
                "TaskTag with this name already exists in the workspace.",
            )

    async def get_or_create_tags(
        self, session: AsyncSession, tag_names: list[str], context: TaskTagContextKwargs | None
    ) -> list[TaskTag]:
        """Get existing tags or create new ones from a list of names."""
        tags = []
        for name in tag_names:
            normalized_name = name.strip()
            if not normalized_name:
                continue

            if context is None:
                raise ValueError("Context is required for get_or_create_tags")

            tag = await self.repo.get_by_name(session, normalized_name, context["parent_id"])
            if not tag:
                # Create new tag
                tag_create = TaskTagCreate(name=normalized_name)
                tag = await self.create(session, tag_create, context)
            tags.append(tag)
        return tags

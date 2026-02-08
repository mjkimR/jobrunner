"""TaskTag Service for Hub Module."""

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
from sqlalchemy.ext.asyncio import AsyncSession


class TaskTagService(
    BaseCreateServiceMixin[TaskTagRepository, TaskTag, TaskTagCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
    BaseGetServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
    BaseUpdateServiceMixin[TaskTagRepository, TaskTag, TaskTagUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[TaskTagRepository, TaskTag, BaseContextKwargs],
):
    """Service for TaskTag business logic."""

    def __init__(self, repo: Annotated[TaskTagRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> TaskTagRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs

    async def get_or_create_tags(self, session: AsyncSession, tag_names: list[str]) -> list[TaskTag]:
        """Get existing tags or create new ones from a list of names."""
        tags = []
        for name in tag_names:
            normalized_name = name.strip()
            if not normalized_name:
                continue

            tag = await self.repo.get_by_name(session, normalized_name)
            if not tag:
                # Create new tag
                tag_create = TaskTagCreate(name=normalized_name)
                tag = await self.create(session, tag_create)
            tags.append(tag)
        return tags

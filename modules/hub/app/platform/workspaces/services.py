from typing import Annotated, Union
from uuid import UUID

from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.schemas import WorkspaceCreate, WorkspaceUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app_base.base.services.exists_check_hook import ExistsCheckHooksMixin
from app_base.base.services.unique_constraints_hook import UniqueConstraintHooksMixin
from fastapi import Depends
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


class WorkspaceContextKwargs(BaseContextKwargs):
    pass


class WorkspaceService(
    UniqueConstraintHooksMixin,  # Ensure unique constraints before create/update
    ExistsCheckHooksMixin,  # Ensure existence checks before operations
    BaseCreateServiceMixin[WorkspaceRepository, Workspace, WorkspaceCreate, WorkspaceContextKwargs],
    BaseGetMultiServiceMixin[WorkspaceRepository, Workspace, WorkspaceContextKwargs],
    BaseGetServiceMixin[WorkspaceRepository, Workspace, WorkspaceContextKwargs],
    BaseUpdateServiceMixin[WorkspaceRepository, Workspace, WorkspaceUpdate, WorkspaceContextKwargs],
    BaseDeleteServiceMixin[WorkspaceRepository, Workspace, WorkspaceContextKwargs],
):
    def __init__(self, repo: Annotated[WorkspaceRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> WorkspaceRepository:
        return self._repo

    @property
    def context_model(self):
        return WorkspaceContextKwargs

    async def _unique_constraints(
        self,
        obj_data: Union[WorkspaceCreate, WorkspaceUpdate],
        context: WorkspaceContextKwargs,
    ):
        if obj_data.name:
            yield self.repo.model.name == obj_data.name, "Workspace name must be unique."
        if obj_data.alias:
            yield self.repo.model.alias == obj_data.alias, "Workspace alias must be unique."

    async def _clear_other_defaults(self, session: AsyncSession, exclude_id: UUID | str | None = None):
        """Clear is_default=True from all other workspaces."""
        stmt = update(Workspace).where(Workspace.is_default.is_(True)).values(is_default=False)
        if exclude_id:
            stmt = stmt.where(Workspace.id != exclude_id)
        await session.execute(stmt)

    async def create(
        self,
        session: AsyncSession,
        obj_in: WorkspaceCreate,
        context: WorkspaceContextKwargs | None = None,
        **update_fields,
    ) -> Workspace:
        """Create a new workspace, ensuring only one default workspace exists."""
        # If creating a default workspace, clear other defaults first
        if obj_in.is_default:
            await self._clear_other_defaults(session)
        # Call parent create method
        return await super().create(session, obj_in, context, **update_fields)

    async def update(
        self,
        session: AsyncSession,
        obj_id: UUID,
        obj_in: WorkspaceUpdate,
        context: WorkspaceContextKwargs | None = None,
        **update_fields,
    ) -> Workspace:
        """Update a workspace, ensuring only one default workspace exists."""
        # If setting this workspace as default, clear other defaults first
        if obj_in.is_default is True:
            await self._clear_other_defaults(session, exclude_id=obj_id)

        # Call parent update method
        return await super().update(session, obj_id, obj_in, context, **update_fields)

from typing import Annotated

from app.platform.workspaces.models import Workspace
from app.platform.workspaces.schemas import WorkspaceCreate, WorkspaceUpdate
from app.platform.workspaces.services import WorkspaceContextKwargs, WorkspaceService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetWorkspaceUseCase(BaseGetUseCase[WorkspaceService, Workspace, WorkspaceContextKwargs]):
    def __init__(self, service: Annotated[WorkspaceService, Depends()]) -> None:
        super().__init__(service)


class GetMultiWorkspaceUseCase(BaseGetMultiUseCase[WorkspaceService, Workspace, WorkspaceContextKwargs]):
    def __init__(self, service: Annotated[WorkspaceService, Depends()]) -> None:
        super().__init__(service)


class CreateWorkspaceUseCase(BaseCreateUseCase[WorkspaceService, Workspace, WorkspaceCreate, WorkspaceContextKwargs]):
    def __init__(self, service: Annotated[WorkspaceService, Depends()]) -> None:
        super().__init__(service)


class UpdateWorkspaceUseCase(BaseUpdateUseCase[WorkspaceService, Workspace, WorkspaceUpdate, WorkspaceContextKwargs]):
    def __init__(self, service: Annotated[WorkspaceService, Depends()]) -> None:
        super().__init__(service)


class DeleteWorkspaceUseCase(BaseDeleteUseCase[WorkspaceService, Workspace, WorkspaceContextKwargs]):
    def __init__(self, service: Annotated[WorkspaceService, Depends()]) -> None:
        super().__init__(service)

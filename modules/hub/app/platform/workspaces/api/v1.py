from typing import Annotated
from uuid import UUID

from app.platform.workspaces.schemas import WorkspaceCreate, WorkspaceRead, WorkspaceUpdate
from app.platform.workspaces.usecases.crud import (
    CreateWorkspaceUseCase,
    DeleteWorkspaceUseCase,
    GetMultiWorkspaceUseCase,
    GetWorkspaceUseCase,
    UpdateWorkspaceUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/workspaces", tags=["Workspaces"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=WorkspaceRead)
async def create_workspace(
    use_case: Annotated[CreateWorkspaceUseCase, Depends()],
    workspace_in: WorkspaceCreate,
):
    return await use_case.execute(workspace_in)


@router.get("", response_model=PaginatedList[WorkspaceRead])
async def get_workspaces(
    use_case: Annotated[GetMultiWorkspaceUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{workspace_id}", response_model=WorkspaceRead)
async def get_workspace(
    use_case: Annotated[GetWorkspaceUseCase, Depends()],
    workspace_id: UUID,
):
    workspace = await use_case.execute(workspace_id)
    if not workspace:
        raise NotFoundException()
    return workspace


@router.put("/{workspace_id}", response_model=WorkspaceRead)
async def update_workspace(
    use_case: Annotated[UpdateWorkspaceUseCase, Depends()],
    workspace_id: UUID,
    workspace_in: WorkspaceUpdate,
):
    workspace = await use_case.execute(workspace_id, workspace_in)
    if not workspace:
        raise NotFoundException()
    return workspace


@router.delete("/{workspace_id}", response_model=DeleteResponse)
async def delete_workspace(
    use_case: Annotated[DeleteWorkspaceUseCase, Depends()],
    workspace_id: UUID,
):
    return await use_case.execute(workspace_id)

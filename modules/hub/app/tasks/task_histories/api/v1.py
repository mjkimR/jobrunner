from typing import Annotated
from uuid import UUID

from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryRead, TaskHistoryUpdate
from app.tasks.task_histories.services import TaskHistoryContextKwargs
from app.tasks.task_histories.usecases.crud import (
    CreateTaskHistoryUseCase,
    DeleteTaskHistoryUseCase,
    GetMultiTaskHistoryUseCase,
    GetTaskHistoryUseCase,
    UpdateTaskHistoryUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/workspaces/{workspace_id}/task_histories", tags=["TaskHistories"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskHistoryRead)
async def create_task_history(
    workspace_id: UUID,
    use_case: Annotated[CreateTaskHistoryUseCase, Depends()],
    task_history_in: TaskHistoryCreate,
):
    context: TaskHistoryContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_history_in, context=context)


@router.get("", response_model=PaginatedList[TaskHistoryRead])
async def get_task_histories(
    workspace_id: UUID,
    use_case: Annotated[GetMultiTaskHistoryUseCase, Depends()],
    pagination: PaginationParam,
):
    context: TaskHistoryContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(**pagination, context=context)


@router.get("/{task_history_id}", response_model=TaskHistoryRead)
async def get_task_history(
    workspace_id: UUID,
    use_case: Annotated[GetTaskHistoryUseCase, Depends()],
    task_history_id: UUID,
):
    context: TaskHistoryContextKwargs = {"parent_id": workspace_id}
    task_history = await use_case.execute(task_history_id, context=context)
    if not task_history:
        raise NotFoundException()
    return task_history


@router.put("/{task_history_id}", response_model=TaskHistoryRead)
async def update_task_history(
    workspace_id: UUID,
    use_case: Annotated[UpdateTaskHistoryUseCase, Depends()],
    task_history_id: UUID,
    task_history_in: TaskHistoryUpdate,
):
    context: TaskHistoryContextKwargs = {"parent_id": workspace_id}
    task_history = await use_case.execute(task_history_id, task_history_in, context=context)
    if not task_history:
        raise NotFoundException()
    return task_history


@router.delete("/{task_history_id}", response_model=DeleteResponse)
async def delete_task_history(
    workspace_id: UUID,
    use_case: Annotated[DeleteTaskHistoryUseCase, Depends()],
    task_history_id: UUID,
):
    context: TaskHistoryContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_history_id, context=context)

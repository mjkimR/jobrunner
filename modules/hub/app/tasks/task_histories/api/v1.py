import uuid
from typing import Annotated

from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryRead, TaskHistoryUpdate
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

router = APIRouter(prefix="/task_histories", tags=["TaskHistorie"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskHistoryRead)
async def create_task_history(
    use_case: Annotated[CreateTaskHistoryUseCase, Depends()],
    task_history_in: TaskHistoryCreate,
):
    return await use_case.execute(task_history_in)


@router.get("", response_model=PaginatedList[TaskHistoryRead])
async def get_task_histories(
    use_case: Annotated[GetMultiTaskHistoryUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{task_history_id}", response_model=TaskHistoryRead)
async def get_task_history(
    use_case: Annotated[GetTaskHistoryUseCase, Depends()],
    task_history_id: uuid.UUID,
):
    task_history = await use_case.execute(task_history_id)
    if not task_history:
        raise NotFoundException()
    return task_history


@router.put("/{task_history_id}", response_model=TaskHistoryRead)
async def update_task_history(
    use_case: Annotated[UpdateTaskHistoryUseCase, Depends()],
    task_history_id: uuid.UUID,
    task_history_in: TaskHistoryUpdate,
):
    task_history = await use_case.execute(task_history_id, task_history_in)
    if not task_history:
        raise NotFoundException()
    return task_history


@router.delete("/{task_history_id}", response_model=DeleteResponse)
async def delete_task_history(
    use_case: Annotated[DeleteTaskHistoryUseCase, Depends()],
    task_history_id: uuid.UUID,
):
    return await use_case.execute(task_history_id)

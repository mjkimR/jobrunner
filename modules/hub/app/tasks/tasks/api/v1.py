import uuid
from typing import Annotated

from app.tasks.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from app.tasks.tasks.usecases.crud import (
    CreateTaskUseCase,
    DeleteTaskUseCase,
    GetMultiTaskUseCase,
    GetTaskUseCase,
    UpdateTaskUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/tasks", tags=["Tasks"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskRead)
async def create_task(
    use_case: Annotated[CreateTaskUseCase, Depends()],
    task_in: TaskCreate,
):
    return await use_case.execute(task_in)


@router.get("", response_model=PaginatedList[TaskRead])
async def get_tasks(
    use_case: Annotated[GetMultiTaskUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    use_case: Annotated[GetTaskUseCase, Depends()],
    task_id: uuid.UUID,
):
    task = await use_case.execute(task_id)
    if not task:
        raise NotFoundException()
    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    use_case: Annotated[UpdateTaskUseCase, Depends()],
    task_id: uuid.UUID,
    task_in: TaskUpdate,
):
    task = await use_case.execute(task_id, task_in)
    if not task:
        raise NotFoundException()
    return task


@router.delete("/{task_id}", response_model=DeleteResponse)
async def delete_task(
    use_case: Annotated[DeleteTaskUseCase, Depends()],
    task_id: uuid.UUID,
):
    return await use_case.execute(task_id)

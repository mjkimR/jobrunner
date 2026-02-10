from typing import Annotated
from uuid import UUID

from app.tasks.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from app.tasks.tasks.services import TagContextKwargs
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

router = APIRouter(prefix="/workspace/{workspace_id}/tasks", tags=["Task"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskRead)
async def create_task(
    workspace_id: UUID,
    use_case: Annotated[CreateTaskUseCase, Depends()],
    task_in: TaskCreate,
):
    context: TagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_in, context)


@router.get("", response_model=PaginatedList[TaskRead])
async def get_tasks(
    workspace_id: UUID,
    use_case: Annotated[GetMultiTaskUseCase, Depends()],
    pagination: PaginationParam,
):
    context: TagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(**pagination, context=context)


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    workspace_id: UUID,
    use_case: Annotated[GetTaskUseCase, Depends()],
    task_id: UUID,
):
    context: TagContextKwargs = {"parent_id": workspace_id}
    task = await use_case.execute(task_id, context=context)
    if not task:
        raise NotFoundException()
    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    workspace_id: UUID,
    use_case: Annotated[UpdateTaskUseCase, Depends()],
    task_id: UUID,
    task_in: TaskUpdate,
):
    context: TagContextKwargs = {"parent_id": workspace_id}
    task = await use_case.execute(task_id, task_in, context=context)
    if not task:
        raise NotFoundException()
    return task


@router.delete("/{task_id}", response_model=DeleteResponse)
async def delete_task(
    workspace_id: UUID,
    use_case: Annotated[DeleteTaskUseCase, Depends()],
    task_id: UUID,
):
    context: TagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_id, context=context)

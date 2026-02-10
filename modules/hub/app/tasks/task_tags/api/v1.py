from typing import Annotated
from uuid import UUID

from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagRead, TaskTagUpdate
from app.tasks.task_tags.services import TaskTagContextKwargs
from app.tasks.task_tags.usecases.crud import (
    CreateTaskTagUseCase,
    DeleteTaskTagUseCase,
    GetMultiTaskTagUseCase,
    GetTaskTagUseCase,
    UpdateTaskTagUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/workspace/{workspace_id}/task_tags", tags=["TaskTag"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskTagRead)
async def create_task_tag(
    workspace_id: UUID,
    use_case: Annotated[CreateTaskTagUseCase, Depends()],
    task_tag_in: TaskTagCreate,
):
    context: TaskTagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_tag_in, context=context)


@router.get("", response_model=PaginatedList[TaskTagRead])
async def get_task_tags(
    workspace_id: UUID,
    use_case: Annotated[GetMultiTaskTagUseCase, Depends()],
    pagination: PaginationParam,
):
    context: TaskTagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(**pagination, context=context)


@router.get("/{task_tag_id}", response_model=TaskTagRead)
async def get_task_tag(
    workspace_id: UUID,
    use_case: Annotated[GetTaskTagUseCase, Depends()],
    task_tag_id: UUID,
):
    context = {"workspace_id": workspace_id}
    task_tag = await use_case.execute(task_tag_id, context=context)
    if not task_tag:
        raise NotFoundException()
    return task_tag


@router.put("/{task_tag_id}", response_model=TaskTagRead)
async def update_task_tag(
    workspace_id: UUID,
    use_case: Annotated[UpdateTaskTagUseCase, Depends()],
    task_tag_id: UUID,
    task_tag_in: TaskTagUpdate,
):
    context: TaskTagContextKwargs = {"parent_id": workspace_id}
    task_tag = await use_case.execute(task_tag_id, task_tag_in, context=context)
    if not task_tag:
        raise NotFoundException()
    return task_tag


@router.delete("/{task_tag_id}", response_model=DeleteResponse)
async def delete_task_tag(
    workspace_id: UUID,
    use_case: Annotated[DeleteTaskTagUseCase, Depends()],
    task_tag_id: UUID,
):
    context: TaskTagContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(task_tag_id, context=context)

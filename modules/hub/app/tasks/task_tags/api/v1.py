import uuid
from typing import Annotated

from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagRead, TaskTagUpdate
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

router = APIRouter(prefix="/task_tags", tags=["TaskTags"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TaskTagRead)
async def create_task_tag(
    use_case: Annotated[CreateTaskTagUseCase, Depends()],
    task_tag_in: TaskTagCreate,
):
    return await use_case.execute(task_tag_in)


@router.get("", response_model=PaginatedList[TaskTagRead])
async def get_task_tags(
    use_case: Annotated[GetMultiTaskTagUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{task_tag_id}", response_model=TaskTagRead)
async def get_task_tag(
    use_case: Annotated[GetTaskTagUseCase, Depends()],
    task_tag_id: uuid.UUID,
):
    task_tag = await use_case.execute(task_tag_id)
    if not task_tag:
        raise NotFoundException()
    return task_tag


@router.put("/{task_tag_id}", response_model=TaskTagRead)
async def update_task_tag(
    use_case: Annotated[UpdateTaskTagUseCase, Depends()],
    task_tag_id: uuid.UUID,
    task_tag_in: TaskTagUpdate,
):
    task_tag = await use_case.execute(task_tag_id, task_tag_in)
    if not task_tag:
        raise NotFoundException()
    return task_tag


@router.delete("/{task_tag_id}", response_model=DeleteResponse)
async def delete_task_tag(
    use_case: Annotated[DeleteTaskTagUseCase, Depends()],
    task_tag_id: uuid.UUID,
):
    return await use_case.execute(task_tag_id)

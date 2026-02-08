import uuid
from typing import Annotated, Optional

from app.tasks.task_tags.services import TaskTagService
from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate, TaskDbCreate, TaskDbUpdate, TaskUpdate
from app.tasks.tasks.services import TagContextKwargs, TaskService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class GetTaskUseCase(BaseGetUseCase[TaskService, Task, TagContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class GetMultiTaskUseCase(BaseGetMultiUseCase[TaskService, Task, TagContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class CreateTaskUseCase(BaseCreateUseCase[TaskService, Task, TaskCreate, TagContextKwargs]):
    def __init__(
        self, service: Annotated[TaskService, Depends()], tag_service: Annotated[TaskTagService, Depends()]
    ) -> None:
        super().__init__(service)
        self.tag_service = tag_service

    async def _execute(self, session: AsyncSession, obj_data: TaskCreate, context: Optional[TagContextKwargs]) -> Task:
        # Get or create tag objects
        tags = obj_data.tags
        tag_objects = await self.tag_service.get_or_create_tags(session, tags)

        # Create Task
        db_obj = TaskDbCreate.model_validate(obj_data.model_dump(exclude={"tags"}))
        db_obj.tags = tag_objects

        return await super()._execute(session, db_obj, context)


class UpdateTaskUseCase(BaseUpdateUseCase[TaskService, Task, TaskUpdate, TagContextKwargs]):
    def __init__(
        self, service: Annotated[TaskService, Depends()], tag_service: Annotated[TaskTagService, Depends()]
    ) -> None:
        super().__init__(service)
        self.tag_service = tag_service

    async def _execute(
        self, session: AsyncSession, obj_id: uuid.UUID, obj_data: TaskUpdate, context: Optional[TagContextKwargs]
    ) -> Task | None:
        # Get or create tag objects
        tags = obj_data.tags
        if tags is not None:
            tag_objects = await self.tag_service.get_or_create_tags(session, tags)
        else:
            tag_objects = None

        # Update Task
        db_obj = TaskDbUpdate.model_validate(obj_data.model_dump(exclude={"tags"}))
        db_obj.tags = tag_objects

        return await super()._execute(session, obj_id, db_obj, context)


class DeleteTaskUseCase(BaseDeleteUseCase[TaskService, Task, TagContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)

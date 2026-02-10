from typing import Annotated

from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagUpdate
from app.tasks.task_tags.services import TaskTagContextKwargs, TaskTagService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetTaskTagUseCase(BaseGetUseCase[TaskTagService, TaskTag, TaskTagContextKwargs]):
    def __init__(self, service: Annotated[TaskTagService, Depends()]) -> None:
        super().__init__(service)


class GetMultiTaskTagUseCase(BaseGetMultiUseCase[TaskTagService, TaskTag, TaskTagContextKwargs]):
    def __init__(self, service: Annotated[TaskTagService, Depends()]) -> None:
        super().__init__(service)


class CreateTaskTagUseCase(BaseCreateUseCase[TaskTagService, TaskTag, TaskTagCreate, TaskTagContextKwargs]):
    def __init__(self, service: Annotated[TaskTagService, Depends()]) -> None:
        super().__init__(service)


class UpdateTaskTagUseCase(BaseUpdateUseCase[TaskTagService, TaskTag, TaskTagUpdate, TaskTagContextKwargs]):
    def __init__(self, service: Annotated[TaskTagService, Depends()]) -> None:
        super().__init__(service)


class DeleteTaskTagUseCase(BaseDeleteUseCase[TaskTagService, TaskTag, TaskTagContextKwargs]):
    def __init__(self, service: Annotated[TaskTagService, Depends()]) -> None:
        super().__init__(service)

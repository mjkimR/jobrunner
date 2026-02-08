from typing import Annotated

from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate, TaskUpdate
from app.tasks.tasks.services import BaseContextKwargs, TaskService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetTaskUseCase(BaseGetUseCase[TaskService, Task, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class GetMultiTaskUseCase(BaseGetMultiUseCase[TaskService, Task, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class CreateTaskUseCase(BaseCreateUseCase[TaskService, Task, TaskCreate, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class UpdateTaskUseCase(BaseUpdateUseCase[TaskService, Task, TaskUpdate, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)


class DeleteTaskUseCase(BaseDeleteUseCase[TaskService, Task, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskService, Depends()]) -> None:
        super().__init__(service)

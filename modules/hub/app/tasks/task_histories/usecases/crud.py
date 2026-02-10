from typing import Annotated

from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryUpdate
from app.tasks.task_histories.services import TaskHistoryContextKwargs, TaskHistoryService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetTaskHistoryUseCase(BaseGetUseCase[TaskHistoryService, TaskHistory, TaskHistoryContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class GetMultiTaskHistoryUseCase(BaseGetMultiUseCase[TaskHistoryService, TaskHistory, TaskHistoryContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class CreateTaskHistoryUseCase(
    BaseCreateUseCase[TaskHistoryService, TaskHistory, TaskHistoryCreate, TaskHistoryContextKwargs]
):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class UpdateTaskHistoryUseCase(
    BaseUpdateUseCase[TaskHistoryService, TaskHistory, TaskHistoryUpdate, TaskHistoryContextKwargs]
):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class DeleteTaskHistoryUseCase(BaseDeleteUseCase[TaskHistoryService, TaskHistory, TaskHistoryContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)

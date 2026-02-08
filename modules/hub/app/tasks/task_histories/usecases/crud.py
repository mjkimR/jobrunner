from typing import Annotated

from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryUpdate
from app.tasks.task_histories.services import BaseContextKwargs, TaskHistoryService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetTaskHistoryUseCase(BaseGetUseCase[TaskHistoryService, TaskHistory, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class GetMultiTaskHistoryUseCase(BaseGetMultiUseCase[TaskHistoryService, TaskHistory, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class CreateTaskHistoryUseCase(
    BaseCreateUseCase[TaskHistoryService, TaskHistory, TaskHistoryCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class UpdateTaskHistoryUseCase(
    BaseUpdateUseCase[TaskHistoryService, TaskHistory, TaskHistoryUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)


class DeleteTaskHistoryUseCase(BaseDeleteUseCase[TaskHistoryService, TaskHistory, BaseContextKwargs]):
    def __init__(self, service: Annotated[TaskHistoryService, Depends()]) -> None:
        super().__init__(service)

import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.repos import TaskHistoryRepository
from app.tasks.task_histories.services import TaskHistoryContextKwargs, TaskHistoryService
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetTaskHistory:
    async def test_get_task_history_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        task_history: TaskHistory = await make_db(
            TaskHistoryRepository,
            workspace_id=workspace.id,
            task_id=task.id,
            event_type="assignment",
            new_value="agent_456",
            changed_by="system_integration",
        )

        service = resolve_dependency(TaskHistoryService)

        context: TaskHistoryContextKwargs = {"parent_id": workspace.id}
        retrieved_task_history = await service.get(session, task_history.id, context=context)

        assert retrieved_task_history is not None
        assert retrieved_task_history.id == task_history.id
        assert retrieved_task_history.event_type == "assignment"

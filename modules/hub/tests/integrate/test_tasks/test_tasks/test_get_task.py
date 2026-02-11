import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.services import TaskService
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetTask:
    async def test_get_task_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(
            TaskRepository,
            workspace_id=workspace.id,
            title="Get Integration Task",
            description="To be fetched",
        )

        service = resolve_dependency(TaskService)

        retrieved_task = await service.get(session, task.id, context={"parent_id": workspace.id})

        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        assert retrieved_task.title == "Get Integration Task"

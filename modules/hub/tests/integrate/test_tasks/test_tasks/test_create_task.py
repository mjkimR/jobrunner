import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate
from app.tasks.tasks.services import TaskContextKwargs
from app.tasks.tasks.usecases.crud import CreateTaskUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateTask:
    async def test_create_task_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        use_case = resolve_dependency(CreateTaskUseCase)

        task_in = TaskCreate(
            title="Integration Task",
            description="Created via integration test with tags",
            tags=["tag1", "tag2"],
        )

        context: TaskContextKwargs = {"parent_id": workspace.id}
        # Using public API .execute()
        created_task = await use_case.execute(task_in, context=context)

        assert created_task.title == "Integration Task"
        assert created_task.description == "Created via integration test with tags"
        assert len(created_task.tags) == 2
        assert {tag.name for tag in created_task.tags} == {"tag1", "tag2"}

        # Verify in DB
        db_task = await session.get(Task, created_task.id)
        assert db_task is not None
        assert db_task.title == "Integration Task"
        assert db_task.workspace_id == workspace.id
        # Refresh to check relationships if needed, though session.get might have it cached or we need await session.refresh(db_task, ["tags"])
        await session.refresh(db_task, ["tags"])
        assert len(db_task.tags) == 2

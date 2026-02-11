import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.schemas import TaskCreate
from app.tasks.tasks.services import TaskContextKwargs, TaskService
from app.tasks.tasks.usecases.crud import CreateTaskUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestTasksIntegration:
    async def test_create_task_via_use_case(
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
        assert len(db_task.tags) == 2

    async def test_get_task_via_service(
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

    async def test_update_task_tags_via_use_case(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        initial_tag: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="initial")
        task: Task = await make_db(
            TaskRepository, workspace_id=workspace.id, title="Task with initial tag", tags=[initial_tag]
        )

        # Using UpdateTaskUseCase with automatic dependency resolution
        from app.tasks.tasks.schemas import TaskUpdate
        from app.tasks.tasks.usecases.crud import UpdateTaskUseCase

        update_use_case = resolve_dependency(UpdateTaskUseCase)

        update_data = TaskUpdate(tags=["new_tag", "another_new_tag"])
        context: TaskContextKwargs = {"parent_id": workspace.id}
        updated_task = await update_use_case.execute(task.id, update_data, context=context)

        assert updated_task is not None
        assert updated_task.title == task.title  # Should not have changed
        assert len(updated_task.tags) == 2
        assert {tag.name for tag in updated_task.tags} == {"new_tag", "another_new_tag"}

        # Verify in DB
        db_task = await session.get(Task, updated_task.id)
        await session.refresh(db_task, attribute_names=["tags"])
        assert db_task is not None
        assert len(db_task.tags) == 2
        assert {tag.name for tag in db_task.tags} == {"new_tag", "another_new_tag"}

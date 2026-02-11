import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.schemas import TaskUpdate
from app.tasks.tasks.services import TaskContextKwargs
from app.tasks.tasks.usecases.crud import UpdateTaskUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestUpdateTask:
    async def test_update_task_tags_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        initial_tag: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="initial")
        task: Task = await make_db(
            TaskRepository, workspace_id=workspace.id, title="Task with initial tag", tags=[initial_tag]
        )

        use_case = resolve_dependency(UpdateTaskUseCase)

        update_data = TaskUpdate(tags=["new_tag", "another_new_tag"])
        context: TaskContextKwargs = {"parent_id": workspace.id}

        # Using public API .execute()
        updated_task = await use_case.execute(task.id, update_data, context=context)

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

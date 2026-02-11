import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.schemas import TaskTagUpdate
from app.tasks.task_tags.services import TaskTagContextKwargs
from app.tasks.task_tags.usecases.crud import UpdateTaskTagUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestUpdateTaskTag:
    async def test_update_task_tag_success(
        self,
        session: AsyncSession,
        inspect_session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(
            TaskTagRepository, workspace_id=workspace.id, name="Old Name", color="#000000"
        )

        use_case = resolve_dependency(UpdateTaskTagUseCase)

        update_data = TaskTagUpdate(name="New Name", color="#FFFFFF")
        context: TaskTagContextKwargs = {"parent_id": workspace.id}

        updated_tag = await use_case.execute(task_tag.id, update_data, context=context)

        assert updated_tag is not None
        assert updated_tag.name == "New Name"
        assert updated_tag.color == "#FFFFFF"

        # Verify DB
        db_tag = await inspect_session.get(TaskTag, task_tag.id)
        assert db_tag is not None
        assert db_tag.name == "New Name"

    async def test_update_task_tag_duplicate_name_fails(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        await make_db(TaskTagRepository, workspace_id=workspace.id, name="Tag1")
        tag2: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="Tag2")

        use_case = resolve_dependency(UpdateTaskTagUseCase)

        # Try to rename tag2 to "Tag1" -> Should fail unique constraint
        update_data = TaskTagUpdate(name="Tag1")
        context: TaskTagContextKwargs = {"parent_id": workspace.id}

        with pytest.raises(Exception) as excinfo:
            await use_case.execute(tag2.id, update_data, context=context)

        assert "TaskTag with this name already exists" in str(excinfo.value)

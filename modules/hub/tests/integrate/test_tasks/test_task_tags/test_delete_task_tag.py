import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.services import TaskTagContextKwargs
from app.tasks.task_tags.usecases.crud import DeleteTaskTagUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestDeleteTaskTag:
    async def test_delete_task_tag_success(
        self,
        session: AsyncSession,
        inspect_session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="Tag To Delete")

        delete_use_case = resolve_dependency(DeleteTaskTagUseCase)

        context: TaskTagContextKwargs = {"parent_id": workspace.id}

        await delete_use_case.execute(task_tag.id, context=context)

        # Verify deletion
        db_tag = await inspect_session.get(TaskTag, task_tag.id)
        assert db_tag is None

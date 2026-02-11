from uuid import UUID

import pytest
from app.platform.workspaces.models import Workspace
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate
from app.tasks.task_tags.services import TaskTagService
from app.tasks.task_tags.usecases.crud import CreateTaskTagUseCase
from app_base.base.exceptions.basic import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestTaskTagsIntegration:
    async def test_create_task_tag_via_use_case(
        self,
        session: AsyncSession,
        make_db,
    ):
        # Create a workspace as parent resource
        workspace: Workspace = await make_db(Workspace)

        # Use resolve_dependency to automatically resolve dependencies
        use_case = resolve_dependency(CreateTaskTagUseCase)

        task_tag_in = TaskTagCreate(name="Integration Tag", description="Created via integration test", color="#AABBCC")

        context = {"parent_id": workspace.id}
        created_task_tag = await use_case._execute(session, task_tag_in, context=context)

        assert created_task_tag.name == "Integration Tag"
        assert created_task_tag.description == "Created via integration test"
        assert created_task_tag.color == "#AABBCC"

        # Verify in DB
        db_task_tag = await session.get(TaskTag, created_task_tag.id)
        assert db_task_tag is not None
        assert db_task_tag.name == "Integration Tag"
        assert db_task_tag.workspace_id == workspace.id

    async def test_get_task_tag_via_service(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(Workspace)
        task_tag: TaskTag = await make_db(
            TaskTag,
            workspace_id=workspace.id,
            name="Get Integration Tag",
            description="To be fetched",
            color="#CCDDEE",
        )

        service = resolve_dependency(TaskTagService)
        # Service can be used directly for simple GET operations
        retrieved_task_tag = await service.get(session, task_tag.id, context={"parent_id": workspace.id})

        assert retrieved_task_tag is not None
        assert retrieved_task_tag.id == task_tag.id
        assert retrieved_task_tag.name == "Get Integration Tag"

        # Test non-existent
        with pytest.raises(NotFoundException):
            await service.get(
                session, UUID("00000000-0000-0000-0000-000000000000"), context={"parent_id": workspace.id}
            )

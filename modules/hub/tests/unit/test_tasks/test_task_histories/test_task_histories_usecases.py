from unittest.mock import AsyncMock, MagicMock

import pytest
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryRead
from app.tasks.task_histories.services import TaskHistoryService
from app.tasks.task_histories.usecases.crud import CreateTaskHistoryUseCase


@pytest.fixture
def mock_task_history_service():
    """Fixture to provide a mocked TaskHistoryService."""
    service = AsyncMock(spec=TaskHistoryService)
    # Configure mock behavior as needed for specific test cases
    service.create.return_value = MagicMock(spec=TaskHistoryRead)
    return service


@pytest.mark.unit
class TestCreateTaskHistoryUseCase:
    async def test_create_task_history_success(self, mock_task_history_service):
        # Given
        use_case = CreateTaskHistoryUseCase(service=mock_task_history_service)
        session = AsyncMock()  # Mock session, as it's passed to _execute
        workspace_id = "123e4567-e89b-12d3-a456-426614174000"
        task_id = "123e4567-e89b-12d3-a456-426614174001"

        task_history_in = TaskHistoryCreate(
            task_id=task_id,
            event_type="status_change",
            previous_value="pending",
            new_value="in_progress",
            changed_by="unit_test",
        )
        context = {"parent_id": workspace_id}

        # Simulate the return value of service.create
        mock_task_history_service.create.return_value = TaskHistoryRead(
            id="123e4567-e89b-12d3-a456-426614174002",
            task_id=task_id,
            event_type="status_change",
            previous_value="pending",
            new_value="in_progress",
            changed_by="unit_test",
            created_at="2024-01-01T00:00:00Z",
        )

        # When
        result = await use_case._execute(session, task_history_in, context=context)

        # Then
        mock_task_history_service.create.assert_called_once_with(session, task_history_in, context=context)
        assert result.task_id == task_id
        assert result.event_type == "status_change"
        assert result.new_value == "in_progress"
        assert result.changed_by == "unit_test"

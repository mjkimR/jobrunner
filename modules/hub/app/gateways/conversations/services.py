from typing import Annotated

from app.gateways.conversations.models import Conversation
from app.gateways.conversations.repos import ConversationRepository
from app.gateways.conversations.schemas import ConversationCreate, ConversationUpdate
from app.platform.workspaces.repos import WorkspaceRepository
from app_base.base.services.base import (
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app_base.base.services.exists_check_hook import ExistsCheckHooksMixin
from app_base.base.services.nested_resource_hook import NestedResourceContextKwargs, NestedResourceHooksMixin
from fastapi import Depends


class ConversationContextKwargs(NestedResourceContextKwargs):
    pass


class ConversationService(
    NestedResourceHooksMixin,  # Relationship with Workspace
    ExistsCheckHooksMixin,  # Ensure existence checks before operations
    BaseCreateServiceMixin[ConversationRepository, Conversation, ConversationCreate, ConversationContextKwargs],
    BaseGetMultiServiceMixin[ConversationRepository, Conversation, ConversationContextKwargs],
    BaseGetServiceMixin[ConversationRepository, Conversation, ConversationContextKwargs],
    BaseUpdateServiceMixin[ConversationRepository, Conversation, ConversationUpdate, ConversationContextKwargs],
    BaseDeleteServiceMixin[ConversationRepository, Conversation, ConversationContextKwargs],
):
    def __init__(
        self,
        repo: Annotated[ConversationRepository, Depends()],
        repo_workspace: Annotated[WorkspaceRepository, Depends()],
    ):
        self._repo = repo
        self._parent_repo = repo_workspace

    @property
    def repo(self) -> ConversationRepository:
        return self._repo

    @property
    def parent_repo(self) -> WorkspaceRepository:
        return self._parent_repo

    @property
    def context_model(self):
        return ConversationContextKwargs

    @property
    def fk_name(self) -> str:
        return "workspace_id"

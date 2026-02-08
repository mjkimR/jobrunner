from typing import Annotated

from app.agents.agent_skills.models import AgentSkill
from app.agents.agent_skills.repos import AgentSkillRepository
from app.agents.agent_skills.schemas import AgentSkillCreate, AgentSkillUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AgentSkillService(
    BaseCreateServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[AgentSkillRepository, AgentSkill, BaseContextKwargs],
    BaseGetServiceMixin[AgentSkillRepository, AgentSkill, BaseContextKwargs],
    BaseUpdateServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[AgentSkillRepository, AgentSkill, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[AgentSkillRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AgentSkillRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs

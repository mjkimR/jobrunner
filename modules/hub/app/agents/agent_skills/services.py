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


class AgentSkillContextKwargs(BaseContextKwargs):
    pass


class AgentSkillService(
    BaseCreateServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillCreate, AgentSkillContextKwargs],
    BaseGetMultiServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillContextKwargs],
    BaseGetServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillContextKwargs],
    BaseUpdateServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillUpdate, AgentSkillContextKwargs],
    BaseDeleteServiceMixin[AgentSkillRepository, AgentSkill, AgentSkillContextKwargs],
):
    def __init__(self, repo: Annotated[AgentSkillRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AgentSkillRepository:
        return self._repo

    @property
    def context_model(self):
        return AgentSkillContextKwargs

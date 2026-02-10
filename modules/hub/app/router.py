from typing import Annotated

from app.agents.agent_executions.api.v1 import router as v1_agent_executions_router
from app.agents.agent_mcps.api.v1 import router as v1_agent_mcps_router
from app.agents.agent_skills.api.v1 import router as v1_agent_skills_router
from app.agents.ai_model_catalogs.api.v1 import router as v1_ai_models_router
from app.agents.configured_agents.api.v1 import router as v1_configured_agents_router
from app.gateways.conversations.api.v1 import router as v1_conversations_router
from app.gateways.routing_logs.api.v1 import router as v1_routing_logs_router
from app.gateways.user_messages.api.v1 import router as v1_user_messages_router
from app.platform.workspaces.api.v1 import router as v1_workspaces_router
from app.tasks.task_histories.api.v1 import router as v1_task_histories_router
from app.tasks.task_tags.api.v1 import router as v1_task_tags_router
from app.tasks.tasks.api.v1 import router as v1_tasks_router
from app_base.core.database.deps import get_session
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api")
v1_router = APIRouter(prefix="/v1")


@router.get("/health", status_code=204)
async def health():
    return Response(status_code=204)


@router.get("/health/deep", status_code=status.HTTP_200_OK)
async def deep_health_check(session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception:
        return Response(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content="Database connection failed",
        )


# Feature routers
v1_router.include_router(v1_tasks_router)
v1_router.include_router(v1_task_tags_router)
v1_router.include_router(v1_task_histories_router)
v1_router.include_router(v1_ai_models_router)
v1_router.include_router(v1_configured_agents_router)
v1_router.include_router(v1_agent_skills_router)
v1_router.include_router(v1_agent_mcps_router)
v1_router.include_router(v1_agent_executions_router)
v1_router.include_router(v1_conversations_router)
v1_router.include_router(v1_user_messages_router)
v1_router.include_router(v1_routing_logs_router)
v1_router.include_router(v1_workspaces_router)
router.include_router(v1_router)

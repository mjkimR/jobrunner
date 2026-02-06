from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.scheduler.usecases.tick import TickUseCase
from app_base.core.database.deps import get_session


def get_tick_usecase(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> TickUseCase:
    return TickUseCase(session=session)

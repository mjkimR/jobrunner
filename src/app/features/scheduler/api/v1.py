from fastapi import APIRouter, Depends

from app.features.scheduler.deps import get_tick_usecase
from app.features.scheduler.schemas import TickRequest, TickResponse
from app.features.scheduler.usecases.tick import TickUseCase

router = APIRouter(prefix="/tick", tags=["Scheduler"], dependencies=[])


@router.post("", response_model=TickResponse)
async def tick(
    body: TickRequest,
    usecase: TickUseCase = Depends(get_tick_usecase),
):
    return await usecase.execute(now=body.now, limit=body.limit)

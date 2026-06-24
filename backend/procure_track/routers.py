from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from procure_track.schemas import (
    OrderCreateRequest,
    OrderResponse
)
from core.database import get_db_session
from procure_track import service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/create_order", response_model=OrderResponse, status_code=201)
async def create_task(
    order: OrderCreateRequest,
    db: AsyncSession = Depends(get_db_session)
):
    return await service.create_order(new_db=db, order_data=order)

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from procure_track.schemas import (
    OrderCreateRequest,
    OrderCreateResponse,
    CompanyComparisonResponse,
    CompanySummaryResponse,
    ProductSummaryResponse,
    StatusSummaryResponse,
    DelayedDeliveriesResponse,
    PendingPaymentsReponse,
    DetailedOrdersResponse
)
from core.database import get_db_session
from procure_track import service, data_loader

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/create_order", response_model=OrderCreateResponse, status_code=201)
async def create_task(
    order: OrderCreateRequest,
    db: AsyncSession = Depends(get_db_session)
):
    return await service.create_order(new_db=db, order_data=order)

@router.post("/create_all_orders", response_model=list[OrderCreateResponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.create_all_orders(new_db=db, order_data=data_loader.get_all_orders())

@router.get("/get_comparison_data/{sort_by}", response_model=list[CompanyComparisonResponse], status_code=201)
async def create_task(
    sort_by: service.CompanySortingCategories,
    db: AsyncSession = Depends(get_db_session)
):
    print(sort_by)
    return await service.get_company_comparison_data(new_db=db, sort_by_input=sort_by)


@router.get("/get_company_summary", response_model=list[CompanySummaryResponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_company_summary(new_db=db)

@router.get("/get_product_summary", response_model=list[ProductSummaryResponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_product_summary(new_db=db)

@router.get("/get_status_summary", response_model=list[StatusSummaryResponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_status_summary(new_db=db)

@router.get("/get_delayed_deliveries", response_model=list[DelayedDeliveriesResponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_delayed_deliveries(new_db=db)

@router.get("/get_pending_payments", response_model=list[PendingPaymentsReponse], status_code=201)
async def create_task(
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_pending_payments(new_db=db)

# @router.get("/get_detailed_orders/{sort_by}", response_model=list[DetailedOrdersResponse], status_code=201)
# async def create_task(
#     sort_by: service.OrderSortingCategories,
#     db: AsyncSession = Depends(get_db_session)
# ):
#     return await service.get_detailed_orders(new_db=db, sort_by_input=sort_by)

@router.get("/get_detailed_orders/{sort_by}/{search_by}/{search_value}", response_model=list[DetailedOrdersResponse], status_code=201)
async def create_task(
    sort_by: service.OrderSortingCategories,
    search_by: service.SearchCritera,
    search_value: str | int,
    db: AsyncSession = Depends(get_db_session)
):
    return await service.get_detailed_orders(new_db=db, sort_by_input=sort_by, search_by_input=search_by, search_by_value=search_value)

from procure_track.repository import OrderRepository
from procure_track.schemas import OrderCreateRequest
from fastapi import HTTPException
from procure_track.models import Order
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, date
from enum import Enum

class SearchCritera(str, Enum):
    company_name = "company_name"
    product_name = "product_name"
    po_no = "po_no"
    tender_ref_no = "tender_ref_no"

class CompanySortingCategories(str, Enum):
        total_po_value = "total_po_value"
        pending_invoice_value = "pending_invoice_value"
        pending_qty = "pending_invoice_qty"
        delayed_deliveries_count = "delayed_deliveries_count"
        payments_pending_count = "payments_pending_count"

class OrderSortingCategories(str, Enum):

        company_name = "company_name"
        po_date = "po_date"
        po_value = "po_value"
        invoice_value = "invoice_value"
        pending_invoice_value = "pending_invoice_value"
        pending_qty = "pending_invoice_qty"
        remaining_days = "remaining_days"
        status = "status"


orderRepository = OrderRepository()

def sort_companies(comparison_data: list[dict], sort_by: CompanySortingCategories):
    return sorted(
        comparison_data,
        key=lambda row: row.get(sort_by.value, 0) if row.get(sort_by.value) is not None else 0,
        reverse=True,
    )[:10]
    
def sort_orders(comparison_data: list[dict], sort_by: OrderSortingCategories):
    value = sort_by.value

    filtered_data = [row for row in comparison_data if (row.get(value) is not None and row.get(value) != "0")]

    def sort_key(row):
        row_value = row.get(value)
        if isinstance(row_value, str):
            return row_value.lower()
        return row_value

    return sorted(
        filtered_data,
        key=sort_key,
        reverse= sort_by is not OrderSortingCategories.company_name,
    )
            



async def create_order(new_db: AsyncSession, order_data: OrderCreateRequest):
    new_order = Order(
        tender_ref_no=order_data.tender_ref_no,
        placebo_required=order_data.placebo_required,

        product_code=order_data.product_code,
        product_name=order_data.product_name,

        company_name=order_data.company_name,

        po_no=order_data.po_no,
        po_date=order_data.po_date,
        po_quantity=order_data.po_quantity,
        po_value=order_data.po_value,

        invoice_qty=order_data.invoice_qty,
        invoice_value=order_data.invoice_value,

        pending_invoice_qty=order_data.pending_invoice_qty,
        pending_invoice_value=order_data.pending_invoice_value,

        schedule_date=order_data.schedule_date,
        remaining_days=order_data.remaining_days,
        status=order_data.status,

        payment_sanction_date=order_data.payment_sanction_date,
    )

    created_order = await orderRepository.create_order(db=new_db, order=new_order)
    return created_order

async def create_all_orders(new_db: AsyncSession, order_data: list[OrderCreateRequest]):
    all_orders = [
        Order(
            tender_ref_no=data.tender_ref_no,
            placebo_required=data.placebo_required,

            product_code=data.product_code,
            product_name=data.product_name,

            company_name=data.company_name,

            po_no=data.po_no,
            po_date=data.po_date,
            po_quantity=data.po_quantity,
            po_value=data.po_value,

            invoice_qty=data.invoice_qty,
            invoice_value=data.invoice_value,

            pending_invoice_qty=data.pending_invoice_qty,
            pending_invoice_value=data.pending_invoice_value,

            schedule_date=data.schedule_date,
            remaining_days=data.remaining_days,
            status=data.status,

            payment_sanction_date=data.payment_sanction_date,
        )
        for data in order_data
    ]

    created_order = await orderRepository.create_all_orders(db=new_db, orders=all_orders)
    return all_orders

async def get_company_comparison_data(new_db: AsyncSession, sort_by_input: CompanySortingCategories):
        
        data = await orderRepository.get_company_comparison_data(db=new_db)
        
        sortedValues = sort_companies(comparison_data=data, sort_by=sort_by_input)
        
        return sortedValues

async def get_company_summary(new_db: AsyncSession):
    
    data = await orderRepository.get_company_summary(db=new_db)
    
    return data

async def get_status_summary(new_db: AsyncSession):
    
    data = await orderRepository.get_status_summary(db=new_db)
    
    return data

async def get_product_summary(new_db: AsyncSession):
    
    data = await orderRepository.get_product_summary(db=new_db)
    
    return data

async def get_delayed_deliveries(new_db: AsyncSession):
    
    data = await orderRepository.get_delayed_deliveries(db=new_db)
    
    return data

async def get_pending_payments(new_db: AsyncSession):
    
    data = await orderRepository.get_pending_payments(db=new_db)
    
    return data

# async def get_detailed_orders(new_db: AsyncSession, sort_by_input: OrderSortingCategories):
    
#     data = await orderRepository.get_detailed_orders(db=new_db)
    
#     sortedValues = sort_orders(comparison_data=data, sort_by=sort_by_input)
    
#     return sortedValues

async def get_detailed_orders(new_db: AsyncSession, search_by_input: SearchCritera, search_by_value: str | int, sort_by_input: OrderSortingCategories):
    
    data = await orderRepository.get_detailed_orders(db=new_db, search_by=search_by_input, search_value=search_by_value)
    
    sortedValues = sort_orders(comparison_data=data, sort_by=sort_by_input)
    
    return sortedValues
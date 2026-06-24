from procure_track.repository import OrderRepository
from procure_track.schemas import OrderCreateRequest, OrderResponse
from fastapi import HTTPException
from procure_track.models import Order
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, date



orderRepository = OrderRepository()

async def create_order(new_db: AsyncSession, order_data: OrderCreateRequest):
        print("Order data: ", order_data)

        new_order = Order(
                tender_ref_no= order_data.tender_ref_no,
                tender_quantity = order_data.tender_quantity,
                loa_percent = order_data.loa_percent,
                approve_rate = order_data.approve_rate,
                placebo_required = order_data.placebo_required,

                product_code = order_data.product_code,
                product_name = order_data.product_name,
                hsn_code = order_data.hsn_code,
                packing_size = order_data.packing_size,
                shelf_life_months = order_data.shelf_life_months,

                company_name = order_data.company_name,
                tax_rate = order_data.tax_rate,

                po_no = order_data.po_no,
                po_date = order_data.po_date,
                po_quantity = order_data.po_quantity,
                drug_value = order_data.drug_value,
                po_value = order_data.po_value,

                invoice_qty = order_data.invoice_qty,
                invoice_value = order_data.invoice_value,

                pending_invoice_qty = order_data.pending_invoice_qty,
                pending_invoice_value = order_data.pending_invoice_value,
                active_quantity_spdr = order_data.active_quantity_spdr,

                schedule_days = order_data.schedule_days,
                schedule_date = order_data.schedule_date,
                remaining_days = order_data.remaining_days,
                status = order_data.status,

                invoice_submission_date = order_data.invoice_submission_date,
                payment_sanction_date = order_data.payment_sanction_date,
                amount_passed = order_data.amount_passed,
                outstanding_to_rmscl = order_data.outstanding_to_rmscl,

                file_no = order_data.file_no,
                remarks = order_data.remarks,

                supply_percent = order_data.supply_percent,
        )

        created_order = await orderRepository.create_order(db=new_db, order=order_data)
        return created_order

from procure_track.models import Order
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class OrderRepository():

    async def create_order(self, db: AsyncSession, order: Order):
        try:
            new_order = Order(
                tender_ref_no=order.tender_ref_no,
                placebo_required=order.placebo_required,

                product_code=order.product_code,
                product_name=order.product_name,

                company_name=order.company_name,

                po_no=order.po_no,
                po_date=order.po_date,
                po_quantity=order.po_quantity,
                po_value=order.po_value,

                invoice_qty=order.invoice_qty,
                invoice_value=order.invoice_value,

                pending_invoice_qty=order.pending_invoice_qty,
                pending_invoice_value=order.pending_invoice_value,

                schedule_date=order.schedule_date,
                remaining_days=order.remaining_days,
                status=order.status,

                payment_sanction_date=order.payment_sanction_date,
            )

            db.add(new_order)
            await db.commit()
            await db.refresh(new_order)

            return new_order
        
        except Exception as e:
            await db.rollback()
            raise e
    
    async def create_all_orders(self, db: AsyncSession, orders: list[Order]):
        
        try:

            order_values = [
                Order(
                    tender_ref_no=order.tender_ref_no,
                    placebo_required=order.placebo_required,

                    product_code=order.product_code,
                    product_name=order.product_name,

                    company_name=order.company_name,

                    po_no=order.po_no,
                    po_date=order.po_date,
                    po_quantity=order.po_quantity,
                    po_value=order.po_value,

                    invoice_qty=order.invoice_qty,
                    invoice_value=order.invoice_value,

                    pending_invoice_qty=order.pending_invoice_qty,
                    pending_invoice_value=order.pending_invoice_value,

                    schedule_date=order.schedule_date,
                    remaining_days=order.remaining_days,
                    status=order.status,

                    payment_sanction_date=order.payment_sanction_date,
                )
                for order in orders
            ]

            db.add_all(order_values)
            await db.commit()
            for value in order_values:
                await db.refresh(value)
            return order_values
        
        except Exception as e:
            await db.rollback()
            raise e
    
    async def get_company_comparison_data(self, db: AsyncSession):
        
        try:
            result = await db.execute(
                select(
                    Order.company_name,
                    Order.po_value,
                    Order.invoice_value,
                    Order.pending_invoice_value,
                    Order.pending_invoice_qty,
                    Order.po_quantity,
                    Order.remaining_days,
                    Order.status,
                )
            )

            # Use mappings() to get dictionary-like rows so Pydantic can validate
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
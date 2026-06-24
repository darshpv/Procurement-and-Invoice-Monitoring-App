from procure_track.models import Order
from sqlalchemy.ext.asyncio import AsyncSession


class OrderRepository():

    async def create_order(self, db: AsyncSession, order: Order):
        try:
            new_order = Order(
                tender_ref_no= order.tender_ref_no,
                tender_quantity = order.tender_quantity,
                loa_percent = order.loa_percent,
                approve_rate = order.approve_rate,
                placebo_required = order.placebo_required,

                product_code = order.product_code,
                product_name = order.product_name,
                hsn_code = order.hsn_code,
                packing_size = order.packing_size,
                shelf_life_months = order.shelf_life_months,

                company_name = order.company_name,
                tax_rate = order.tax_rate,

                po_no = order.po_no,
                po_date = order.po_date,
                po_quantity = order.po_quantity,
                drug_value = order.drug_value,
                po_value = order.po_value,

                invoice_qty = order.invoice_qty,
                invoice_value = order.invoice_value,

                pending_invoice_qty = order.pending_invoice_qty,
                pending_invoice_value = order.pending_invoice_value,
                active_quantity_spdr = order.active_quantity_spdr,

                schedule_days = order.schedule_days,
                schedule_date = order.schedule_date,
                remaining_days = order.remaining_days,
                status = order.status,

                invoice_submission_date = order.invoice_submission_date,
                payment_sanction_date = order.payment_sanction_date,
                amount_passed = order.amount_passed,
                outstanding_to_rmscl = order.outstanding_to_rmscl,

                file_no = order.file_no,
                remarks = order.remarks,

                supply_percent = order.supply_percent,
            )

            db.add(new_order)
            await db.commit()
            await db.refresh(new_order)

            return new_order
        
        except Exception as e:
            await db.rollback()
            raise e
    
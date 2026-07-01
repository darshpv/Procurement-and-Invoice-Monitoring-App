from procure_track.models import Order
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, case, String
from enum import Enum

 

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
                    func.sum(Order.invoice_value).label("total_invoice_value"),
                    func.sum(Order.po_value).label("total_po_value"),
                    func.sum(Order.pending_invoice_value).label("pending_invoice_value"),
                    func.sum(Order.pending_invoice_qty).label("pending_invoice_qty"),
                    func.sum(
                        case(
                                (
                                    (Order.pending_invoice_qty > 0) &
                                    (Order.remaining_days < 0) &
                                    (Order.status != "P O Closed"),
                                    1
                                ),
                            else_=0
                        )
                    ).label("delayed_deliveries_count"),
                    func.sum(
                        case(
                                (
                                    (Order.pending_invoice_qty > 0),
                                    1
                                ),
                            else_=0
                        )
                    ).label("payments_pending_count"),

                ).group_by(Order.company_name)
            )
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
        
    async def get_company_summary(self, db: AsyncSession):   
        
        try:
            result = await db.execute(
                select(
                    Order.company_name,
                    func.sum(Order.invoice_value).label("total_invoice_value"),
                    func.sum(Order.po_value).label("total_po_value"),
                    func.sum(Order.pending_invoice_value).label("pending_invoice_value"),
                    func.sum(Order.pending_invoice_qty).label("pending_invoice_qty"),
                    func.sum(
                        case(
                                (
                                    (Order.pending_invoice_qty > 0) &
                                    (Order.remaining_days < 0) &
                                    (Order.status != "P O Closed"),
                                    1
                                ),
                            else_=0
                        )
                    ).label("delayed_deliveries_count"),
                    func.sum(
                        case(
                                (
                                    (Order.pending_invoice_qty > 0),
                                    1
                                ),
                            else_=0
                        )
                    ).label("payments_pending_count"),
                    func.coalesce(
                        func.sum(Order.invoice_qty) / func.nullif(func.sum(Order.po_quantity), 0),
                        0
                    ).label("supply_percentage")
                ).group_by(Order.company_name)
            )

            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
       
    async def get_product_summary(self, db: AsyncSession):
        try:
            
            result = await db.execute(
                select(
                    Order.product_name,
                    func.sum(Order.po_quantity).label("total_po_qty"),
                    func.sum(Order.po_value).label("total_po_value"),
                    func.sum(Order.invoice_qty).label("total_invoice_qty"),
                    func.sum(Order.pending_invoice_qty).label("pending_invoice_qty"),
                    func.sum(Order.invoice_value).label("total_invoice_value"),
                    func.sum(Order.pending_invoice_value).label("pending_invoice_value"),
                    func.sum(
                        case(
                                (
                                    (Order.pending_invoice_qty > 0) &
                                    (Order.remaining_days < 0) &
                                    (Order.status != "P O Closed"),
                                    1
                                ),
                            else_=0
                        )
                    ).label("delayed_deliveries_count"),
                ).group_by(Order.product_name)
            )
            
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
        
    async def get_status_summary(self, db: AsyncSession):
        
        try:
            result = await db.execute(
                select(
                    func.sum(
                        case(
                            (
                                (Order.status == "Bill Submit"),
                                1
                            ),
                            else_=0
                        )
                    ).label("bill_submit"),
                    func.sum(
                        case(
                            (
                                (Order.status == "Bill Process"),
                                1
                            ),
                            else_=0
                        )
                    ).label("bill_process"),
                    func.sum(
                        case(
                            (
                                (Order.status == "P O Closed"),
                                1
                            ),
                            else_=0
                        )
                    ).label("po_closed"),
                    func.sum(
                        case(
                            (
                                (Order.status == "L D 0%"),
                                1
                            ),
                            else_=0
                        )
                    ).label("ld_0"),
                    func.sum(
                        case(
                            (
                                (Order.status == "L D 5.0%"),
                                1
                            ),
                            else_=0
                        )
                    ).label("ld_5"),
                    func.sum(
                        case(
                            (
                                (Order.status == "L D 10%"),
                                1
                            ),
                            else_=0
                        )
                    ).label("ld_10"),
                    func.sum(
                        case(
                            (
                                (Order.status == "L D 7.5%"),
                                1
                            ),
                            else_=0
                        )
                    ).label("ld_7_5"),
                )
            )

            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
                
    async def get_delayed_deliveries(self, db: AsyncSession):
        
        try:
            
            result = await db.execute(
                select(
                    Order.company_name,
                    Order.product_name,
                    Order.po_no,
                    Order.schedule_date,
                    Order.remaining_days,
                    Order.pending_invoice_qty,
                    Order.pending_invoice_value
                ).where(
                    (Order.pending_invoice_qty > 0) &
                    (Order.remaining_days < 0) &
                    (Order.status != "P O Closed")
                )
            )
            
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
    
    async def get_pending_payments(self, db: AsyncSession):
        
        try:
            
            result = await db.execute(
                select(
                    Order.company_name,
                    Order.po_no,
                    Order.invoice_value,
                    Order.pending_invoice_value,
                    Order.payment_sanction_date
                ).where(
                    Order.pending_invoice_qty > 0
                )
            )
            
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e   
    
    # async def get_detailed_orders(self, db: AsyncSession):
        
    #     try:
            
    #         result = await db.execute(
    #             select(
    #                 Order.tender_ref_no,
    #                 Order.product_name,
    #                 Order.company_name,
    #                 Order.po_no,
    #                 Order.po_date,
    #                 Order.po_quantity,
    #                 Order.po_value,
    #                 Order.invoice_qty,
    #                 Order.invoice_value,
    #                 Order.pending_invoice_qty,
    #                 Order.pending_invoice_value,
    #                 Order.schedule_date,
    #                 Order.remaining_days,
    #                 Order.status,
    #                 Order.payment_sanction_date
    #             )
    #         )
            
    #         mappings = result.mappings().all()
    #         return [dict(row) for row in mappings]
        
    #     except Exception as e:
    #         await db.rollback()
    #         raise e       
        
    async def get_detailed_orders(self, db: AsyncSession, search_by: str, search_value: str | int):
        column = getattr(Order, search_by)
        
        
            
        
        try:
            
            if search_value == "load_all":
                result = await db.execute(
                    select(
                        Order.tender_ref_no,
                        Order.product_name,
                        Order.company_name,
                        Order.po_no,
                        Order.po_date,
                        Order.po_quantity,
                        Order.po_value,
                        Order.invoice_qty,
                        Order.invoice_value,
                        Order.pending_invoice_qty,
                        Order.pending_invoice_value,
                        Order.schedule_date,
                        Order.remaining_days,
                        Order.status,
                        Order.payment_sanction_date
                    )
                )
            
            elif isinstance(column.type, String):
                result = await db.execute(
                    select(
                        Order.tender_ref_no,
                        Order.product_name,
                        Order.company_name,
                        Order.po_no,
                        Order.po_date,
                        Order.po_quantity,
                        Order.po_value,
                        Order.invoice_qty,
                        Order.invoice_value,
                        Order.pending_invoice_qty,
                        Order.pending_invoice_value,
                        Order.schedule_date,
                        Order.remaining_days,
                        Order.status,
                        Order.payment_sanction_date
                    ).where(
                        column.ilike(f"%{search_value}%")
                    )
                )
            else:
                result = await db.execute(
                    select(
                        Order.tender_ref_no,
                        Order.product_name,
                        Order.company_name,
                        Order.po_no,
                        Order.po_date,
                        Order.po_quantity,
                        Order.po_value,
                        Order.invoice_qty,
                        Order.invoice_value,
                        Order.pending_invoice_qty,
                        Order.pending_invoice_value,
                        Order.schedule_date,
                        Order.remaining_days,
                        Order.status,
                        Order.payment_sanction_date
                    ).where(
                        column == int(search_value)
                    )
                )
        
            mappings = result.mappings().all()
            return [dict(row) for row in mappings]
        
        except Exception as e:
            await db.rollback()
            raise e
       
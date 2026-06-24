from core.database import Base
from enum import Enum
from sqlalchemy import Column, Numeric, String, Integer, Boolean, Float, Enum as SQLAlchemyEnum, Date

class PO_Status(str, Enum):
    PO_CLOSED = "PO Closed"
    BILL_PROCESS = "Bill Process" 


class Order(Base):
    __tablename__ = "orders"

    #  Tender Info
    tender_ref_no = Column(String, primary_key=True)
    tender_quantity = Column(Integer)
    loa_percent = Column(Integer)
    approve_rate = Column(Float)
    placebo_required = Column(Boolean)

    #  Product Info
    product_code = Column(String)
    product_name = Column(String)
    hsn_code = Column(String)
    packing_size = Column(String)
    shelf_life_months = Column(Integer)

    #  Company Info
    company_name = Column(String)
    tax_rate = Column(Float)

    #  Purchase Order (PO)
    po_no = Column(Integer)
    po_date = Column(Date)
    po_quantity = Column(Integer)
    drug_value = Column(Integer)
    po_value = Column(Integer)

    #  Invoice Info
    invoice_qty = Column(Integer)
    invoice_value = Column(Integer)

    #  Pending / Calculated
    pending_invoice_qty = Column(Integer)
    pending_invoice_value = Column(Integer)
    active_quantity_spdr = Column(Integer)

    #  Delivery & Schedule
    schedule_days = Column(Integer)
    schedule_date = Column(Date)
    remaining_days = Column(Integer)
    status = Column(SQLAlchemyEnum(PO_Status))

    #  Payment Info
    invoice_submission_date = Column(Date)
    payment_sanction_date = Column(Date)
    amount_passed = Column(Integer)
    outstanding_to_rmscl = Column(Integer)

    #  File / Tracking
    file_no = Column(Integer)
    remarks = Column(String)
    
    #  Metrics
    supply_percent = Column(Float)

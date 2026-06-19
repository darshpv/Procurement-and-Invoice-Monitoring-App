from core.database import Base
from enum import Enum
from sqlalchemy import Column, String, Integer, Boolean, Float, Enum as SQLAlchemyEnum, ForeignKey, Date

class PO_Status(str, Enum):
    PO_CLOSED = "PO Closed"
    BILL_PROCESS = "Bill Process" 


class Tender(Base):
    __tablename__ = "tenders"
    id =  Column(String, primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    LOA_percent = Column(Integer, nullable=False)
    approve_rate = Column(Float(precision=2), nullable=False)
    placebo_required = Column(Boolean, nullable=False)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    hsn_code = Column(Integer, nullable=False)
    packing_size = Column(String, nullable=False)
    shelf_life_months = Column(Integer, nullable=False)

class Tender_items(Base):
    __tablename__ = "tender_items"
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(String, ForeignKey(Tender.id))
    product_id = Column(Integer, ForeignKey(Product.id))

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Purchase_order(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True)
    tender_id = Column(String, ForeignKey(Tender.id))
    company_id = Column(Integer, ForeignKey(Company.id))
    date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    drug_value = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    schedule_days = Column(Integer, nullable=False)
    schedule_date = Column(Date, nullable=False)
    status = Column(SQLAlchemyEnum(PO_Status), nullable=False)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    po_id = Column(Integer, ForeignKey(Purchase_order.id))
    quantity = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    submission_date = Column(Date, nullable=False)
    sum = Column(Integer, nullable=False)
    amount_passed = Column(Integer, nullable=False)


class Delivery_status(Base):
    __tablename__ = "delivery_statuses"
    id = Column(Integer, primary_key=True, nullable=False)
    po_id = Column(Integer, ForeignKey(Purchase_order.id))
    pending_invoice_quantity = Column(Integer, nullable=False)
    pending_invoice_value = Column(Integer, nullable=False)
    remaining_days = Column(Integer, nullable=False)
    active_quantity_spdr = Column(Integer, nullable=False)
    supply_percent = Column(Integer, nullable=False)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey(Purchase_order.id))
    payment_sanction_date = Column(Date, nullable=False)
    outstanding_to_rmscl = Column(Integer, nullable=False)
    difference_value = Column(Integer, nullable=False)

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    po_id = Column(Integer, ForeignKey(Purchase_order.id))
    remarks = Column(String, nullable=False)
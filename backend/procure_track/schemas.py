from pydantic import BaseModel
from datetime import date

class OrderCreateRequest(BaseModel):

    tender_ref_no: str
    placebo_required: bool

    product_code: str
    product_name: str

    company_name: str

    po_no: int
    po_date: date
    po_quantity: int
    po_value: int

    invoice_qty: int
    invoice_value: int

    pending_invoice_qty: int
    pending_invoice_value: int

    schedule_date: date
    remaining_days: int
    status: str

    payment_sanction_date: date

class OrderCreateResponse(BaseModel):
    tender_ref_no: str
    product_code: str
    company_name: str

class CompanyComparisonResponse(BaseModel):
    company_name: str
    po_value: int
    invoice_value: int
    pending_invoice_value: int
    pending_invoice_qty: int
    po_quantity: int
    remaining_days: int
    status: str
    
    

class OrderResponse(BaseModel):

    tender_ref_no: str
    placebo_required: bool

    product_code: str
    product_name: str

    company_name: str

    po_no: int
    po_date: date
    po_quantity: int
    po_value: int

    invoice_qty: int
    invoice_value: int

    pending_invoice_qty: int
    pending_invoice_value: int

    schedule_date: date
    remaining_days: int
    status: str
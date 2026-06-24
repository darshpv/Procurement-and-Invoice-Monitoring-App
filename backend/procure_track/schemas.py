from pydantic import BaseModel
from datetime import date

class OrderCreateRequest(BaseModel):

    tender_ref_no:str
    tender_quantity: int
    loa_percent: float
    approve_rate:  float
    placebo_required: bool

    product_code:str
    product_name:str
    hsn_code:str
    packing_size:str
    shelf_life_months: int

    company_name:str
    tax_rate:  float

    po_no: int
    po_date:  date
    po_quantity: int
    drug_value: int
    po_value: int

    invoice_qty: int
    invoice_value: int

    pending_invoice_qty: int
    pending_invoice_value: int
    active_quantity_spdr: int

    schedule_days: int
    schedule_date:  date
    remaining_days: int
    status: str

    invoice_submission_date: date
    payment_sanction_date: date
    amount_passed: int
    outstanding_to_rmscl: int

    file_no: int
    remarks: str

    supply_percent:  float

class OrderResponse(BaseModel):

    tender_ref_no: str
    tender_quantity: int
    loa_percent: float
    approve_rate: float
    placebo_required: bool

    product_code: str
    product_name: str
    hsn_code: str
    packing_size: str
    shelf_life_months: int

    company_name: str
    tax_rate: float

    po_no: int
    po_date: date
    po_quantity: int
    drug_value: int
    po_value: int

    invoice_qty: int
    invoice_value: int

    pending_invoice_qty: int
    pending_invoice_value: int
    active_quantity_spdr: int

    schedule_days: int
    schedule_date: date
    remaining_days: int
    status: str

    invoice_submission_date:  date
    payment_sanction_date:  date
    amount_passed: int
    outstanding_to_rmscl: int

    file_no: int
    remarks: str

    supply_percent: float
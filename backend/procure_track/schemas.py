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
    total_po_value: int
    total_invoice_value: int
    pending_invoice_value: int
    pending_invoice_qty: int
    delayed_deliveries_count: int
    payments_pending_count: int

    
class CompanySummaryResponse(BaseModel):
    company_name: str
    total_invoice_value: int
    total_po_value: int
    pending_invoice_value: int
    pending_invoice_qty: int
    delayed_deliveries_count: int
    payments_pending_count: int
    supply_percentage: float

class ProductSummaryResponse(BaseModel):
    product_name: str
    total_po_qty: int
    total_invoice_qty: int
    pending_invoice_qty: int
    total_po_value: int
    total_invoice_value: int
    pending_invoice_value: int
    delayed_deliveries_count: int

class StatusSummaryResponse(BaseModel):
    po_closed: int
    bill_process: int
    bill_submit: int
    ld_0: int
    ld_5: int
    ld_7_5: int
    ld_10: int
    
class DelayedDeliveriesResponse(BaseModel):
    company_name: str
    product_name: str
    po_no: int
    schedule_date: date
    remaining_days: int
    pending_invoice_qty: int
    pending_invoice_value: int
    
class PendingPaymentsReponse(BaseModel):
    company_name: str
    po_no: int
    invoice_value: int
    pending_invoice_value: int
    payment_sanction_date: date

class DetailedOrdersResponse(BaseModel):
    tender_ref_no: str
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

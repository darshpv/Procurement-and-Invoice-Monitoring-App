from datetime import date
import pandas as pd
from procure_track.models import PO_Status
from procure_track.schemas import OrderCreateRequest
from procure_track import service
from core.database import SessionLocal
import asyncio


excel_file = pd.ExcelFile(r"C:\Users\darsh.chaudhary\procurement-and-invoice-monitoring-app\backend\work_data.xlsx")

df = pd.read_excel(excel_file, sheet_name="All Orders")
df.columns = df.columns.str.strip()  # remove whitespace from headers
row = df.iloc[2]


def scalar(value):
    if pd.isna(value):
        return None
    return value

def parse_bool(value):
    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return False
    if value == "Yes":
        return True
    if value == "No":
        return False
    else:
        raise ValueError(f"Unknown value: {value}")

def parse_date(value):
    if pd.isna(value):
        return None
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    return pd.to_datetime(value).date()

def parse_status(value):
    if isinstance(value, PO_Status):
        return value
    text = str(value).strip()
    if text == "PO Closed":
        return PO_Status.PO_CLOSED
    if text == "Bill Process":
        return PO_Status.BILL_PROCESS
    raise ValueError(f"Unknown status: {value}")


row_data = {
    "tender_ref_no": str(scalar(row["Tender Ref. No."])),
    "tender_quantity": int(scalar(row["Tender Quantity"])),
    "loa_percent": int(scalar(row["L O A %"])),
    "approve_rate": float(scalar(row["Approve Rate"])),
    "placebo_required": parse_bool(row["Placebo Required (Yes/No)"]),
    "product_code": str(scalar(row["Product Code"])),
    "product_name": str(scalar(row["Product Name"])),
    "hsn_code": str(scalar(row["HSN Code"])),
    "packing_size": str(scalar(row["Packing Size"])),
    "shelf_life_months": int(scalar(row["Minimum Labeled Shelf Life (Months) as per Tender"])),
    "company_name": str(scalar(row["Name Of Company"])),
    "tax_rate": float(scalar(row["Tax Rate"])),
    "po_no": int(scalar(row["PO No."])),
    "po_date": parse_date(row["PO Date"]),
    "po_quantity": int(scalar(row["PO Quantity"])),
    "drug_value": int(scalar(row["Drug Value"])),
    "po_value": int(scalar(row["PO Value"])),
    "invoice_qty": int(scalar(row["Invoice Qty."])),
    "invoice_value": int(scalar(row["Invoice Value"])),
    "pending_invoice_qty": int(scalar(row["Pending Invoice Qty"])),
    "pending_invoice_value": int(scalar(row["Pending Invoice Value"])),
    "active_quantity_spdr": int(scalar(row["Active Quantity in SPDR"])),
    "schedule_days": int(scalar(row["Schedule Days on PO Copy"])),
    "schedule_date": parse_date(row["Schedule Date"]),
    "remaining_days": int(scalar(row["Remaining Days  in Schedule Date"])),
    "status": parse_status(row["Penalty / Late Delivery Charges"]),
    "invoice_submission_date": parse_date(row["Date of Invoice Submission"]),
    "payment_sanction_date": parse_date(row["Date of Payment Sanction"]),
    "amount_passed": int(scalar(row["Amount Pass This P O"])),
    "outstanding_to_rmscl": int(scalar(row["O/s to RMSCL"])),
    "file_no": int(scalar(row["File No."])),
    "remarks": str(scalar(row["Remark"])) if not pd.isna(row["Remark"]) else "",
    "supply_percent": float(scalar(row[f"% of supply"])),
}
order_request = OrderCreateRequest(**row_data)

print(order_request)

async def create_order_test():
    async with SessionLocal() as session:
        return await service.create_order(new_db=session, order_data=order_request)

new_order = asyncio.run(create_order_test())



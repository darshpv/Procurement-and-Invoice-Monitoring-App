from datetime import date
import pandas as pd
from procure_track.schemas import OrderCreateRequest


excel_file = pd.ExcelFile(r"C:\Users\darsh.chaudhary\procurement-and-invoice-monitoring-app\backend\work_data.xlsx")

df = pd.read_excel(excel_file, sheet_name="All Orders")
df.columns = df.columns.str.strip()  # remove whitespace from headers
row = df.iloc[2]


def scalar(value):
    if pd.isna(value):
        return "0"
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
        return date(year=2026, month=12, day=12)
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, date):
        return value
    return pd.to_datetime(value).date()


def get_all_orders():
    orders = []

    for _, row in df.iterrows():
        order = OrderCreateRequest(
            tender_ref_no=str(scalar(row["Tender Ref. No."])),
            placebo_required=parse_bool(row["Placebo Required (Yes/No)"]),
            product_code=str(scalar(row["Product Code"])),
            product_name=str(scalar(row["Product Name"])),
            company_name=str(scalar(row["Name Of Company"])),
            po_no=int(scalar(row["PO No."])),
            po_date=parse_date(row["PO Date"]),
            po_quantity=int(scalar(row["PO Quantity"])),
            po_value=int(scalar(row["PO Value"])),
            invoice_qty=int(scalar(row["Invoice Qty."])),
            invoice_value=int(scalar(row["Invoice Value"])),
            pending_invoice_qty=int(scalar(row["Pending Invoice Qty"])),
            pending_invoice_value=int(scalar(row["Pending Invoice Value"])),
            schedule_date=parse_date(row["Schedule Date"]),
            remaining_days=int(scalar(row["Remaining Days  in Schedule Date"])),
            status=scalar(row["Penalty / Late Delivery Charges"]),
            payment_sanction_date=parse_date(row["Date of Payment Sanction"]),
        )
        orders.append(order)
    return orders


import pandas as pd
from procure_track.models import Company
from sqlalchemy.ext.asyncio import AsyncSession

excel_file = pd.ExcelFile(r"C:\Users\darsh.chaudhary\procurement-and-invoice-monitoring-app\backend\work_data.xlsx")

df = pd.read_excel(excel_file, sheet_name="All Orders")

company_df = (
    df[
        ["Name Of Company"]
    ]
)




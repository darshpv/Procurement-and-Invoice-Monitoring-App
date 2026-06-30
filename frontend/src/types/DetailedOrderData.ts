export type DetailedOrderData = {
    tender_ref_no: string
    product_name: string

    company_name: string

    po_no: number
    po_date: Date
    po_quantity: number
    po_value: number

    invoice_qty: number
    invoice_value: number

    pending_invoice_qty: number
    pending_invoice_value: number

    schedule_date: Date
    remaining_days: number
    status: string

    payment_sanction_date: Date
}
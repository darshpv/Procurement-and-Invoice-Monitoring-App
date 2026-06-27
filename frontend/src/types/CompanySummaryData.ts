export type CompanySummaryData = {
    company_name: string
    total_invoice_value: number
    total_po_value: number
    pending_invoice_value: number
    pending_invoice_qty: number
    delayed_deliveries_count: number
    payments_pending_count: number
    supply_percentage: number
}
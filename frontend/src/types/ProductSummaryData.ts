export type ProductSummaryData = {
    product_name: string
    total_po_qty: number
    total_invoice_qty: number
    pending_invoice_qty: number
    total_po_value: number
    total_invoice_value: number
    pending_invoice_value: number
    delayed_deliveries_count: number
}
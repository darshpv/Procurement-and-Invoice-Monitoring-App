import axios from "axios"

export const ENDPOINTS = {
    CREATE_ORDERS: () => "/orders/create_all_orders",
    GET_COMPARISON_DATA: (sort_by: string) => `/orders/get_comparison_data/${sort_by}`,
    GET_DETAILED_ORDERS: (sort_by: string, search_by: string, search_value: string | number) => `/orders/get_detailed_orders/${sort_by}/${encodeURIComponent(search_by)}/${encodeURIComponent(String(search_value))}`,
    // SEARCH_DETAILED_ORDER: (search_by: string, search_value: string | number) =>
    //     `/orders/search_detailed_order/${encodeURIComponent(search_by)}/${encodeURIComponent(String(search_value))}`,
    GET_COMPANY_SUMMARY: () => "/orders/get_company_summary",
    GET_PRODUCT_SUMMARY: () => "/orders/get_product_summary",
    GET_STATUS_SUMMARY: () => "/orders/get_status_summary",
    GET_DELAYED_DELIVERIES: () => "/orders/get_delayed_deliveries",
    GET_PENDING_PAYMENTS: () => "/orders/get_pending_payments",
}

export const instance = axios.create({
    baseURL: "http://127.0.0.1:8000/"
})
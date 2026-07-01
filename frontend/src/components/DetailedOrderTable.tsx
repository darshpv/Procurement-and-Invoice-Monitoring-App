import { ENDPOINTS, instance } from "../utils/api"
import { SearchCriterias, OrderSortingCategories } from "../enums";
import type { DetailedOrderData } from "../types/DetailedOrderData";
import { useState, useEffect } from "react";
import "./DetailedOrderTable.css"

export default function DetailedOrderTable() {

    const [displayedOrders, setDisplayedOrders] = useState<DetailedOrderData[]>();
    const [sortingCategory, setSortingCategory] = useState<string>(OrderSortingCategories.company_name)
    const [searchingCriteria, setSearchingCriteria] = useState<string>(SearchCriterias.company_name);
    const [searchValue, setSearchValue] = useState<string | number>("");
    const [pageNumber, setPageNumber] = useState<number>(1);
    const [pageStartValue, setPageStartValue] = useState<number>(0);
 
    async function getSortedOrders(category: string, criteria: string, value: string | number) {
        try {
            const response = await instance.get(ENDPOINTS.GET_DETAILED_ORDERS(category, criteria, value));
            console.log(response.data[0])
            if (response.data != null) {
                const normalizedOrders = (response.data as DetailedOrderData[]).map(
                                    (order) => ({
                                        ...order,
                                        po_date: new Date(order.po_date),
                                        schedule_date: new Date(order.schedule_date),
                                        payment_sanction_date: new Date(order.payment_sanction_date)
                                    })
                                );
                setDisplayedOrders(normalizedOrders);
            }
        } catch(e) {
            console.log(e);
        };
    };

    function getPageEndValue() {

        const pageEndValue = 15 * pageNumber;

        return pageEndValue;
    }

    useEffect(() => {
        if (searchingCriteria && searchValue !== undefined && searchValue != "") {
            getSortedOrders(sortingCategory, searchingCriteria, searchValue);
        } else if (searchValue == "") {
            getSortedOrders(sortingCategory, searchingCriteria, "load_all");
        }
    }, [sortingCategory, searchingCriteria, searchValue])

    useEffect(() => {
        getSortedOrders(sortingCategory, searchingCriteria, "load_all");
    }, []);


    return (
        <div className="detailed-order-table">
            <div className="header-container">
                <h2>
                    DETAILED ORDER-LEVEL INFORMATION
                </h2>
                <div className="search-container">
                    <h2>
                        SORT BY: 
                    </h2>
                    <select
                        value={sortingCategory}
                        onChange={(e) => {
                            setSortingCategory(e.target.value);
                            setPageNumber(1);
                            setPageStartValue(0);
                        }}
                        title="Edit Sorting Category"
                        className="searching-category-select"
                    >
                        <option value={OrderSortingCategories.company_name}>Company Name</option>
                        <option value="po_date">PO Date</option>
                        <option value="po_value">PO Value</option>
                        <option value="invoice_value">Invoice Value</option>
                        <option value="pending_invoice_value">Pending Invoice Value</option>
                        <option value="pending_invoice_qty">Pending Invoice Quantity</option>
                        <option value="remaining_days">Remaining Days</option>
                        <option value="status">Status</option>
                    </select>
                    <div style={{width: "20px"}}></div>
                    <h2>
                        SEARCH BY: 
                    </h2>
                    <select
                        value={searchingCriteria}
                        onChange={(e) => {
                            setSearchingCriteria(e.target.value)
                            setPageNumber(1);
                            setPageStartValue(0);
                        }}
                        title="Edit Searching Category"
                        className="searching-category-select"
                    >
                        <option value="company_name">Company Name</option>
                        <option value="product_name">Product Name</option>
                        <option value="po_no">PO Number</option>
                        <option value="tender_ref_no">Tender Reference</option>
                    </select>
                    <div style={{width: "20px"}}></div>
                    <h2>
                        SEARCH VALUE: 
                    </h2>
                    <input
                        title="Search value..."
                        value={searchValue}
                        onChange={(e) => {
                            setSearchValue(e.target.value);
                        }}
                    />
                    <div style={{width: "20px"}}></div>
                    <button
                        disabled={Boolean(pageNumber === 1)}
                        onClick={() => {
                            setPageNumber(pageNumber - 1);
                            setPageStartValue(pageStartValue - 15);
                        }}
                    >
                        {"<"}
                    </button>
                    <h2>
                        {pageNumber}
                    </h2>
                    <button
                        disabled={Boolean(displayedOrders && getPageEndValue() > (displayedOrders.length ?? 0))}
                        onClick={() => {
                            setPageNumber(pageNumber + 1);
                            setPageStartValue(getPageEndValue());
                        }}
                    >
                        {">"}
                    </button>
                </div>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Tender Ref. No.</th>
                        <th>Company Name</th>
                        <th>Product Name</th>
                        <th>PO No.</th>
                        <th>PO Date</th>
                        <th>PO Quantity</th>
                        <th>PO Value</th>
                        <th>Invoice Quantity</th>
                        <th>Invoice Value</th>
                        <th>Pending Invoice Value</th>
                        <th>Pending Invoice Quantity</th>
                        <th>Schedule Date</th>
                        <th>Remaining Days</th>
                        <th>Status</th>
                        <th>Payment Sanction Date</th>

                    </tr>
                </thead>
                <tbody>
                    {
                        displayedOrders?.slice(pageStartValue, getPageEndValue() + 1).map(
                            (order, index) => (
                                <tr
                                    key={index}
                                    className={
                                        (order.pending_invoice_qty > 0 && order.remaining_days < 0 && order.status !== "P O Closed") ?
                                        "red-row" :
                                        (order.pending_invoice_value > 0) ?
                                        "orange-row" :
                                        "green-row"
                                    }
                                >
                                    <td>{order.tender_ref_no}</td>
                                    <td>{order.company_name}</td>
                                    <td>{order.product_name}</td>
                                    <td>{order.po_no}</td>
                                    <td>{(order.po_date).toLocaleDateString()}</td>
                                    <td>{order.po_quantity}</td>
                                    <td>INR {(order.po_value/10000000).toFixed(2)} Cr</td>
                                    <td>{order.invoice_qty}</td>
                                    <td>INR {(order.invoice_value/10000000).toFixed(2)} Cr</td>
                                    <td>INR {(order.pending_invoice_value/10000000).toFixed(2)} Cr</td>
                                    <td>{(order.pending_invoice_qty).toLocaleString("en-IN")}</td>
                                    <td>{(order.schedule_date).toLocaleDateString()}</td>
                                    <td>{order.remaining_days}</td>
                                    <td>{order.status}</td>
                                    <td>{(order.payment_sanction_date).toLocaleDateString()}</td>
                                </tr>
                            )
                        )
                    }
                </tbody>
                
            </table>
            
        </div>
    )
}

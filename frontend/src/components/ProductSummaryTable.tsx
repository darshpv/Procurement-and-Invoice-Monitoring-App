import { ENDPOINTS, instance } from "../utils/api"
import type { ProductSummaryData } from "../types/ProductSummaryData";
import { useState, useEffect } from "react";
import "./ProductSummaryTable.css"

export default function ProductSummaryTable() {

    const [displayedProducts, setDisplayedProducts] = useState<ProductSummaryData[]>();
 
    async function getProductSummary() {
        try {
            const response = await instance.get(ENDPOINTS.GET_PRODUCT_SUMMARY());
            if (response.data != null) {
                setDisplayedProducts(response.data);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getProductSummary()
    }, [])

    return (
        <div className="products-table">
            <div className="products-container">
                <h2>
                    PRODUCT SUMMARY
                </h2>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Product Name</th>
                        <th>Total PO Quantity</th>
                        <th>Total Invoice Quantity</th>
                        <th>Pending Quantity</th>
                        <th>Total PO Value</th>
                        <th>Total Invoice Value</th>
                        <th>Pending Invoice Value</th>
                        <th>Delayed Deliveries Count</th>
                    </tr>
                </thead>
                <tbody>
                    {displayedProducts?.map(
                        (product) => (
                            <tr>
                                <td>{product.product_name}</td>
                                <td>{product.total_po_qty}</td>
                                <td>{product.total_invoice_qty}</td>
                                <td>{product.pending_invoice_qty}</td>
                                <td>{product.total_po_value}</td>
                                <td>{product.total_invoice_value}</td>
                                <td>{product.pending_invoice_value}</td>
                                <td>{product.delayed_deliveries_count}</td>
                            </tr>
                        )
                    )}
                </tbody>
                
            </table>
            
        </div>
    )
}


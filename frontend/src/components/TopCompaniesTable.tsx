import { ENDPOINTS, instance } from "../utils/api"
import { SortingCategories } from "../enums";
import type { ComparisonData } from "../types/ComparisonData";
import { useState, useEffect } from "react";
import "./TopCompaniesTable.css"

export default function TopCompaniesTable() {

    const [displayedCompanies, setDisplayedCompanies] = useState<ComparisonData[]>();
    const [sortingCategory, setSortingCategory] = useState<string>(SortingCategories.pending_invoice_qty);
 
    async function getTopCompanies(category: string) {
        try {
            const response = await instance.get(ENDPOINTS.GET_COMPARISON_DATA(category));
            if (response.data != null) {
                setDisplayedCompanies(response.data);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getTopCompanies(sortingCategory)
    }, [sortingCategory])
    return (
        <div className="top-companies-table">
            <h2>
                Top 10 Companies
            </h2>
            <select
                    value={sortingCategory}
                    onChange={(e) => {
                        setSortingCategory(e.target.value)
                    }}
                    title="Edit Sorting Category"
                    className="sorting-category-select"
                >
                    <option value="total_po_value">Total PO Value</option>
                    <option value="pending_invoice_value">Pending Invoice Value</option>
                    <option value="pending_invoice_qty">Pending Quantity</option>
                    <option value="delayed_deliveries_count">Delayed Deliveries Count</option>
                    <option value="payments_pending_count">Payments Pending Count</option>
                </select>
            <table>
                <thead>
                    <tr>
                        <th>Company Name</th>
                        <th>Total PO Value</th>
                        <th>Total Invoice Value</th>
                        <th>Pending Invoice Value</th>
                        <th>Pending Quantity</th>
                        <th>Delayed Deliveries Count</th>
                        <th>Payments Pending Count</th>
                    </tr>
                </thead>
                <tbody>
                    {displayedCompanies?.map(
                        (company) => (
                            <tr>
                                <td>{company.company_name}</td>
                                <td>INR {(company.total_po_value/10000000).toFixed(2)} Cr</td>
                                <td>INR {(company.total_invoice_value/10000000).toFixed(2)} Cr</td>
                                <td>INR {(company.pending_invoice_value/10000000).toFixed(2)} Cr</td>
                                <td>{(company.pending_invoice_qty).toLocaleString("en-IN")}</td>
                                <td>{company.delayed_deliveries_count}</td>
                                <td>{company.payments_pending_count}</td>
                            </tr>
                        )
                    )}
                </tbody>
                
            </table>
            
        </div>
    )
}


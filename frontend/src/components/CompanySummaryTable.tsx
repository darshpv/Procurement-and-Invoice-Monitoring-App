import { ENDPOINTS, instance } from "../utils/api"
import type { CompanySummaryData } from "../types/CompanySummaryData";
import { useState, useEffect } from "react";
import "./CompanySummary.css"

export default function CompanySummaryTable() {

    const [displayedCompanies, setDisplayedCompanies] = useState<CompanySummaryData[]>();
 
    async function getCompanySummary() {
        try {
            const response = await instance.get(ENDPOINTS.GET_COMPANY_SUMMARY());
            if (response.data != null) {
                setDisplayedCompanies(response.data);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getCompanySummary()
    }, [])

    return (
        <div className="companies-table">
            <div className="container">
                <h2>
                    COMPANY SUMMARY
                </h2>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Company Name</th>
                        <th>Total PO Value</th>
                        <th>Total Invoice Value</th>
                        <th>Pending Invoice Value</th>
                        <th>Pending Quantity</th>
                        <th>Supply Percentage</th>
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
                                <td>{(company.supply_percentage*100).toFixed(2)}%</td>
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


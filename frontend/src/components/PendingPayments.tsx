import { ENDPOINTS, instance } from "../utils/api"
import type { PendingPaymentsData } from "../types/PendingPaymentsData";
import { useState, useEffect } from "react";
import "./PendingPayments.css"


export default function PendingPaymentsList() {

    const [displayedPayments, setDisplayedPayments] = useState<PendingPaymentsData[]>();
 
    async function getPendingPayments() {
        try {
            const response = await instance.get(ENDPOINTS.GET_PENDING_PAYMENTS());
            if (response.data != null) {
                const normalizedPayments = (response.data as PendingPaymentsData[]).map(
                    (delivery) => ({
                        ...delivery,
                        payment_sanction_date: new Date(delivery.payment_sanction_date),
                    })
                );
                setDisplayedPayments(normalizedPayments);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getPendingPayments()
    }, [])

    return (
        <div className="payments-table">
            <div className="container">
                <h2>
                    PENDING PAYMENTS LIST
                </h2>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Company Name</th>
                        <th>PO Number</th>
                        <th>Invoice Value</th>
                        <th>Pending Invoice Value</th>
                        <th>Payment Sanction Date</th>
                    </tr>
                </thead>
                <tbody>
                    {displayedPayments?.map(
                        (payment) => (
                            <tr>
                                <td>{payment.company_name}</td>
                                <td>{payment.po_no}</td>                   
                                <td>INR {(payment.invoice_value/10000000).toFixed(2)} Cr</td>
                                <td>INR {(payment.pending_invoice_value/10000000).toFixed(2)} Cr</td>
                                <td>{(payment.payment_sanction_date).toLocaleDateString()}</td>
                            </tr>
                        )
                    )}
                </tbody>
                
            </table>
            
        </div>
    )
}


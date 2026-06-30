import { ENDPOINTS, instance } from "../utils/api"
import type { DelayedDeliveriesData } from "../types/DelayedDeliveriesData";
import { useState, useEffect } from "react";
import "./DelayedDeliveries.css"


export default function DelayedDeliveriesList() {

    const [displayedDeliveries, setDisplayedDeliveries] = useState<DelayedDeliveriesData[]>();
 
    async function getDelayedDeliveries() {
        try {
            const response = await instance.get(ENDPOINTS.GET_DELAYED_DELIVERIES());
            if (response.data != null) {
                const normalizedDeliveries = (response.data as DelayedDeliveriesData[]).map(
                    (delivery) => ({
                        ...delivery,
                        schedule_date: new Date(delivery.schedule_date),
                    })
                );
                setDisplayedDeliveries(normalizedDeliveries);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getDelayedDeliveries()
    }, [])

    return (
        <div className="deliveries-table">
            <div className="container">
                <h2>
                    DELAYED DELIVERIES LIST
                </h2>
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Company Name</th>
                        <th>Product Name</th>
                        <th>PO Number</th>
                        <th>Schedule Date</th>
                        <th>Remaining Days</th>
                        <th>Pending Quantity</th>
                        <th>Pending Invoice Value</th>
                    </tr>
                </thead>
                <tbody>
                    {displayedDeliveries?.map(
                        (delivery) => (
                            <tr>
                                <td>{delivery.company_name}</td>
                                <td>{delivery.product_name}</td>
                                <td>{delivery.po_no}</td>
                                <td>{(delivery.schedule_date).toLocaleDateString()}</td>
                                <td>{delivery.remaining_days}</td>
                                <td>{(delivery.pending_invoice_qty).toLocaleString("en-IN")}</td>
                                <td>INR {(delivery.pending_invoice_value/10000000).toFixed(2)} Cr</td>
                            </tr>
                        )
                    )}
                </tbody>
                
            </table>
            
        </div>
    )
}


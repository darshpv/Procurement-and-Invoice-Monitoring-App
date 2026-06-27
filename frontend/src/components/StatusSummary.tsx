
import { instance, ENDPOINTS } from "../utils/api";
import { useEffect, useState } from "react";
import type { StatusSummaryData } from "../types/StatusSummaryData";
import "./StatusSummary.css"

export default function StatusSummaryCards() {

    const [statusCount, setStatusCount] = useState<StatusSummaryData | null>(null);

    async function getStatusSummary() {
        try {
            const response = await instance.get(ENDPOINTS.GET_STATUS_SUMMARY());
            if (response.data != null) {
                const payload = Array.isArray(response.data) ? response.data[0] : response.data;
                setStatusCount(payload);
            }
        } catch(e) {
            console.log(e);
        };
    };

    useEffect(() => {
        getStatusSummary();
    }, [])

    return (
        <div className="status-summary-page">
            <h2>
                Status Summary
            </h2>
            <div className="status-cards">
                <div className="status-card">
                    <div className="label">Bill Process</div>
                    <div className="value">{statusCount?.bill_process ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">Bill Submit</div>
                    <div className="value">{statusCount?.bill_submit ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">PO Closed</div>
                    <div className="value">{statusCount?.po_closed ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">L D 0%</div>
                    <div className="value">{statusCount?.ld_0 ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">L D 5.0%</div>
                    <div className="value">{statusCount?.ld_5 ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">L D 7.5%</div>
                    <div className="value">{statusCount?.ld_7_5 ?? '-'}</div>
                </div>
                <div className="status-card">
                    <div className="label">L D 10.0%</div>
                    <div className="value">{statusCount?.ld_10 ?? '-'}</div>
                </div>
            </div>
        </div>
    )
}
import { useState } from "react";
import "./DashBoard.css";
import StatusSummaryCards from "./StatusSummary";
import TopCompaniesTable from "./TopCompaniesTable";
import ProductSummaryTable from "./ProductSummaryTable";
import CompanySummaryTable from "./CompanySummaryTable";
import DelayedDeliveriesList from "./DelayedDeliveries";
import PendingPaymentsList from "./PendingPayments";
import DetailedOrderTable from "./DetailedOrderTable";

export default function DashBoard() {
    const [activeComponent, setActiveComponent] = useState<string | null>("statusSummary");

    return (
        <>
        <div className="app-bar">
            <h1>
                Procurement & Invoice Monitoring App
            </h1>
            <div className="buttons-container">
                <button onClick={() => (setActiveComponent("topCompanies"))}>Top Companies</button>
                <button onClick={() => (setActiveComponent("companySummary"))}>Company Summary</button>
                <button onClick={() => (setActiveComponent("productSummary"))}>Product Summary</button>
                <button onClick={() => (setActiveComponent("statusSummary"))}>Status Summary</button>
                <button onClick={() => (setActiveComponent("delayedDeliveries"))}>Delayed Deliveries</button>
                <button onClick={() => (setActiveComponent("paymentsPending"))}>Payments Pending</button>
                <button onClick={() => (setActiveComponent("detailedOrders"))}>Detailed Orders</button>
            </div>
        </div>
        <>
                {activeComponent === "statusSummary" && (<StatusSummaryCards></StatusSummaryCards>)}
                {activeComponent === "topCompanies" && (<TopCompaniesTable></TopCompaniesTable>)}
                {activeComponent === "companySummary" && (<CompanySummaryTable></CompanySummaryTable>)}
                {activeComponent === "productSummary" && (<ProductSummaryTable></ProductSummaryTable>)}
                {activeComponent === "delayedDeliveries" && (<DelayedDeliveriesList></DelayedDeliveriesList>)}
                {activeComponent === "paymentsPending" && (<PendingPaymentsList></PendingPaymentsList>)}
                {activeComponent === "detailedOrders" && (<DetailedOrderTable></DetailedOrderTable>)}
            
        </>
        </>
    )
}
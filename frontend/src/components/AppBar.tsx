import "./AppBar.css";

export default function AppBar() {
    return (
        <div className="app-bar">
            <h1>
                Procurement & Invoice Monitoring App
            </h1>
            <div className="buttons-container">
                <button>Top Companies</button>
                <button>Company Summary</button>
                <button>Product Summary</button>
                <button>Status Summary</button>
                <button>Delayed Deliveries</button>
                <button>Payments Pending</button>
                <button>Detailed Orders</button>
            </div>
        </div>
    )
}
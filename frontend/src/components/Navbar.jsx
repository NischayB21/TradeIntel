import "./Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="logo">

                TradeIntel

            </div>

            <div className="nav-links">

                <a href="/">Home</a>

                <a href="/">Features</a>

                <a href="/">Prediction</a>

                <a href="/">News</a>

                <a href="/">About</a>

            </div>

            <button className="dashboard-btn">

                Dashboard

            </button>

        </nav>

    );

}

export default Navbar;
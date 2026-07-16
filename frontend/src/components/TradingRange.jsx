import "./TradingRange.css";

function TradingRange({ stock }) {

    return (

        <div className="trading-range">

            <div className="trading-header">

                <h2>

                    Expected Trading Range

                </h2>

                <p>

                    Machine Learning Estimated Price Range

                </p>

            </div>

            <div className="range-grid">

                <div className="range-card">

                    <span>

                        Low Target

                    </span>

                    <h2>

                        ${stock["Expected Trading Range"]["Low Target"]}

                    </h2>

                </div>

                <div className="range-card expected">

                    <span>

                        Expected Target

                    </span>

                    <h2>

                        ${stock["Expected Trading Range"]["Best Target"]}

                    </h2>

                </div>

                <div className="range-card">

                    <span>

                        High Target

                    </span>

                    <h2>

                        ${stock["Expected Trading Range"]["High Target"]}

                    </h2>

                </div>

            </div>

        </div>

    );

}

export default TradingRange;
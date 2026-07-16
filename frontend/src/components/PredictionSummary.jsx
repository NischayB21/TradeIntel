import "./PredictionSummary.css";

function PredictionSummary({ stock }) {

    return (

        <div className="prediction-summary">

            <div className="summary-header">

                <div>

                    <h1>{stock.Ticker}</h1>

                    <p>

                        AI Stock Prediction Dashboard

                    </p>

                </div>

                <div
                    className={`recommendation ${stock["Final Recommendation"].toLowerCase().replace(" ", "-")}`}
                >
                    {stock["Final Recommendation"]}
                </div>

            </div>

            <div className="summary-grid">

                <div className="summary-card">

                    <span>Current Price</span>

                    <h2>

                        ${stock["Current Closing Price"]}

                    </h2>

                </div>

                <div className="summary-card">

                    <span>Target Price</span>

                    <h2>

                        ${stock["Target Closing Price"]}

                    </h2>

                </div>

                <div className="summary-card">

                    <span>Expected Return</span>

                    <h2>

                        {stock["Expected Return (%)"]}%

                    </h2>

                </div>

                <div className="summary-card">

                    <span>Confidence</span>

                    <h2>

                        {stock["Confidence (%)"]}%

                    </h2>

                </div>

                <div className="summary-card">

                    <span>Risk</span>

                    <h2>

                        {stock["Risk Level"]}

                    </h2>

                </div>

                <div className="summary-card">

                    <span>Prediction Date</span>

                    <h2>

                        {stock["Prediction Date"]}

                    </h2>

                </div>

            </div>

        </div>

    );

}

export default PredictionSummary;
import { useState } from "react";
import "./Hero.css";
import api from "../services/api";

function Hero() {

    const [ticker, setTicker] = useState("");

    const [loading, setLoading] = useState(false);

    const [stock, setStock] = useState(null);

    const analyzeStock = async () => {

    console.log("Analyze button clicked");

};
    return (

        <section className="hero">

            <div className="left">

                <h1>

                    Predict Stocks

                    <br />

                    Smarter

                    <br />

                    with AI

                </h1>

                <p>

                    AI-powered stock intelligence using
                    Machine Learning, Sentiment Analysis,
                    RAG and Local LLMs.

                </p>

                <div className="search">

                    <input

                        type="text"

                        placeholder="Enter Stock Symbol"

                        value={ticker}

                        onChange={(e) => setTicker(e.target.value)}

                        onKeyDown={(e) => {

                            if (e.key === "Enter") {

                                analyzeStock();

                            }

                        }}

                    />

                    <button

                        onClick={analyzeStock}

                    >

                        {

                            loading

                                ?

                                "Analyzing..."

                                :

                                "Analyze"

                        }

                    </button>

                </div>

            </div>

            <div className="right">

                <div className="card">

                    <small>

                        {

                            stock

                                ?

                                stock["Ticker"]

                                :

                                "Apple Inc."

                        }

                    </small>

                    <h2>

                        {

                            stock

                                ?

                                `$${stock["Target Closing Price"]}`

                                :

                                "$317.61"

                        }

                    </h2>

                    <p>

                        Predicted Closing Price

                    </p>

                    <br />

                    <strong>

                        Recommendation :

                        {

                            stock

                                ?

                                stock["Final Recommendation"]

                                :

                                "BUY"

                        }

                    </strong>

                    <br />

                    <br />

                    <strong>

                        Confidence :

                        {

                            stock

                                ?

                                `${stock["Confidence (%)"]}%`

                                :

                                "90%"

                        }

                    </strong>

                </div>

            </div>

        </section>

    );

}

export default Hero;
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Hero.css";

function Hero() {

    const [ticker, setTicker] = useState("");

    const navigate = useNavigate();

    const analyzeStock = () => {

        if (!ticker.trim()) {

            alert("Please enter a stock ticker.");

            return;

        }

        navigate(
            `/analysis/${ticker.toUpperCase()}`
        );

    };

    return (

        <section className="hero">

            <div className="left">

                <h1>

                    Predict Stocks

                    <br />

                    Smarter with AI

                </h1>

                <p>

                    Machine Learning, Sentiment Analysis,
                    RAG and Local LLMs combined into one
                    intelligent stock analysis platform.

                </p>

                <div className="search">

                    <input

                        type="text"

                        placeholder="Enter Stock Symbol (AAPL)"

                        value={ticker}

                        onChange={(e) =>
                            setTicker(e.target.value)
                        }

                        onKeyDown={(e) => {

                            if (e.key === "Enter") {

                                analyzeStock();

                            }

                        }}

                    />

                    <button

                        onClick={analyzeStock}

                    >

                        Analyze

                    </button>

                </div>

            </div>

            <div className="right">

                <div className="card">

                    <small>

                        TradeIntel AI

                    </small>

                    <h2>

                        Smart
                        <br />
                        Predictions

                    </h2>

                    <p>

                        AI powered stock prediction
                        using Machine Learning,
                        Sentiment Analysis,
                        Live News and RAG.

                    </p>

                </div>

            </div>

        </section>

    );

}

export default Hero;
import { useState } from "react";

function SearchBar({ onAnalyze }) {

    const [ticker, setTicker] = useState("");

    const handleSubmit = () => {

        if (!ticker.trim()) return;

        onAnalyze(ticker.toUpperCase());

    };

    return (

        <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

            <h2 className="text-xl font-semibold mb-4">

                Search Stock

            </h2>

            <div className="flex gap-3">

                <input
                    className="flex-1 border rounded-lg px-4 py-3"
                    placeholder="AAPL, MSFT, TSLA..."
                    value={ticker}
                    onChange={(e) => setTicker(e.target.value)}
                />

                <button
                    className="bg-blue-600 hover:bg-blue-700 text-white px-6 rounded-lg"
                    onClick={handleSubmit}
                >
                    Analyze
                </button>

            </div>

        </div>

    );

}

export default SearchBar;
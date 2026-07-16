import "./AIAnalysisCard.css";

function AIAnalysisCard({ analysis }) {

    if (!analysis) return null;

    return (

        <div className="ai-analysis">

            <div className="ai-header">

                <div>

                    <h2>

                        AI Investment Analysis

                    </h2>

                    <p>

                        Generated using Local LLM + RAG

                    </p>

                </div>

                <div className="ai-badge">

                    {analysis.recommendation}

                </div>

            </div>

            <div className="summary-box">

                <h3>

                    Summary

                </h3>

                <p>

                    {analysis.summary}

                </p>

            </div>

            <div className="stats-grid">

                <div className="stat-card">

                    <span>

                        Recommendation

                    </span>

                    <h2>

                        {analysis.recommendation}

                    </h2>

                </div>

                <div className="stat-card">

                    <span>

                        Risk

                    </span>

                    <h2>

                        {analysis.risk}

                    </h2>

                </div>

                <div className="stat-card">

                    <span>

                        AI Confidence

                    </span>

                    <h2>

                        {analysis.confidence}%

                    </h2>

                </div>

            </div>

            <div className="analysis-grid">

                <div className="analysis-box">

                    <h3>

                        AI Reasoning

                    </h3>

                    <ul>

                        {

                            analysis.reasoning.map(

                                (item, index) => (

                                    <li key={index}>

                                        {item}

                                    </li>

                                )

                            )

                        }

                    </ul>

                </div>

                <div className="analysis-box">

                    <h3>

                        Bullish Factors

                    </h3>

                    <ul>

                        {

                            analysis.pros.map(

                                (item, index) => (

                                    <li key={index}>

                                        {item}

                                    </li>

                                )

                            )

                        }

                    </ul>

                </div>

                <div className="analysis-box">

                    <h3>

                        Bearish Factors

                    </h3>

                    <ul>

                        {

                            analysis.cons.map(

                                (item, index) => (

                                    <li key={index}>

                                        {item}

                                    </li>

                                )

                            )

                        }

                    </ul>

                </div>

            </div>

        </div>

    );

}

export default AIAnalysisCard;
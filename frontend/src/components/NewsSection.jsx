import "./NewsSection.css";

function NewsSection({ news }) {

    return (

        <div className="news-section">

            <div className="news-header">

                <h2>

                    Latest News Analysis

                </h2>

                <p>

                    AI analyzed the latest market news impacting this stock.

                </p>

            </div>

            <div className="news-grid">

                {

                    news.map((article, index) => (

                        <div

                            className="news-card"

                            key={index}

                        >

                            <div
                                className={`news-tag ${article.Sentiment.toLowerCase()}`}
                            >

                                {article.Sentiment}

                            </div>

                            <h3>

                                {article.Headline}

                            </h3>

                            <div className="news-footer">

                                <div>

                                    Confidence

                                    <strong>

                                        {(article.Confidence * 100).toFixed(1)}%

                                    </strong>

                                </div>

                                <div>

                                    Score

                                    <strong>

                                        {article["Weighted Score"].toFixed(2)}

                                    </strong>

                                </div>

                            </div>

                        </div>

                    ))

                }

            </div>

        </div>

    );

}

export default NewsSection;
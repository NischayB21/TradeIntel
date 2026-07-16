import "./RetrievedContext.css";

function RetrievedContext({ documents }) {

    return (

        <div className="context-section">

            <div className="context-header">

                <h2>

                    Retrieved Financial Context

                </h2>

                <p>

                    Evidence retrieved using RAG before the AI generated its analysis.

                </p>

            </div>

            <div className="context-grid">

                {

                    documents.map(

                        (doc, index) => (

                            <div

                                className="context-card"

                                key={index}

                            >

                                <div className="context-number">

                                    Document {index + 1}

                                </div>

                                <p>

                                    {doc}

                                </p>

                            </div>

                        )

                    )

                }

            </div>

        </div>

    );

}

export default RetrievedContext;
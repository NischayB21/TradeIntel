import "./FeatureImportance.css";

function FeatureImportance({ features }) {

    const maxImportance = Math.max(

        ...features.map(

            feature => feature.Importance

        )

    );

    return (

        <div className="feature-section">

            <div className="feature-header">

                <h2>

                    Feature Importance

                </h2>

                <p>

                    Top Machine Learning Features influencing the prediction.

                </p>

            </div>

            {

                features.map(

                    (feature, index) => (

                        <div

                            key={index}

                            className="feature-row"

                        >

                            <div className="feature-top">

                                <span>

                                    {feature.Feature}

                                </span>

                                <span>

                                    {(feature.Importance * 100).toFixed(2)}%

                                </span>

                            </div>

                            <div className="progress">

                                <div

                                    className="progress-fill"

                                    style={{

                                        width:

                                            `${(feature.Importance / maxImportance) * 100}%`

                                    }}

                                />

                            </div>

                        </div>

                    )

                )

            }

        </div>

    );

}

export default FeatureImportance;
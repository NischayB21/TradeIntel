import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import api from "../services/api";

import Navbar from "../components/Navbar";
import PredictionSummary from "../components/PredictionSummary";
import TradingRange from "../components/TradingRange";
import AIAnalysisCard from "../components/AIAnalysisCard";
import NewsSection from "../components/NewsSection";
import FeatureImportance from "../components/FeatureImportance";
import RetrievedContext from "../components/RetrievedContext";

function Analysis() {

    const { ticker } = useParams();

    const [analysis, setAnalysis] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchAnalysis();

    }, [ticker]);

    async function fetchAnalysis() {

        try {

            setLoading(true);

            const response = await api.get(

                `/analyze/${ticker}`

            );

            setAnalysis(response.data);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    }

    if (loading) {

        return (

            <>

                <Navbar />

                <div className="analysis-container">

                    <h2>

                        Loading Analysis...

                    </h2>

                </div>

            </>

        );

    }

    return (

        <>

            <Navbar />

            <div className="analysis-container">

                <PredictionSummary

                    stock={analysis.Prediction}

                />

                <TradingRange

                    stock={analysis.Prediction}

                />

                <AIAnalysisCard

                    analysis={analysis["AI Analysis"]}

                />

                <NewsSection

                    news={analysis.Prediction["Top News"]}

                />

                <FeatureImportance

                    features={analysis.Prediction["Top Features"]}

                />

                <RetrievedContext

                    documents={analysis["Retrieved Context"]}

                />

            </div>

        </>

    );

}

export default Analysis;
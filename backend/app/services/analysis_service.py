from app.services.prediction_service import PredictionService
from app.services.rag_service import RAGService
from app.services.llm_service import LLMService


class AnalysisService:

    def __init__(self):

        self.prediction_service = PredictionService()

        self.rag_service = RAGService()

        self.llm_service = LLMService()

    def analyze(
        self,
        ticker: str,
        question: str,
    ):

        # ---------------------------------------------------
        # Prediction
        # ---------------------------------------------------

        prediction = self.prediction_service.predict(
            ticker
        )

        # ---------------------------------------------------
        # RAG
        # ---------------------------------------------------

        rag = self.rag_service.ask(
            ticker=ticker,
            question=question,
        )

        # ---------------------------------------------------
        # LLM Analysis
        # ---------------------------------------------------

        ai_analysis = self.llm_service.analyze(

            prediction=prediction,

            sentiment={
                "overall": prediction.get(
                    "News Sentiment"
                ),
                "score": prediction.get(
                    "Sentiment Score"
                ),
            },

            retrieved_context="\n\n".join(
                rag["Retrieved Documents"]
            ),

            question=question,

        )

        # ---------------------------------------------------
        # Final Response
        # ---------------------------------------------------

        return {

            "Ticker": ticker,

            "Prediction": prediction,

            "AI Analysis": ai_analysis,

            "Retrieved Context": rag[
                "Retrieved Documents"
            ],

        }
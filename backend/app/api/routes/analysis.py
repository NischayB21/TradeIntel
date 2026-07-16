from fastapi import APIRouter

from app.services.analysis_service import AnalysisService

router = APIRouter()

analysis = AnalysisService()


@router.get("/analyze/{ticker}")
def analyze_stock(ticker: str):

    return analysis.analyze(

        ticker=ticker.upper(),

        question=f"Should I buy {ticker.upper()} stock now?"

    )
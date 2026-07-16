from fastapi import APIRouter

from app.services.prediction_service import PredictionService

router = APIRouter()

predictor = PredictionService()


@router.get("/predict/{ticker}")
def predict_stock(ticker: str):

    result = predictor.predict(ticker.upper())

    return result
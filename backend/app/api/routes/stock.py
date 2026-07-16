from fastapi import APIRouter

from app.services.stock_service import StockService

router = APIRouter()

stock_service = StockService()


@router.get("/stocks")
def get_stocks():
    return stock_service.get_available_stocks()


@router.post("/stocks/download")
def download_stock_data():

    stock_service.download_stock_data()

    return {
        "message": "Stock data downloaded successfully."
    }
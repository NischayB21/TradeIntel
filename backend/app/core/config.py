from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import os

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()

# =====================================================
# Project Directories
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODEL_DIR = DATA_DIR / "models"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# =====================================================
# Finnhub
# =====================================================

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# =====================================================
# Stock Configuration
# =====================================================

SUPPORTED_STOCKS = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "NVDA": "NVIDIA",
    "AMZN": "Amazon",
    "GOOGL": "Google",
    "META": "Meta",
    "TSLA": "Tesla",
    "NFLX": "Netflix",
    "AMD": "AMD",
    "INTC": "Intel",
    "RELIANCE.NS": "Reliance",
    "TCS.NS": "TCS",
    "INFY.NS": "Infosys",
    "HDFCBANK.NS": "HDFC Bank",
    "ICICIBANK.NS": "ICICI Bank",
}

# =====================================================
# Download Dates
# =====================================================

START_DATE = "2014-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")

# =====================================================
# ML Features
# =====================================================

FEATURE_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Daily_Return",
    "SMA_20",
    "EMA_20",
    "RSI",
    "MACD",
    "BB_High",
    "BB_Low",
    "ATR",
    "Volume_Change",
    "Volatility",
    "Close_Lag1",
    "Close_Lag2",
    "Close_Lag3",
    "Return_Lag1",
    "Return_Lag2",
    "Return_Lag3",
    "RSI_Lag1",
    "MACD_Lag1",
    "Rolling_Mean_5",
    "Rolling_STD_5",
    "Momentum",
    "ROC",
    "MFI",
    "CCI",
    "ADX",
    "OBV",
]
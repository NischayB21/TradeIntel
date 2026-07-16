import pandas as pd
import yfinance as yf

from app.core.config import (
    SUPPORTED_STOCKS,
    START_DATE,
    END_DATE,
    RAW_DATA_DIR,
)


class StockService:
    """
    Handles all stock-related operations.
    """

    def __init__(self):
        self.stocks = SUPPORTED_STOCKS

    def get_supported_stocks(self):
        return self.stocks

    def download_stock(self, ticker: str) -> pd.DataFrame:
        """
        Download historical data for a single stock.
        """

        if ticker not in self.stocks:
            raise ValueError(f"{ticker} is not supported.")

        df = yf.download(
            ticker,
            start=START_DATE,
            end=END_DATE,
            auto_adjust=True,
            progress=False,
        )

        # Flatten MultiIndex columns (new yfinance versions)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Move Date from index to a column
        df.reset_index(inplace=True)

        return df

    def save_stock(self, ticker: str, df: pd.DataFrame):
        """
        Save stock data as CSV.
        """

        path = RAW_DATA_DIR / f"{ticker}.csv"

        df.to_csv(path, index=False)

        return path

    def download_all_stocks(self):
        """
        Download and save all supported stocks.
        """

        for ticker in self.stocks:

            print(f"Downloading {ticker}...")

            df = self.download_stock(ticker)

            self.save_stock(ticker, df)

        print("\nAll stock data downloaded successfully!")
import pandas as pd

from app.core.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR
)

from app.services.feature_service import FeatureService


class DatasetService:

    def __init__(self):
        self.feature_service = FeatureService()

    def process_stock(self, ticker):

        file_path = RAW_DATA_DIR / f"{ticker}.csv"

        df = pd.read_csv(file_path)

        df = self.feature_service.add_features(df)

        output_path = PROCESSED_DATA_DIR / f"{ticker}.csv"

        df.to_csv(output_path, index=False)

        return df
import pandas as pd

from app.core.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
)

from app.services.feature_service import FeatureService


class DatasetBuilder:

    def __init__(self):
        self.feature_service = FeatureService()

    def build_dataset(self):

        all_data = []

        for csv_file in RAW_DATA_DIR.glob("*.csv"):

            ticker = csv_file.stem

            print(f"Processing {ticker}")

            df = pd.read_csv(csv_file)

            df = self.feature_service.add_features(df)

            df["Ticker"] = ticker

            all_data.append(df)

        master_df = pd.concat(all_data, ignore_index=True)

        output_file = PROCESSED_DATA_DIR / "master_dataset.csv"

        master_df.to_csv(output_file, index=False)

        print(f"\nSaved dataset to {output_file}")

        return master_df
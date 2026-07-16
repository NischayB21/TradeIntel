import joblib
import pandas as pd

from app.core.config import MODEL_DIR


class FeatureImportanceService:

    def __init__(self):

        self.model = joblib.load(
            MODEL_DIR / "random_forest_regressor.pkl"
        )

    def get_feature_importance(self):

        importance = self.model.feature_importances_

        features = [
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

        df = pd.DataFrame(
            {
                "Feature": features,
                "Importance": importance,
            }
        )

        df = df.sort_values(
            by="Importance",
            ascending=False,
        )

        return df

    def get_top_features(self, top_n=5):

        df = self.get_feature_importance()

        return (
            df.head(top_n)
            .round(4)
            .to_dict(orient="records")
        )
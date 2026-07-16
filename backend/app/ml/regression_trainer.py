import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import TimeSeriesSplit

from app.core.config import MODEL_DIR


class RegressionTrainer:

    def train(self, df: pd.DataFrame):

        # -------------------------
        # Clean Data
        # -------------------------

        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.dropna()

        # -------------------------
        # Sort by Date
        # -------------------------

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date").reset_index(drop=True)

        # -------------------------
        # Features & Target
        # -------------------------

        X = df.drop(
            columns=[
                "Date",
                "Ticker",
                "Tomorrow_Close",
                "Target_Return",
            ]
        )

        y = df["Target_Return"]

        # -------------------------
        # Time Series Split
        # -------------------------

        tscv = TimeSeriesSplit(n_splits=5)

        mae_scores = []
        rmse_scores = []
        r2_scores = []

        last_model = None

        for fold, (train_idx, test_idx) in enumerate(tscv.split(X), start=1):

            X_train = X.iloc[train_idx]
            X_test = X.iloc[test_idx]

            y_train = y.iloc[train_idx]
            y_test = y.iloc[test_idx]

            model = RandomForestRegressor(
                n_estimators=300,
                random_state=42,
                n_jobs=-1,
            )

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            mae = mean_absolute_error(y_test, predictions)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))
            r2 = r2_score(y_test, predictions)

            mae_scores.append(mae)
            rmse_scores.append(rmse)
            r2_scores.append(r2)

            last_model = model

            print(f"\nFold {fold}")
            print(f"MAE  : {mae:.4f}")
            print(f"RMSE : {rmse:.4f}")
            print(f"R²   : {r2:.4f}")

        print("\n==============================")
        print("Average Results")
        print("==============================")

        print(f"\nAverage MAE  : {np.mean(mae_scores):.4f}")
        print(f"Average RMSE : {np.mean(rmse_scores):.4f}")
        print(f"Average R²   : {np.mean(r2_scores):.4f}")

        joblib.dump(
            last_model,
            MODEL_DIR / "random_forest_regressor.pkl",
        )

        print("\nModel Saved Successfully!")
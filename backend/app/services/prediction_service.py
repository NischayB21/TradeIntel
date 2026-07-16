import joblib
import numpy as np
import pandas as pd

from datetime import datetime, timedelta

from app.core.config import MODEL_DIR

from app.services.stock_service import StockService
from app.services.feature_service import FeatureService
from app.services.news_service import NewsService
from app.services.sentiment_service import SentimentService
from app.services.feature_importance_service import FeatureImportanceService
from app.services.decision_service import DecisionService


class PredictionService:

    def __init__(self):

        self.stock_service = StockService()

        self.feature_service = FeatureService()

        self.news_service = NewsService()

        self.sentiment_service = SentimentService()

        self.feature_importance_service = (
            FeatureImportanceService()
        )

        self.decision_service = DecisionService()

        self.model = joblib.load(
            MODEL_DIR / "random_forest_regressor.pkl"
        )

    def predict(self, ticker):

        # ---------------------------------------
        # Latest Stock Data
        # ---------------------------------------

        df = self.stock_service.download_stock(
            ticker
        )

        df = self.feature_service.add_features(df)

        latest = df.iloc[-1:].copy()

        current_price = float(
            latest["Close"].values[0]
        )

        latest_date = latest["Date"].values[0]

        prediction_date = (
            pd.bdate_range(
                pd.to_datetime(latest_date),
                periods=2,
            )[1]
            .strftime("%Y-%m-%d")
        )

        X = latest.drop(
            columns=[
                "Date"
            ]
        )

        # ---------------------------------------
        # Prediction
        # ---------------------------------------

        X_values = X.values

        predicted_return = float(
            self.model.predict(X_values)[0]
        )

        tree_predictions = np.array(
            [
                float(tree.predict(X_values)[0])
                for tree in self.model.estimators_
            ]
        )

        # ---------------------------------------
        # Prediction Targets
        # ---------------------------------------

        low_return = float(
            np.percentile(
                tree_predictions,
                25,
            )
        )

        target_return = float(
            np.mean(
                tree_predictions
            )
        )

        high_return = float(
            np.percentile(
                tree_predictions,
                75,
            )
        )

        low_price = current_price * (
            1 + low_return / 100
        )

        target_price = current_price * (
            1 + target_return / 100
        )

        high_price = current_price * (
            1 + high_return / 100
        )

        # ---------------------------------------
        # Technical Signal
        # ---------------------------------------

        if predicted_return >= 2:

            technical_signal = "STRONG BUY"

        elif predicted_return >= 1:

            technical_signal = "BUY"

        elif predicted_return <= -2:

            technical_signal = "STRONG SELL"

        elif predicted_return <= -1:

            technical_signal = "SELL"

        else:

            technical_signal = "HOLD"

        # ---------------------------------------
        # News
        # ---------------------------------------

        today = datetime.today().date()

        week_ago = today - timedelta(days=7)

        articles = self.news_service.get_news(
            ticker,
            str(week_ago),
            str(today),
        )

        sentiment = self.sentiment_service.analyze(
            articles
        )

        # ---------------------------------------
        # Confidence
        # ---------------------------------------

        volatility = float(
            latest["Volatility"].iloc[0]
        )

        prediction_strength = min(
            abs(predicted_return) * 40,
            100,
        )

        sentiment_strength = abs(
            float(sentiment["Sentiment Score"])
        ) * 100

        volatility_score = max(
            0,
            100 - volatility * 500,
        )

        confidence = (
            prediction_strength * 0.4
            + sentiment_strength * 0.3
            + volatility_score * 0.3
        )

        confidence = float(
            round(
                max(
                    10,
                    min(
                        confidence,
                        100,
                    ),
                ),
                2,
            )
        )

        # ---------------------------------------
        # Risk
        # ---------------------------------------

        if volatility >= 0.04:

            risk = "HIGH"

        elif volatility >= 0.02:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        if sentiment["Sentiment Score"] <= -0.40:

            risk = "HIGH"

        elif sentiment["Sentiment Score"] >= 0.40 and risk != "HIGH":

            risk = "LOW"

        if confidence < 40:

            risk = "HIGH"

        # ---------------------------------------
        # Decision
        # ---------------------------------------

        decision = self.decision_service.decide(
            technical_signal,
            predicted_return,
            confidence,
            sentiment["Overall Sentiment"],
            sentiment["Sentiment Score"],
        )

        # ---------------------------------------
        # Feature Importance
        # ---------------------------------------

        top_features = (
            self.feature_importance_service
            .get_top_features(5)
        )

        # ---------------------------------------
        # Response
        # ---------------------------------------

        return {

            "Ticker": ticker,

            "Prediction Horizon":
            "Next Trading Day",

            "Prediction Date":
            prediction_date,

            "Current Closing Price":
            float(round(current_price, 2)),

            "Target Closing Price":
            float(round(target_price, 2)),

            "Expected Return (%)":
            float(round(predicted_return, 2)),

            "Expected Trading Range": {

                "Low Target":
                float(round(low_price, 2)),

                "Best Target":
                float(round(target_price, 2)),

                "High Target":
                float(round(high_price, 2)),

            },

            "Technical Signal":
            technical_signal,

            "Confidence (%)":
            float(round(confidence, 2)),

            "News Sentiment":
            sentiment["Overall Sentiment"],

            "Sentiment Score":
            float(sentiment["Sentiment Score"]),

            "Final Recommendation":
            decision["Recommendation"],

            "Risk Level":
            risk,

            "Reason":
            decision["Reason"],

            "Top News":
            sentiment["Articles"],

            "Top Features":
            top_features,

        }
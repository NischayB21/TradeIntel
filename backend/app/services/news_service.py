import math
import requests
from datetime import datetime, timezone

from app.core.config import FINNHUB_API_KEY


class NewsService:

    def __init__(self):

        self.base_url = (
            "https://finnhub.io/api/v1/company-news"
        )

    def calculate_weight(self, timestamp):

        article_time = datetime.fromtimestamp(
            timestamp,
            tz=timezone.utc
        )

        now = datetime.now(timezone.utc)

        age_days = (
            now - article_time
        ).total_seconds() / 86400

        return round(
            max(
                math.exp(-0.15 * age_days),
                0.20
            ),
            3,
        )

    def relevance_score(
        self,
        ticker,
        headline,
        summary,
    ):

        ticker = ticker.replace(".NS", "")

        text = (
            headline +
            " " +
            summary
        ).lower()

        score = 0

        if ticker.lower() in text:
            score += 3

        company_names = {
            "AAPL": "apple",
            "MSFT": "microsoft",
            "NVDA": "nvidia",
            "GOOGL": "google",
            "META": "meta",
            "AMZN": "amazon",
            "TSLA": "tesla",
        }

        company = company_names.get(
            ticker,
            ""
        )

        if company and company in text:
            score += 5

        return score

    def get_news(
        self,
        ticker,
        from_date,
        to_date,
    ):

        params = {

            "symbol": ticker,

            "from": from_date,

            "to": to_date,

            "token": FINNHUB_API_KEY,

        }

        response = requests.get(
            self.base_url,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        news = response.json()

        articles = []

        for article in news:

            relevance = self.relevance_score(

                ticker,

                article["headline"],

                article["summary"]

            )

            if relevance == 0:
                continue

            articles.append({

                "Headline": article["headline"],

                "Summary": article["summary"],

                "Source": article["source"],

                "Published": datetime.fromtimestamp(
                    article["datetime"],
                    tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M"),

                "Weight": self.calculate_weight(
                    article["datetime"]
                ),

                "Relevance": relevance,

            })

        articles.sort(

            key=lambda x: (

                x["Relevance"],

                x["Weight"]

            ),

            reverse=True,

        )

        return articles[:5]
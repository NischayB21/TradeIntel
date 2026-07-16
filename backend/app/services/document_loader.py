from datetime import datetime, timedelta

from app.services.news_service import NewsService


class DocumentLoader:

    def __init__(self):

        self.news_service = NewsService()

    def load_news_documents(self, ticker):

        today = datetime.today().date()

        week_ago = today - timedelta(days=7)

        articles = self.news_service.get_news(

            ticker=ticker,

            from_date=str(week_ago),

            to_date=str(today),

        )

        documents = []

        for i, article in enumerate(articles):

            headline = article.get(
                "Headline",
                ""
            )

            summary = article.get(
                "Summary",
                ""
            )

            source = article.get(
                "Source",
                ""
            )

            weight = article.get(
                "Weight",
                1.0
            )

            published = article.get(
                "Published",
                ""
            )

            text = f"""
Headline:
{headline}

Summary:
{summary}

Source:
{source}

Published:
{published}

Importance Weight:
{weight}
"""

            documents.append(

                {

                    "id": f"{ticker}_{i}",

                    "text": text.strip(),

                    "metadata": {

                        "ticker": ticker,

                        "headline": headline,

                        "source": source,

                        "published": published,

                        "weight": weight,

                    },

                }

            )

        return documents
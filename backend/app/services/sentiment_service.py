from transformers import pipeline


class SentimentService:

    def __init__(self):

        self.classifier = pipeline(
            "text-classification",
            model="ProsusAI/finbert",
            tokenizer="ProsusAI/finbert",
        )

    def analyze(self, articles):

        results = []

        total_score = 0.0
        total_weight = 0.0

        for article in articles:

            text = (
                article["Headline"] +
                ". " +
                article["Summary"]
            )

            prediction = self.classifier(text)[0]

            label = prediction["label"]
            confidence = prediction["score"]

            if label == "positive":
                sentiment_score = confidence

            elif label == "negative":
                sentiment_score = -confidence

            else:
                sentiment_score = 0.0

            weight = article["Weight"]

            total_score += sentiment_score * weight
            total_weight += weight

            results.append(
                {
                    "Headline": article["Headline"],
                    "Sentiment": label.capitalize(),
                    "Confidence": round(confidence, 4),
                    "Weighted Score": round(
                        sentiment_score * weight,
                        4,
                    ),
                }
            )

        if total_weight == 0:

            overall_score = 0

        else:

            overall_score = total_score / total_weight

        if overall_score > 0.20:

            overall_label = "Positive"

        elif overall_score < -0.20:

            overall_label = "Negative"

        else:

            overall_label = "Neutral"

        return {

            "Overall Sentiment": overall_label,

            "Sentiment Score": round(
                overall_score,
                4,
            ),

            "Articles": results,

        }
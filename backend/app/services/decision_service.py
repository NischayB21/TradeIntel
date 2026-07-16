class DecisionService:

    def decide(
        self,
        technical_signal,
        predicted_return,
        confidence,
        news_sentiment,
        sentiment_score,
    ):

        technical_signal = technical_signal.upper()
        news_sentiment = news_sentiment.upper()

        recommendation = technical_signal
        risk = "MEDIUM"

        # -----------------------------
        # BUY Cases
        # -----------------------------

        if technical_signal == "STRONG BUY":

            if news_sentiment == "NEGATIVE":

                recommendation = "BUY"

                reason = (
                    "Strong technical indicators are partially "
                    "offset by negative recent news."
                )

            else:

                recommendation = "STRONG BUY"

                reason = (
                    "Strong technical indicators are supported "
                    "by market sentiment."
                )

        elif technical_signal == "BUY":

            if news_sentiment == "NEGATIVE":

                recommendation = "HOLD"

                reason = (
                    "Bullish technical indicators are weakened "
                    "by negative news sentiment."
                )

            else:

                recommendation = "BUY"

                reason = (
                    "Technical indicators and news sentiment "
                    "support a bullish outlook."
                )

        # -----------------------------
        # HOLD
        # -----------------------------

        elif technical_signal == "HOLD":

            recommendation = "HOLD"

            reason = (
                "Technical indicators do not provide a strong "
                "trading opportunity."
            )

        # -----------------------------
        # SELL
        # -----------------------------

        elif technical_signal == "SELL":

            if news_sentiment == "POSITIVE":

                recommendation = "HOLD"

                reason = (
                    "Bearish technical indicators are balanced "
                    "by positive market news."
                )

            else:

                recommendation = "SELL"

                reason = (
                    "Technical indicators and market sentiment "
                    "both indicate downside risk."
                )

        # -----------------------------
        # STRONG SELL
        # -----------------------------

        elif technical_signal == "STRONG SELL":

            if news_sentiment == "POSITIVE":

                recommendation = "SELL"

                reason = (
                    "Positive news slightly reduces downside "
                    "risk."
                )

            else:

                recommendation = "STRONG SELL"

                reason = (
                    "Strong bearish technical indicators are "
                    "supported by negative news."
                )

        # -----------------------------
        # Risk
        # -----------------------------

        if confidence >= 90:

            risk = "LOW"

        elif confidence >= 75:

            risk = "MEDIUM"

        else:

            risk = "HIGH"

        return {

            "Recommendation": recommendation,

            "Risk Level": risk,

            "Reason": reason,

        }
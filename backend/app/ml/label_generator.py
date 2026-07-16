import pandas as pd


class LabelGenerator:

    def generate_labels(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Creates the regression target.

        Target = Tomorrow's Percentage Return
        """

        df = df.copy()

        # Tomorrow's Close
        df["Tomorrow_Close"] = (
            df.groupby("Ticker")["Close"].shift(-1)
        )

        # Tomorrow's Return (%)
        df["Target_Return"] = (
            (df["Tomorrow_Close"] - df["Close"])
            / df["Close"]
        ) * 100

        # Remove rows without tomorrow's data
        df.dropna(inplace=True)

        return df
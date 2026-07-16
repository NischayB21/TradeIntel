import numpy as np
import pandas as pd
import ta


class FeatureService:

    def add_features(self, df: pd.DataFrame) -> pd.DataFrame:

        # -----------------------------
        # Basic Returns
        # -----------------------------
        df["Daily_Return"] = df["Close"].pct_change()

        # -----------------------------
        # Moving Averages
        # -----------------------------
        df["SMA_20"] = ta.trend.sma_indicator(
            close=df["Close"],
            window=20
        )

        df["EMA_20"] = ta.trend.ema_indicator(
            close=df["Close"],
            window=20
        )

        # -----------------------------
        # RSI
        # -----------------------------
        df["RSI"] = ta.momentum.rsi(
            close=df["Close"],
            window=14
        )

        # -----------------------------
        # MACD
        # -----------------------------
        df["MACD"] = ta.trend.macd(
            close=df["Close"]
        )

        # -----------------------------
        # Bollinger Bands
        # -----------------------------
        bb = ta.volatility.BollingerBands(
            close=df["Close"]
        )

        df["BB_High"] = bb.bollinger_hband()
        df["BB_Low"] = bb.bollinger_lband()

        # -----------------------------
        # ATR
        # -----------------------------
        atr = ta.volatility.AverageTrueRange(
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )

        df["ATR"] = atr.average_true_range()

        # -----------------------------
        # Volume Change
        # -----------------------------
        df["Volume_Change"] = df["Volume"].pct_change()

        # -----------------------------
        # Volatility
        # -----------------------------
        df["Volatility"] = (
            (df["High"] - df["Low"])
            / df["Close"]
        )

        # ===================================================
        # NEW FEATURES
        # ===================================================

        # Lag Features
        df["Close_Lag1"] = df["Close"].shift(1)
        df["Close_Lag2"] = df["Close"].shift(2)
        df["Close_Lag3"] = df["Close"].shift(3)

        df["Return_Lag1"] = df["Daily_Return"].shift(1)
        df["Return_Lag2"] = df["Daily_Return"].shift(2)
        df["Return_Lag3"] = df["Daily_Return"].shift(3)

        df["RSI_Lag1"] = df["RSI"].shift(1)
        df["MACD_Lag1"] = df["MACD"].shift(1)

        # Rolling Statistics
        df["Rolling_Mean_5"] = (
            df["Close"]
            .rolling(5)
            .mean()
        )

        df["Rolling_STD_5"] = (
            df["Close"]
            .rolling(5)
            .std()
        )

        # Momentum
        df["Momentum"] = (
            df["Close"]
            - df["Close"].shift(5)
        )

        # Rate of Change
        df["ROC"] = ta.momentum.ROCIndicator(
            close=df["Close"],
            window=10
        ).roc()

        # Money Flow Index
        df["MFI"] = ta.volume.MFIIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            volume=df["Volume"],
            window=14
        ).money_flow_index()

        # Commodity Channel Index
        df["CCI"] = ta.trend.CCIIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            window=20
        ).cci()

        # Average Directional Index
        df["ADX"] = ta.trend.ADXIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            window=14
        ).adx()

        # On Balance Volume
        df["OBV"] = ta.volume.OnBalanceVolumeIndicator(
            close=df["Close"],
            volume=df["Volume"]
        ).on_balance_volume()

        # -----------------------------
        # Clean Data
        # -----------------------------
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        df.dropna(inplace=True)

        return df
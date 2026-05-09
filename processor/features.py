import numpy as np


class FeatureEngine:

    def add_features(self, df):
        df = df.copy()

        # returns
        df["return"] = df["close"].pct_change()

        # log returns
        df["log_return"] = np.log(df["close"] / df["close"].shift(1))

        # volatility
        df["volatility_10"] = df["return"].rolling(10).std()

        # momentum
        df["momentum_5"] = df["close"] - df["close"].shift(5)

        # VWAP
        df["vwap"] = (df["close"] * df["volume"]).cumsum() / df["volume"].cumsum()

        # deviation from VWAP
        df["vwap_dist"] = df["close"] - df["vwap"]

        # range
        df["range"] = df["high"] - df["low"]

        return df.dropna()
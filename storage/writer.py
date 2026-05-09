import pandas as pd
import os

from config.settings import RAW_PATH, FEATURE_PATH


def save_raw_trades(buffer):
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)

    df = pd.DataFrame(buffer)

    if os.path.exists(RAW_PATH):
        old = pd.read_parquet(RAW_PATH)
        df = pd.concat([old, df], ignore_index=True)

    df.to_parquet(RAW_PATH, index=False)


def save_features(df):
    os.makedirs(os.path.dirname(FEATURE_PATH), exist_ok=True)

    if os.path.exists(FEATURE_PATH):
        old = pd.read_parquet(FEATURE_PATH)
        df = pd.concat([old, df], ignore_index=True)

    df.to_parquet(FEATURE_PATH, index=False)
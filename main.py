import asyncio
import pandas as pd

from collector.stream import TradeCollector
from processor.candles import CandleBuilder
from processor.features import FeatureEngine
from storage.writer import save_features


collector = TradeCollector()
candle_builder = CandleBuilder()
feature_engine = FeatureEngine()

candle_buffer = []


async def process_trade(trade):
    global candle_buffer

    candle = candle_builder.add_trade(trade)

    if candle:
        candle_buffer.append(candle)

        # keep rolling window
        if len(candle_buffer) > 200:
            df = pd.DataFrame(candle_buffer)

            df = feature_engine.add_features(df)

            save_features(df)

            print(f"📊 features updated: {len(df)} rows")


async def run():
    await collector.connect(process_trade)


if __name__ == "__main__":
    asyncio.run(run())
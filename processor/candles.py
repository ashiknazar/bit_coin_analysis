from collections import defaultdict


class CandleBuilder:
    def __init__(self):
        self.buckets = defaultdict(list)
        self.current_bucket = None

    def add_trade(self, trade):
        bucket = trade["timestamp"] // 1000

        if self.current_bucket is None:
            self.current_bucket = bucket

        # new candle
        if bucket != self.current_bucket:
            candle = self.build_candle(self.current_bucket)
            self.buckets[self.current_bucket] = []
            self.current_bucket = bucket
            self.buckets[bucket].append(trade)
            return candle

        self.buckets[bucket].append(trade)
        return None

    def build_candle(self, bucket):
        trades = self.buckets[bucket]

        if not trades:
            return None

        prices = [t["price"] for t in trades]
        volumes = [t["quantity"] for t in trades]

        return {
            "timestamp": bucket,
            "open": prices[0],
            "high": max(prices),
            "low": min(prices),
            "close": prices[-1],
            "volume": sum(volumes),
            "trade_count": len(trades)
        }
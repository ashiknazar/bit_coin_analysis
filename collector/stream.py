import json
import websockets
from collections import deque

from config.settings import WS_URL, BUFFER_SIZE
from storage.writer import save_raw_trades


class TradeCollector:
    def __init__(self):
        self.buffer = deque(maxlen=BUFFER_SIZE)

    async def connect(self, callback):
        async with websockets.connect(WS_URL, ping_interval=20) as ws:
            print("✅ Connected to Binance WebSocket")

            counter = 0

            while True:
                msg = await ws.recv()
                data = json.loads(msg)

                trade = self.normalize(data)

                self.buffer.append(trade)
                counter += 1

                # batch persist
                if counter % 200 == 0:
                    save_raw_trades(list(self.buffer))
                    print("💾 raw trades saved")

                await callback(trade)

    def normalize(self, data):
        return {
            "timestamp": data["T"],
            "price": float(data["p"]),
            "quantity": float(data["q"]),
            "is_buyer_maker": data["m"],
            "trade_id": data["t"]
        }
import ccxt
import pandas as pd


class PriceService:

    def __init__(self):
        self.exchange = ccxt.binance()

    def get_ohlcv(self, symbol="BTC/USDT", timeframe="5m", limit=1000):

        candles = self.exchange.fetch_ohlcv(
            symbol,
            timeframe=timeframe,
            limit=limit
        )

        df = pd.DataFrame(
            candles,
            columns=[
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            ]
        )

        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        # Create amount column ourselves
        df["amount"] = df["close"] * df["volume"]

        return df
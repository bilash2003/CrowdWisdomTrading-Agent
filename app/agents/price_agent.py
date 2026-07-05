from app.services.price_service import PriceService


class PriceAgent:

    def __init__(self):
        self.service = PriceService()

    def execute(self, asset):

        symbol = f"{asset.upper()}/USDT"

        df = self.service.get_ohlcv(symbol)

        return {
            "asset": asset.upper(),
            "bars": len(df),
            "latest_close": float(df.iloc[-1]["close"])
        }
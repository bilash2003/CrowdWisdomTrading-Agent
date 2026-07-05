from app.services.price_service import PriceService
from app.services.kronos_service import KronosService
from app.agents.risk_agent import RiskAgent


class PredictionAgent:

    def __init__(self):
        self.price_service = PriceService()
        self.kronos_service = KronosService()
        self.risk = RiskAgent()

    def execute(self, asset: str):

        symbol = f"{asset.upper()}/USDT"

        df = self.price_service.get_ohlcv(
            symbol=symbol,
            timeframe="5m",
            limit=1000
        )
        print(df.columns)
        print(df.head())

        prediction = self.kronos_service.predict(df)

        risk = self.risk.calculate(
            prediction["confidence"]
        )

        return {
            "asset": asset.upper(),
            "prediction": prediction,
            "risk": risk
        }
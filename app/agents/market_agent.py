from app.services.market_service import MarketService
from app.utils.logger import logger
from app.services.polymarket_service import PolymarketService


class MarketAgent:

    def __init__(self):
        self.market_service = MarketService()

    def execute(self, asset: str):

        logger.info(f"Searching markets for {asset}")

        result = self.market_service.search_markets(asset)

        logger.info("Market search completed")

        return result
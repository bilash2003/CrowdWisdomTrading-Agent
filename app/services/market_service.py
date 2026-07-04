from app.services.polymarket_service import PolymarketService


class MarketService:

    def __init__(self):
        self.polymarket = PolymarketService()

    def search_markets(self, asset: str):

        polymarket_results = self.polymarket.search_market(asset)

        return {
            "asset": asset.upper(),
            "markets": polymarket_results
        }
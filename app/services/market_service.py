from typing import Dict, List


class MarketService:

    def search_markets(self, asset: str) -> Dict:
        """
        Temporary mock implementation.
        Later this will call Polymarket and Kalshi APIs.
        """

        return {
            "asset": asset.upper(),
            "markets": [
                {
                    "platform": "Polymarket",
                    "question": f"Will {asset.upper()} go UP in the next 5 minutes?",
                    "probability": 0.61,
                },
                {
                    "platform": "Kalshi",
                    "question": f"Will {asset.upper()} close higher?",
                    "probability": 0.58,
                },
            ],
        }
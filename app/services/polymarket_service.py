import requests


class PolymarketService:
    BASE_URL = "https://gamma-api.polymarket.com"

    def search_market(self, asset: str):
        """
        Search active Polymarket markets for a crypto asset.
        """

        try:
            response = requests.get(
                f"{self.BASE_URL}/markets",
                params={
                    "active": "true",
                    "closed": "false",
                    "limit": 100
                },
                timeout=10
            )

            response.raise_for_status()

            markets = response.json()

            asset = asset.upper()

            keywords = {
                    "BTC": ["BTC", "BITCOIN"],
                    "ETH": ["ETH", "ETHEREUM"]
            }

            search_terms = keywords.get(asset, [asset])

            results = []

            for market in markets:

                question = market.get("question", "")

                if any(term in question.upper() for term in search_terms):

                    prices = market.get("outcomePrices")

                    probability = None

                    if prices:
                        try:
                            # outcomePrices may already be a list or a JSON string.
                            if isinstance(prices, str):
                                import json
                                prices = json.loads(prices)

                            probability = float(prices[0])

                        except Exception:
                            probability = None

                    results.append({
                        "platform": "Polymarket",
                        "question": question,
                        "probability": probability,
                        "url": f"https://polymarket.com/event/{market.get('slug', '')}"
                    })

            return results

        except Exception as e:

            return [{
                "platform": "Polymarket",
                "error": str(e)
            }]
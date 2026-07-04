from app.services.apify_service import ApifyService


class DataAgent:

    def __init__(self):
        self.apify = ApifyService()

    def health(self):
        return {
            "status": "connected",
            "service": "Apify"
        }
from apify_client import ApifyClient
from app.utils.config import APIFY_TOKEN


class ApifyService:

    def __init__(self):
        self.client = ApifyClient(APIFY_TOKEN)

    def get_client(self):
        return self.client
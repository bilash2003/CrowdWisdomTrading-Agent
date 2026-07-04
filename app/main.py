from fastapi import FastAPI
from app.utils.logger import logger
from app.agents.market_agent import MarketAgent

market_agent = MarketAgent()

app = FastAPI(
    title="CrowdWisdom Trading Agent",
    version="1.0.0"
)


@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "status": "running",
        "project": "CrowdWisdomTrading Crypto Agent"
    }
    

@app.get("/market/{asset}")
def get_market(asset: str):

    return market_agent.execute(asset)
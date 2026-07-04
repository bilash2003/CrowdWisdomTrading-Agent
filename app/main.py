from fastapi import FastAPI
from app.utils.logger import logger
from app.agents.market_agent import MarketAgent

from app.agents.llm_agent import LLMAgent

llm_agent = LLMAgent()


market_agent = MarketAgent()

app = FastAPI(
    title="CrowdWisdom Trading Agent",
    version="1.0.0"
)

@app.get("/ask")
def ask(question: str):

    return {
        "answer": llm_agent.ask(question)
    }


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
from fastapi import FastAPI
from app.utils.logger import logger
from app.agents.market_agent import MarketAgent

from app.agents.llm_agent import LLMAgent
from app.agents.price_agent import PriceAgent
from app.agents.prediction_agent import PredictionAgent


from app.agents.data_agent import DataAgent
llm_agent = LLMAgent()
market_agent = MarketAgent()
price_agent = PriceAgent()
prediction_agent = PredictionAgent()
data_agent = DataAgent()

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

@app.get("/apify")
def apify_status():
    return data_agent.health()

@app.get("/price/{asset}")
def price(asset: str):
    return price_agent.execute(asset)

@app.get("/predict/{asset}")
def predict(asset: str):

    return prediction_agent.execute(asset)
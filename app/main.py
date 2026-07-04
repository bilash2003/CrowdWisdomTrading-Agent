from fastapi import FastAPI
from app.utils.logger import logger

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
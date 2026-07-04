from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CrowdWisdomTrading Agent Running"}
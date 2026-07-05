📊 CrowdWisdom Trading Agent
🚀 Introduction
CrowdWisdom Trading Agent is an AI-powered crypto trading intelligence system that combines:
📈 Real-time market data (Binance via CCXT)
🧠 Machine Learning forecasting (Kronos Time-Series Model)
📊 Market sentiment (Polymarket / external prediction markets)
⚖️ Risk management (Kelly-based position sizing)
🤖 LLM-based reasoning layer (optional Q&A assistant)

The system analyzes assets like BTC/USDT and produces:
Direction (UP / DOWN)
Confidence score
Predicted price movement
Risk-adjusted position sizing
🎯 Why This Project?

Traditional trading systems rely only on:
Technical indicators ❌
Human intuition ❌
Static rules ❌

This project introduces:
✔ Crowd + AI Hybrid Intelligence

Combines:
Market data (truth)
Prediction markets (crowd wisdom)
AI forecasting models
✔ Automated decision pipeline

No manual analysis needed.
✔ Risk-aware trading

Not just prediction → but how much to invest safely

💡 Key Features
Real-time OHLCV data fetching (Binance)
Time-series forecasting using Kronos model
Market sentiment integration (Polymarket)
Risk engine using Kelly Criterion
Modular agent-based architecture
FastAPI backend for real-time API access
🧠 System Architecture

📌 High-Level Flow
 <p align="center">
  <img src="pic/High level flow.png" width="500">
</p>


🏗 Architecture Diagram
<p align="center">
  <img src="pic/Architecture Diagram.png" width="500">
</p>
              
⚙️ System Pipeline
1️⃣ Data Layer
Fetches live crypto OHLCV data
Source: Binance via CCXT
PriceService → get_ohlcv()
2️⃣ Market Intelligence Layer
Fetches prediction market sentiment
Source: Polymarket API
MarketService → search_markets()
3️⃣ AI Prediction Layer
Kronos Transformer-based time series model
Predicts next price movement
KronosService → predictor.predict()
4️⃣ Risk Management Layer
Converts confidence → position sizing
RiskAgent → Kelly Criterion
5️⃣ API Layer

FastAPI endpoints:

Endpoint	Description
/market/{asset}	Market sentiment
/price/{asset}	OHLCV data
/predict/{asset}	Full prediction + risk
/ask	LLM assistant
🧪 Example Output
{
  "asset": "BTC",
  "prediction": {
    "direction": "DOWN",
    "confidence": 0.0185,
    "current_price": 62734.01,
    "predicted_price": 61572.19,
    "expected_change_percent": -1.85
  },
  "risk": {
    "kelly_fraction": 0.12,
    "recommended_position_percent": 12
  }
}
🛠 Technologies Used
Backend
FastAPI
Uvicorn
Data Engineering
Pandas
NumPy
CCXT (Binance API)
AI / ML
PyTorch
HuggingFace Transformers
Kronos Time-Series Model
Infrastructure
Python 3.11+
Virtual Environment (venv)
🔁 System Workflow
1. User calls API (/predict/BTC)
2. Fetch OHLCV market data
3. Fetch sentiment (Polymarket)
4. Run Kronos model prediction
5. Calculate confidence score
6. Apply risk engine (Kelly Criterion)
7. Return final trading signal
📊 Benefits of This Project
💰 Trading Intelligence
Combines AI + crowd wisdom
More robust than single indicator systems
⚡ Real-time Decision System
Live API-based architecture
🧠 Modular AI system
Each component is independent (agents)
📉 Risk-controlled output
Prevents over-trading
Capital protection focused
📂 Project Structure
CrowdWisdomTrading-Agent/
│
├── app/
│   ├── agents/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── Kronos/               # AI model module
├── data/
├── logs/
├── texts/
├── venv/
└── README.md
🚀 Future Improvements
Add live trading execution (Binance orders)
Add reinforcement learning agent
Improve risk model (VaR / CVaR)
Add dashboard UI (React / Streamlit)
Deploy on cloud (AWS / Render / Railway)

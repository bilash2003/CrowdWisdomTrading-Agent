import os
import sys
import pandas as pd

from app.utils.logger import logger

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

KRONOS_PATH = os.path.join(PROJECT_ROOT, "Kronos")

if KRONOS_PATH not in sys.path:
    sys.path.insert(0, KRONOS_PATH)

from model import Kronos, KronosTokenizer, KronosPredictor


class KronosService:

    def __init__(self):

        logger.info("Loading Kronos model...")

        self.tokenizer = KronosTokenizer.from_pretrained(
            "NeoQuasar/Kronos-Tokenizer-base"
        )

        self.model = Kronos.from_pretrained(
            "NeoQuasar/Kronos-small"
        )

        self.predictor = KronosPredictor(
            self.model,
            self.tokenizer,
            max_context=512
        )

        logger.info("✅ Kronos model loaded.")

    def predict(self, df: pd.DataFrame):

        lookback = 400
        pred_len = 24

        if len(df) < lookback + pred_len:
            raise Exception("Not enough market data for Kronos.")

        x_df = df.iloc[:lookback][
            ["open", "high", "low", "close", "volume", "amount"]
        ]

        x_timestamp = df.iloc[:lookback]["timestamp"]

        last_time = x_timestamp.iloc[-1]

        y_timestamp = pd.Series(
            pd.date_range(
                start=last_time + pd.Timedelta(minutes=5),
                periods=pred_len,
                freq="5min"
            )
        )

        pred_df = self.predictor.predict(
            df=x_df,
            x_timestamp=x_timestamp,
            y_timestamp=y_timestamp,
            pred_len=pred_len,
            T=1.0,
            top_p=0.9,
            sample_count=1,
            verbose=False
        )

        current_price = float(df["close"].iloc[-1])

        predicted_price = float(pred_df["close"].iloc[-1])

        change = (
            predicted_price - current_price
        ) / current_price

        direction = "UP" if change > 0 else "DOWN"

        confidence = round(abs(change), 4)

        return {
            "direction": direction,
            "confidence": confidence,
            "current_price": round(current_price, 2),
            "predicted_price": round(predicted_price, 2),
            "expected_change_percent": round(change * 100, 2)
        }
import pandas as pd
import numpy as np

from market.repositories.candle_repository import CandleRepository

class MarketAnalysisService:

    def __init__(
            self,
            pair,
            timeframe="H1"
        ):
        self.pair = pair
        self.timeframe = timeframe

        # _____________________________
        # Load Data
        # _____________________________
    def load_dataframe(self):
        candles = CandleRepository.dataframe(
            self.pair,
            self.timeframe
        )

        data = list(
            candles.values(
                "timestamp",
                "open",
                "high",
                "low",
                "close",
                "volume"
            )
        )

        df = pd.DataFrame(data)

        return df
    
    # Clean Data
    def clean_dataframe(self, df):
        if df.empty:
            return df
        
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.sort_values("timestamp")
        df.set_index(
            "timestamp",
            inplace=True
        )
        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col])

        df = df.drop_duplicates()
        df = df.dropna()

        return df
    
    def analysee(self):
        df = self.load_dataframe()
        df = self.clean_dataframe(df)
        return df
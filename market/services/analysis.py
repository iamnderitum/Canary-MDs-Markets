import pandas as pd
import numpy as np

from market.repositories.candle_repository import CandleRepository
from market.indicators.rsi import RSI
from market.indicators.ema import EMA

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
        queryset = CandleRepository.dataframe(
            self.pair,
            self.timeframe
        )
        dataframe = pd.DataFrame(
            list(
                queryset.values(
                    "timestamp",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume"
                )
            )
        )

        dataframe["timestamp"] = pd.to_datetime(
            dataframe["timestamp"]
        )
        dataframe.set_index(
            "timestamp",
            inplace=True
        )

        dataframe.sort_index(
            inplace=True
        )

        numeric = [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        dataframe[numeric] = dataframe[numeric].apply(
            pd.to_numeric
        )

        dataframe.drop_duplicates()
        dataframe.dropna()

        return dataframe

    
    # # Clean Data
    # def clean_dataframe(self, df):
    #     if df.empty:
    #         return df
        
    #     df["timestamp"] = pd.to_datetime(df["timestamp"])
    #     df.sort_values("timestamp")
    #     df.set_index(
    #         "timestamp",
    #         inplace=True
    #     )
    #     numeric_columns = [
    #         "open",
    #         "high",
    #         "low",
    #         "close",
    #         "volume"
    #     ]

    #     for col in numeric_columns:
    #         df[col] = pd.to_numeric(df[col])

    #     df = df.drop_duplicates()
    #     df = df.dropna()

    #     return df
    
    def analyze(self):
        dataframe = self.load_dataframe()
        indicators = [
            EMA(20),
            EMA(50),
            RSI()
        ]
        for indicator in indicators:
            dataframe = indicator.calculate(
                dataframe
            )

        return dataframe
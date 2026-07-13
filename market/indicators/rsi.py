import pandas as pd
from .base import Indicator

class RSI(Indicator):
    def __init__(self, period=14, source="close"):
        self.period = period
        self.source = source

    def calculate(self, dataframe):
        delta = dataframe[self.source].diff()
        gain = delta.clip(lower=0)
        loss = delta.clip(upper=0)

        average_gain = gain.rolling(
            self.period
        ).mean()

        average_loss = loss.rolling(
            self.period
        ).mean()

        rs = average_gain / average_loss

        dataframe["RSI"] = (
            100 -
            (
                100 /
                (
                    1 + rs
                )
            )
        )

        return dataframe
    

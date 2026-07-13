import pandas as pd
from .base import Indicator

class EMA(Indicator):

    def __init__(self,period, source="close"):
        self.period = period
        self.source = source

    @property
    def column_name(self):
        return f"EMA{self.period}"
    
    def calculate(self, dataframe):
        dataframe[self.column_name] = (
            dataframe[self.source]
            .ewm(
                span=self.period,
                adjust=False
            )
            .mean()
        )
        return dataframe
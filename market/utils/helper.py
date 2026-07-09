from decimal import Decimal
from django.utils.dateparse import parse_datetime

def parse_candle(pair, timeframe, candle):
    mid = candle["mid"]

    return {
        "pair": pair,
        "timeframe": timeframe,
        "timestamp": parse_datetime(candle["time"]),
        "open": Decimal(mid["o"]),
        "high":Decimal(mid["h"]),
        "low":Decimal(mid["l"]),
        "close":Decimal(mid["c"]),
        "volume":candle["volume"],
        "complete":candle["complete"]
    }
from market.brokers.oanda import OandaBroker
from market.brokers.mt5 import MT5Broker
from market.models import Candle
from market.repositories.candle_repository import CandleRepository
from market.repositories.pair_repository import PairRepository
from market.utils.helper import parse_candle

class MarketLoader:

    def __init__(self):
        self.broker = MT5Broker()

    def load_candles(self, instrument, timeframe="H1", count=500):
        pair = PairRepository.get_or_create(
            instrument,
            instrument
        )

        response = self.broker.get_candles(
            instrument=instrument,
            granularity=timeframe,
            count=count
        )

        candles = []
            
        for item in response["candles"]:
            data = parse_candle(
                pair,
                timeframe,
                item
            )

            candles.append(
                Candle(**data)
            )

        CandleRepository.bulk_insert(
            candles
            )

        return len(candles)
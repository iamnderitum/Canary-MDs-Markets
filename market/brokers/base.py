from abc import ABC
from abc import abstractmethod

class BrokerInterface(ABC):
    @abstractmethod
    def get_account(self):
        pass

    @abstractmethod
    def get_instruments(self):
        pass

    @abstractmethod
    def get_candles(
            self,
            instrument,
            granularity,
            count=500
        ):
        pass

    @abstractmethod
    def get_latest_price(
            self,
            instrument
        ):
        pass
    @abstractmethod
    def place_order(
            self,
            order_date
        ):
        pass
import MetaTrader5 as mt5
from datetime import datetime

from .base import BrokerInterface

TIMEFRAME_MAPPING = {
    "M1":mt5.TIMEFRAME_M1,
    "M5":mt5.TIMEFRAME_M5,
    "M15":mt5.TIMEFRAME_M15,
    "M30":mt5.TIMEFRAME_M30,
    "H1":mt5.TIMEFRAME_H1,
    "M4":mt5.TIMEFRAME_H4,
    "D1":mt5.TIMEFRAME_D1,
}

class MT5Broker(BrokerInterface):
    def __init__(self):
        if not mt5.initialize():
            raise Exception(
                f"MT5 initialization failed: {mt5.last_error()}"
            )
        
    def get_account(self):
        account = mt5.account_info()

        if account is None:
            return None
        
        return account._asdict()
    
    def get_instruments(self):
        symbols = mt5.symbols_get()

        return [
            symbol._asdict()
            for symbol in symbols
        ]
    
    def get_candles(self, instrument, granularity, count=500):
        timeframe = TIMEFRAME_MAPPING[granularity]
        rates = mt5.copy_rates_from_pos(
            instrument, 
            timeframe,
            0,
            count
        )
        if rates is None:
            return{
                "candles": []
            }
        
        candles = []
        for rate in rates:
            candles.append({
                "complete": True,
                "volume": int(rate["tick_volume"]),
                "time": datetime.utcfromtimestamp(
                    rate["time"]
                ).isoformat(),

                "mid": {
                    "o": str(rate["open"]),
                    "h": str(rate["high"]),
                    "l": str(rate["low"]),
                    "c": str(rate["close"]),
                }
            })

        return {
            "candles": candles
        }
    
    def get_latest_price(self, instrument):
        tick = mt5.symbol_info_tick(instrument)
        if tick is None:
            return None
        
        return {
            "bid":tick.bid,
            "ask":tick.ask,
            "time": tick.time
        }
    
    def place_order(self, order_date):
        raise NotImplementedError(
            "Will Implement Later"
        )
    
    def shutdown(self):
        mt5.shutdown()
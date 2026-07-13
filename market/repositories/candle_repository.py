from django.db import transaction
from market.models import Candle

class CandleRepository:

    @staticmethod
    def latest(pair, timeframe):
        return Candle.objects.filter(
            pair=pair,
            timeframe=timeframe
        ).order_by("-timestamp").first()
    
    @staticmethod
    def history(pair, timeframe, limit=None):
        queryset = Candle.objects.filter(
            pair=pair,
            timeframe=timeframe
        ).order_by("timestamp")

        if limit:
            queryset = queryset[:limit]

        return queryset
    
    @staticmethod
    @transaction.atomic()
    def bulk_insert(candles):
        Candle.objects.bulk_create(
            candles,
            ignore_conflicts=True,
            batch_size=1000
        )

    @staticmethod
    def count(pair):
        return Candle.objects.filter(
            pair=pair
        ).count()
    
    @staticmethod
    def dataframe(pair, timeframe):
        return Candle.objects.filter(
            pair__name=pair,
            timeframe=timeframe
        ).order_by("timestamp")
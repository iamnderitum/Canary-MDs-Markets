from typing import Optional
from market.models import CurrencyPair

class PairRepository:

    @staticmethod
    def get(symbol: str) -> Optional[CurrencyPair]:
        return CurrencyPair.objects.filter(
            name=symbol
        ).first()
    
    @staticmethod
    def get_or_create(symbol:str, display_name: str=None):
        pair, _ = CurrencyPair.objects.get_or_create(
            name=symbol,
            defaults={
                "display_name": display_name or symbol
            }
        )

        return pair
    
    def all():
        return CurrencyPair.objects.filter(
            is_active=True
        )
    
    @staticmethod
    def deactivate(pair):
        pair.is_active = False
        pair.save(update_fields=["is_active"])
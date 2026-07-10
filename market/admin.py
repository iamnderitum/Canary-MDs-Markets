from django.contrib import admin
from .models import CurrencyPair, Candle
# Register your models here.

@admin.register(CurrencyPair)
class CurrencyPairAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        "display_name",
        "pip_location",
        "display_precision",
        "created_at"
    ]
@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = [
        "pair",
        "timeframe",
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "complete",

    ]
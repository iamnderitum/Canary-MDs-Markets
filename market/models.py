from django.db import models

class CurrencyPair(models.Model):
    """
    Example:
        EUR_USD
        GBP_USD
        USD_JPY
    """

    name = models.CharField(max_length=20, unique=True)
    display_name = models.CharField(max_length=30)

    pip_location = models.IntegerField(default=-4)
    display_precision = models.IntegerField(max_length=5,default=5)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        app_label = "CurrencyPair"

    def __str__(self):
        return self.display_name
    
class Candle(models.Model):
    pair = models.ForeignKey(
        CurrencyPair,
        on_delete=models.CASCADE,
        related_name="candles"
    )
    timeframe = models.CharField(max_length=10)
    timestamp = models.DateTimeField()

    open = models.DecimalField(
        max_digits=15,
        decimal_places=8
    )
    high = models.DecimalField(
        max_digits=15,
        decimal_places=8
    )
    low = models.DecimalField(
        max_digits=15,
        decimal_places=8
    )
    close = models.DecimalField(
        max_digits=15,
        decimal_places=8
    )

    volume = models.PositiveIntegerField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "Candle"
        ordering = ["timestamp"]
        indexes = [
            models.Index(fields=["pair", "timestamp"]),
            models.Index(fields=["timeframe"]),
        ]

        unique_together = (
            "pair",
            "timeframe",
            "timestamp",
        )

    def __str__(self):
        return f"{self.pair.name} {self.timestamp}"
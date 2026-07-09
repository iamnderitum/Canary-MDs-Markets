from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from market.services.loader import MarketLoader

class Command(BaseCommand):
    """
    fetch market candles from broker and save to PostgreSQL.

    Example:
    python manage.py fetch_candles EURUSD

    python manage.py fetch_candles EURUSD --timeframe H1

    python manage.py fetch_candles GBPUSD --timeframe M15 --count 1000
    """

    help = "Download Candles from broker and store them"

    def add_arguments(self, parser):
        parser.add_argument(
            "instrument",
            type=str,
            help="Currency pair e.g EURUSD"
        )

        parser.add_argument(
            "--timeframe",
            default="H1",
            type=str,
            help="M1, M5, M15, M30, H1, H4, D1"
        )

        parser.add_argument(
            "--count",
            default=500,
            type=int,
            help="Number of candles"
        )

    def handle(self, *args, **options):
        instrument = options["instrument"]
        timeframe = options["timeframe"]
        count = options["count"]

        self.stdout.write("===========================")
        self.stdout.write("   Market Data Loader")
        self.stdout.write("===========================")

        self.stdout.write(
            self.style.WARNING(
                f"Instrument : {instrument}"
            )
        )

        self.stdout.write(
            self.style.WARNING(
                f"Timeframe : {timeframe}"
            )
        )

        self.stdout.write(
            self.style.WARNING(
                f"Candles : {count}"
            )
        )

        loader = MarketLoader()

        try:
            inserted = loader.load_candles(
                instrument=instrument,
                timeframe=timeframe,
                count=count
            )
            self.stdout.write("")

            self.stdout.write(
            self.style.SUCCESS(
                f"Successfully fetched : {inserted} candles"
                )
            )

        except Exception as exc:
            raise CommandError(str(exc))
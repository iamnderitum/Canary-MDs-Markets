from django.core.management.base import BaseCommand
from market.services.analysis import MarketAnalysisService

class Command(BaseCommand):
    help = "Analyze stored market Candles"

    def add_arguments(self, parser):

        parser.add_argument(
            "pair",
            type=str,
            help="Currency Pair"
        )

        parser.add_argument(
            "--timeframe",
            default="H1",
            type=str,
            help="Major TF"
        )

    def handle(self, *args, **options):
        pair = options["pair"]
        timeframe = options["timeframe"]

        self.stdout.write("=" *60)
        self.stdout.write(f"Analyzing {pair} ({timeframe})")
        self.stdout.write("=" *60)

        analysis = MarketAnalysisService(
            pair=pair,
            timeframe=timeframe
        )

        df = analysis.analyze()

        if df.empty:
            self.stdout.write(
                self.style.ERROR("No candle data found")
            )
            return
        
        self.stdout.write("")
        self.stdout.write("Latest 10 candles with indicators:")
        self.stdout.write("")

        print(
            df[
                [
                    "close",
                    "EMA20",
                    "EMA50",
                    "RSI"
                ]
            ].tail(10)
        )

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Analysis completed Successfully"))
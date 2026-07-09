import requests
from django.conf import settings
from .base import BrokerInterface

class OandaBroker(BrokerInterface):
    BASE_URL = "https://api-fxpractive.oanda.com/v3"

    def __init__(self):
        self.account_id = settings.OANDA_ACCOUNT_ID
        self.api_key = settings.OANDA_API_KEY
        self.headers = {
            "Authorization": f"Bearer{self.api_key}",
            "Content-Type": "application/json"
        }

    def get_account(self):
        endpoint = (
            f"{self.BASE_URL}/accounts/{self.account_id}"
        )
        response = requests.get(
            endpoint,
            headers=self.headers
        )
        response.raise_for_status()

        return response.json()
    
    def get_instrumens(self):
        endpoint = (
            f"{self.BASE_URL}/accounts"
            f"{self.account_id}/instruments"
        )
        response = requests.get(
            endpoint,
            headers=self.headers
        )
        response.raise_for_status()

        return response.json()
    
    def get_candles(self, instrument, granularity="H1", count=500):
        endpoint = (
            f"{self.BASE_URL}/"
            f"instruments/{instrument}/candles"
        )
        params = {
            "granularity": granularity,
            "count": count,
            "price": "M"
        }

        response = requests.get(
            endpoint,
            params=params,
            headers=self.headers
        )
        response.raise_for_status()

        return response.json()
    
    def get_latest_price(self, instrument):
        endpoint = (
            f"{self.BASE_URL}/accounts/"
            f"{self.account_id}/pricing"
        )
        params = {
            "instruments":instrument
        }

        response = requests.get(
            endpoint,
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def place_order(self, order_date):
        endpoint = (
            f"{self.BASE_URL}/accounts/"
            f"{self.account_id}/orders"
        )

        response = requests.post(
            endpoint,
            headers=self.headers,
            json=order_date
        )
        response.raise_for_status()

        return response.json()
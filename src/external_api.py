import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]

API_URL = "https://api.apilayer.com/exchangerates_data/latest"
HEADERS = {"apikey": API_KEY}


def get_exchange_rate(currency: str) -> float:
    """Получает текущий курс валюты к рублю через Exchange Rates Data API"""
    response = requests.get(API_URL, headers=HEADERS, params={"base": currency, "symbols": "RUB"})
    response.raise_for_status()
    data = response.json()
    return float(data["rates"]["RUB"])


def convert_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях с конвертацией иностранной валюты"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    exchange_rate = get_exchange_rate(currency)
    return amount * exchange_rate

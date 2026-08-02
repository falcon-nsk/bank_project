"""
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
"""
from typing import Iterator

# filter_by_currency

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Args:
        transactions: Список словарей.
        currency: Код валюты для фильтрации (например, USD).
    Returns:
        Итератор транзакций, соответствующих указанной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

# transaction_descriptions

"""
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
"""

def transaction_descriptions(transactions: list[dict]) -> str:

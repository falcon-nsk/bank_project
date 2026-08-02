import pytest

from src.generators import filter_by_currency, transaction_descriptions

@pytest.fixture
def transactions():
    return [
        {
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
            },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                    }
                },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

# filter_by_currency


def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    transaction = next(usd_transactions)
    assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_currency(transactions):
    no_currency_transactions = filter_by_currency(transactions, currency="EUR")
    assert list(no_currency_transactions) == []


def test_filter_by_currency_empty_transactions():
    empty_transactions = filter_by_currency([], "USD")
    assert list(empty_transactions) == []


"""
@pytest.mark.parametrize(
    "index, expected_description",
    [(0, "Перевод организации"), (1, "Перевод со счета на счет")]
)
def test_transaction_descriptions(transactions: list[dict], expected_description: str) -> None:
    descriptions = transaction_descriptions(transactions)
    for _ in range("index"):

    assert next(descriptions) == expected_description
"""

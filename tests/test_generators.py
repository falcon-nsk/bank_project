import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


# filter_by_currency


def test_filter_by_currency_usd(transactions: list[dict]) -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    transaction = next(usd_transactions)
    assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_currency(transactions: list[dict]) -> None:
    no_currency_transactions = filter_by_currency(transactions, currency="EUR")
    assert list(no_currency_transactions) == []


def test_filter_by_currency_empty_transactions() -> None:
    empty_transactions = filter_by_currency([], "USD")
    assert list(empty_transactions) == []


# transaction_descriptions


def test_transaction_descriptions(transactions: list[dict]) -> None:
    descriptions = transaction_descriptions(transactions)
    expected_1 = next(descriptions)
    expected_2 = next(descriptions)
    assert expected_1 == "Перевод организации"
    assert expected_2 == "Перевод со счета на счет"


def test_transaction_descriptions_empty_transactions() -> None:
    empty_descriptions = transaction_descriptions([])
    assert list(empty_descriptions) == []


# card_number_generator


@pytest.mark.parametrize("start, stop, expected", [(1, 1, "0000 0000 0000 0001")])
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    card_number = card_number_generator(start, stop)
    assert next(card_number) == expected


@pytest.mark.parametrize("start, stop", [(1, 1), (9999999999999998, 9999999999999999)])
def test_card_number_generator_spaces(start: int, stop: int) -> None:
    card_number = next(card_number_generator(start, stop))
    assert len(card_number.split(" ")) == 4


@pytest.mark.parametrize("start, stop", [(9999999999999998, 9999999999999999)])
def test_card_number_generator_values_of_range(start: int, stop: int) -> None:
    cards = card_number_generator(start, stop)
    card_number_1 = next(cards)
    card_number_2 = next(cards)
    assert card_number_1 == "9999 9999 9999 9998"
    assert card_number_2 == "9999 9999 9999 9999"


def test_card_number_generator_stop_iteration() -> None:
    cards = card_number_generator(9999999999999999, 9999999999999999)
    next(cards)
    with pytest.raises(StopIteration):
        next(cards)

from typing import Iterator

# filter_by_currency


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Принимает на вход список словарей, представляющих транзакции.
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


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями.
    Args:
        transactions: Список словарей.
    Returns:
        Итератор описаний операций.
    """
    for transaction in transactions:
        yield transaction["description"]


# card_number_generator


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.
    Args:
        start: Начальное значение для генерации диапазона номеров.
        end: Конечное значение для генерации диапазона номеров.
    Returns:
        Итератор номеров банковских карт в формате XXXX XXXX XXXX XXXX,
        где X — цифра номера карты.
    """
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        parts_card_number = [card_number[0:4], card_number[4:8], card_number[-8:-4], card_number[-4:]]
        card_number = " ".join(parts_card_number)
        yield card_number

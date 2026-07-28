"""
print(get_mask_card_number("7000792289606361")) #Проверка файла masks
print(get_mask_account("3654108430135874305"))

from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361")) #Проверка файла widget
print(get_date("2024-03-11T02:26:18.671407")) #Получение даты
"""

import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected", [("7000792289606361", "7000 79** **** 6361"), ("1000792289606234", "1000 79** **** 6234")]
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        ("70007922896063"),
        ("10007922896062345"),
    ],
)
def test_get_wrong_len_mask_card_number(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [("700079228960636A"), ("1000792-89606234")])
def test_get_mask_card_number_with_symbols(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", ["", "  "])
def test_get_zero_len_mask_card_number(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)

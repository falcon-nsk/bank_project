"""
print(get_mask_card_number("7000792289606361")) #Проверка файла masks
print(get_mask_account("3654108430135874305"))

from src.widget import get_date, mask_account_card

<<<<<<< HEAD
print(mask_account_card("Visa Platinum 7000792289606361")) #Проверка файла widget
print(get_date("2024-03-11T02:26:18.671407")) #Получение даты
"""

import pytest

from src.masks import get_mask_account, get_mask_card_number

# get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected", [("7000792289606361", "7000 79** **** 6361"), ("1000792289606234", "1000 79** **** 6234")]
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [("70007922896063"), ("10007922896062345")])
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


# get_mask_account


@pytest.mark.parametrize(
    "account_number, expected", [("73654108430135874305", "**4305"), ("73654108430135875467", "**5467")]
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number, expected", [("73654108430135874305", "**4305"), ("7365 4108 4301 3587 4305", "**4305")]
)
def test_get_mask_account_with_spaces(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [("736541084301358743"), ("736541084301358754677")])
def test_get_wrong_len_mask_account(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@pytest.mark.parametrize("account_number", [("7365410843013587430A"), ("736541084-0135874305")])
def test_get_mask_account_with_symbols(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@pytest.mark.parametrize("account_number", ["", "  "])
def test_get_zero_len_mask_account(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)

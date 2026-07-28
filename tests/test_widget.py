import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(info: str, expected: str) -> None:
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1000792289606234", "MasterCard 1000 79** **** 6234"),
    ],
)
def test_mask_account_card_different_card_names(card_number: str, expected: str) -> None:
    assert mask_account_card(card_number) == expected


@pytest.mark.parametrize("card_number", [("Visa Platinum 73654108430135874305"), ("Счет 7000792289606361")])
def test_mask_account_card_with_wrong_number_type(card_number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card_number)


@pytest.mark.parametrize(
    "card_number, expected",
    [("Visa Platinum", "Некорректный ввод информации"), ("Счет", "Некорректный ввод информации")],
)
def test_mask_account_card_without_digits(card_number: str, expected: str) -> None:
    assert mask_account_card(card_number) == expected

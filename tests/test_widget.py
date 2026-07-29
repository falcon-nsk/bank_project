import pytest

from src.widget import get_date, mask_account_card


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


@pytest.mark.parametrize(
    "input_date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024")]
)
def test_get_date(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-3-1T02:26:18.671407", "1.3.2024"),
        ("2024-03-1T02:26:18.671407", "1.03.2024"),
        ("2024-3-01T02:26:18.671407", "01.3.2024"),
    ],
)
def test_get_date_unusual_format(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


@pytest.mark.parametrize("input_date", [("11.03.2024"), ("03/11/2024"), (""), ("  "), ("T02:26:18.671407")])
def test_get_date_with_invalid_format(input_date: str) -> None:
    with pytest.raises(ValueError):
        get_date(input_date)

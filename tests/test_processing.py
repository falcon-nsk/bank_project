import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def operations() -> list[dict]:
    return [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]

"""
print(filter_by_state(operations))  # фильтрует по статусу по умолчанию (EXECUTED)
print(filter_by_state(operations, "CANCELED"))  # фильтрует по переданному статусу (CANCELED)
print(sort_by_date(operations))  # сортирует по убыванию по умолчанию (reverse=True)
print(sort_by_date(operations, reverse=False))  # сортирует по возрастанию при reverse=False
"""

@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(operations: list[dict], state: str, expected: list[dict]) -> None:
    result = filter_by_state(operations, state)

    assert result == expected


def test_sort_by_date_descending(operations: list[dict]) -> None:
    result = sort_by_date(operations)
    expected = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert result == expected


def test_sort_by_date_ascending(operations: list[dict]) -> None:
    result = sort_by_date(operations, reverse=False)
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    assert result == expected


def test_sort_by_date_the_same_date() -> None:
    same_date_operations = [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = sort_by_date(same_date_operations)

    assert result == same_date_operations


def test_sort_by_date_without_date() -> None:
    same_date_operations = [
        {"id": 615064591, "state": "CANCELED"},
    ]
    with pytest.raises(KeyError):
        sort_by_date(same_date_operations)

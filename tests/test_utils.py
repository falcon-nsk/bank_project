from pathlib import Path
from unittest.mock import Mock, mock_open, patch

from src.utils import load_transactions

# load_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}, {"id": 2}]')
def test_load_transactions(mock_file: Mock) -> None:
    file_path = Path("transactions.json")
    transactions = [{"id": 1}, {"id": 2}]
    result = load_transactions(file_path)
    assert result == transactions
    mock_file.assert_called_once_with(file_path, "r", encoding="utf-8")


def test_load_transactions_file_not_found(tmp_path: Path) -> None:
    file_path = tmp_path / "missing.json"
    result = load_transactions(file_path)
    assert result == []


def test_load_transactions_invalid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("это не JSON", encoding="utf-8")
    result = load_transactions(file_path)
    assert result == []


def test_load_transactions_empty_json(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")
    result = load_transactions(file_path)
    assert result == []


def test_load_transactions_not_list(tmp_path: Path) -> None:
    file_path = tmp_path / "not_list.json"
    file_path.write_text('{"id": 1}', encoding="utf-8")
    result = load_transactions(file_path)
    assert result == []

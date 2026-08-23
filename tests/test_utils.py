import json
from pathlib import Path

from src.utils import load_transactions

# load_transactions


def test_load_transactions(tmp_path: Path) -> None:
    file_path = tmp_path / "transactions.json"
    transactions = [{"id": 1}, {"id": 2}]
    file_path.write_text(json.dumps(transactions), encoding="utf-8")
    result = load_transactions(file_path)
    assert result == transactions


def test_load_transactions_file_not_found(tmp_path: Path) -> None:
    file_path = tmp_path / "missing.json"
    result = load_transactions(file_path)
    assert result == []


def test_load_transactions_invalid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("это не JSON", encoding="utf-8")
    result = load_transactions(file_path)
    assert result == []

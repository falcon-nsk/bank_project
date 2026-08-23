from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_success(capsys: CaptureFixture[str]) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert captured.out == "my_function ok\n"


def test_log_error(capsys: CaptureFixture[str]) -> None:
    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    captured = capsys.readouterr()

    assert captured.out == ("my_function error: division by zero. Inputs: (1, 0), {}\n")


def test_log_success_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)

    assert result == 3
    assert log_file.read_text(encoding="utf-8") == "my_function ok\n"


def test_log_error_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    assert log_file.read_text(encoding="utf-8") == ("my_function error: division by zero. Inputs: (1, 0), {}\n")

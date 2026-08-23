from unittest.mock import Mock, patch

import src.external_api
from src.external_api import convert_amount, get_exchange_rate

# get_exchange_rate


def test_get_exchange_rate() -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 80.0}}

    with patch("src.external_api.requests.get", return_value=mock_response) as mock_get:
        result = get_exchange_rate("USD")
        assert result == 80.0
        mock_get.assert_called_once_with(
            src.external_api.API_URL,
            headers=src.external_api.HEADERS,
            params={"base": "USD", "symbols": "RUB"},
        )


# convert_amount


@patch("src.external_api.get_exchange_rate")
def test_convert_amount_rub(mock_get_rate: Mock) -> None:
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}
    result = convert_amount(transaction)
    assert result == 1000.00
    mock_get_rate.assert_not_called()


@patch("src.external_api.get_exchange_rate", return_value=80.0)
def test_convert_amount_usd(mock_get_rate: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = convert_amount(transaction)
    assert result == 8000.0
    mock_get_rate.assert_called_once_with("USD")


@patch("src.external_api.get_exchange_rate", return_value=90.0)
def test_convert_amount_eur(mock_get_rate: Mock) -> None:
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}
    result = convert_amount(transaction)
    assert result == 9000.0
    mock_get_rate.assert_called_once_with("EUR")

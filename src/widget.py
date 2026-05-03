from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """Принимает тип и номер карты или счета, возвращает замаскированный номер"""
    account_number = ""
    card_number = ""
    if info.startswith("Счет"):
        for number in info:
            if number.isdigit():
                account_number += number
        return get_mask_account(account_number)
    else:
        for number in info:
            if number.isdigit():
                card_number += number
        return get_mask_card_number(card_number)

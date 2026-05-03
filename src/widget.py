from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """Принимает тип и номер карты или счета, возвращает замаскированный номер"""
    account_number = ""
    card_number = ""
    card_name = ""
    if info.startswith("Счет"):
        for symbol in info:
            if symbol.isdigit():
                account_number += symbol
        return f"Счет {get_mask_account(account_number)}"
    else:
        for symbol in info:
            if symbol.isdigit():
                card_number += symbol
            else:
                card_name += symbol
        return f"{card_name.strip()} {get_mask_card_number(card_number)}"

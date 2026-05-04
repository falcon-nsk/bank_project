from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """Принимает тип и номер карты или счета, возвращает замаскированный номер"""
    if info.strip() == "":
        return "Вы ничего не ввели"
    has_digit = False

    for symbol in info:
        if symbol.isdigit():
            has_digit = True
            break

    if not has_digit:
        return "Некорректный ввод информации"
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


def get_date(info: str) -> str:
    """Принимает строку с информацией и возвращает строку с датой"""
    separated_line = info.split("T")
    date = separated_line[0]
    parts_of_date = date.split("-")
    return f"{parts_of_date[2]}.{parts_of_date[1]}.{parts_of_date[0]}"

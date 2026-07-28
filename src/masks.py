"""
Функция get_mask_card_number
принимает на вход номер карты и возвращает ее маску.
Номер карты замаскирован и отображается в формате
XXXX XX** **** XXXX, где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры,
остальные символы отображаются звездочками,
номер разбит по блокам по 4 цифры, разделенным пробелами.

Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
"""


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает ее маску"""
    card_number = card_number.replace(" ", "")

    if len(card_number) != 16:
        raise ValueError("Неверная длина номера карты")

    if not card_number.isdigit():
        raise ValueError("Неверный номер карты")

    first_part_of_number = card_number[:6]
    second_part_of_number = card_number[-4:]
    result = f"{first_part_of_number[:4]} {first_part_of_number[4:6]}** **** {second_part_of_number}"
    return result


"""
Функция get_mask_account принимает на вход номер счета
и возвращает его маску.
Номер счета замаскирован и отображается в формате
**XXXX, где X — это цифра номера.
То есть видны только последние 4 цифры номера, а перед ними — две звездочки.

Пример работы функции:
73654108430135874305 # входной аргумент
**4305 # выход функции
"""


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает его маску"""
    account_number = account_number.replace(" ", "")

    if len(account_number) != 20:
        raise ValueError("Неверная длина номера аккаунта")

    if not account_number.isdigit():
        raise ValueError("Неверный номер счета")

    return f"**{account_number[-4:]}"

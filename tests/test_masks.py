"""from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("7000792289606361")) #Проверка файла masks
print(get_mask_account("3654108430135874305"))
"""

from src.widget import get_date, mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))  # Проверка файла widget
print(get_date("2024-03-11T02:26:18.671407"))  # Получение даты

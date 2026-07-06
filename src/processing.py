"""
В модуле processing напишите функцию filter_by_state,
которая принимает список словарей
и опционально значение для ключа state
(по умолчанию 'EXECUTED').
Функция возвращает новый список словарей,
содержащий только те словари,
у которых ключ state соответствует указанному значению.
"""

def filter_by_state(
        list_of_dicts: list[dict],
        state="EXECUTED"
) -> list[dict]:
    """Фильтрует список словарей по значению ключа `state`.
    Args:
        list_of_dicts: Список словарей.
        state: Значение состояния для фильтрации. По умолчанию "EXECUTED".
    Returns:
        Новый список словарей, удовлетворяющих условию.
    """
    new_list_of_dicts = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list_of_dicts.append(item)
    return new_list_of_dicts


def sort_by_date(
        list_of_dicts: list[dict],
        reverse: bool = True
) -> list[dict]:
    """
    Сортирует список словарей по дате.
    Args:
        list_of_dicts: список словарей
        reverse: порядок сортировки. True - по убыванию, False - по возрастанию.
    Returns:
        Новый отсортированный список словарей
    """
    new_list_sorted_by_date = sorted(
        list_of_dicts,
        key=lambda item: item["date"],
    reverse=reverse
    )
    return new_list_sorted_by_date

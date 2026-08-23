import json

def load_transactions(file_path):
    """ Загружает финансовые транзакции из JSON-файла """
    try:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                if all(isinstance(item, dict) for item in data):
                    return data

            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: Path) -> list[dict]:
    """Загружает финансовые транзакции из JSON-файла"""
    try:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                if all(isinstance(item, dict) for item in data):
                    logger.debug("Транзакции успешно загружены")
                    return data

            logger.error("Некорректный формат данных")
            return []
    except FileNotFoundError:
        logger.error("Файл с транзакциями не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []

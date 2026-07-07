from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(operations))  # фильтрует по статусу по умолчанию (EXECUTED)
print(filter_by_state(operations, "CANCELED"))  # фильтрует по переданному статусу (CANCELED)
print(sort_by_date(operations))  # сортирует по убыванию по умолчанию (reverse=True)
print(sort_by_date(operations, reverse=False))  # сортирует по возрастанию при reverse=False

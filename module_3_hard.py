def calculate_structure_sum(data):
    total_sum = 0  

    # Проверяем тип данных: список, кортеж или множество
    if isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивно обрабатываем каждый элемент
    # Если это словарь, отдельно обрабатываем ключи и значения
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, str):
                total_sum += len(key)  # Если ключ строка, добавляем его длину
            total_sum += calculate_structure_sum(value)  # Рекурсивно обрабатываем значение
    # Если это число, добавляем его
    elif isinstance(data, int):
        total_sum += data
    # Если это строка, добавляем её длину
    elif isinstance(data, str):
        total_sum += len(data)

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаем результат 99
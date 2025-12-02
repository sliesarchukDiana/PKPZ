def sort_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda p: p["age"])

if __name__ == "__main__":
    data_1 = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Eve", "age": 35},
    ]

    print("Вхідні дані 1:", data_1)
    result_1 = sort_by_age(data_1)
    print("Результат 1:  ", result_1)

    print("-" * 30)

    data_2 = [
        {"name": "Zara", "age": 18},
        {"name": "Liam", "age": 22},
        {"name": "Noah", "age": 20}
    ]

    print("Вхідні дані 2:", data_2)
    result_2 = sort_by_age(data_2)
    print("Результат 2:  ", result_2)
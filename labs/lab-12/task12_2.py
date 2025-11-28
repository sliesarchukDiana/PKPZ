def filter_long_words(words: list[str]) -> list[str]:
    """
    Повертає список слів, довжина яких строго більша за 3 символи.
    Використовує вбудовану функцію filter().
    """
    # filter приймає функцію-предикат та ітерований об'єкт.
    # lambda w: len(w) > 3 повертає True, якщо довжина слова > 3.
    # list() перетворює ітератор, який повертає filter, назад у список.
    return list(filter(lambda w: len(w) > 3, words))

# --- Блок перевірки ---
if __name__ == "__main__":
    # Тест 1 (із завдання)
    test_1 = ["a", "the", "code", "Python", "is", "fun"]
    print(f"Вхід: {test_1}")
    print(f"Результат: {filter_long_words(test_1)}")  # Очікується: ['code', 'Python']
    print("-" * 20)

    # Тест 2
    test_2 = ["cat", "dog", "fish", "go", "egg"]
    print(f"Вхід: {test_2}")
    print(f"Результат: {filter_long_words(test_2)}")  # Очікується: ['fish'] ('cat' має 3 літери, тому не проходить)
    print("-" * 20)

    # Тест 3 (порожні рядки та слова різної довжини)
    test_3 = ["", "aa", "bbb", "cccc", "ddddd"]
    print(f"Вхід: {test_3}")
    print(f"Результат: {filter_long_words(test_3)}")  # Очікується: ['cccc', 'ddddd']
    print("-" * 20)

    # Тест 4 (порожній список)
    test_4 = []
    print(f"Вхід: {test_4}")
    print(f"Результат: {filter_long_words(test_4)}")  # Очікується: []
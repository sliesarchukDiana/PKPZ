from typing import Iterable


def capitalize_words(words: Iterable[str]) -> Iterable[str]:
    """
    Приймає ітерабельну послідовність рядків і повертає ітератор,
    де кожен рядок починається з великої літери, а решта — малі.

    Використовує map() та str.capitalize.
    Повертає об'єкт map (ітератор), не перетворюючи його на список.
    """
    # Ми передаємо метод str.capitalize як функцію.
    # map автоматично застосує цей метод до кожного елемента words.
    return map(str.capitalize, words)


# --- Блок перевірки ---
if __name__ == "__main__":
    # Тест 1: Список
    input_1 = ["python", "java", "c++"]
    # Оскільки функція повертає ітератор, для виводу перетворюємо його на list
    print(f"Вхід: {input_1}")
    print(f"Результат: {list(capitalize_words(input_1))}")
    print("-" * 20)

    # Тест 2: Кортеж (tuple)
    input_2 = ("hello", "WORLD")  # WORLD перетвориться на World
    print(f"Вхід: {input_2}")
    print(f"Результат: {tuple(capitalize_words(input_2))}")
    print("-" * 20)

    # Тест 3: Порожній рядок
    input_3 = [""]
    print(f"Вхід: {input_3}")
    print(f"Результат: {list(capitalize_words(input_3))}")
    print("-" * 20)

    # Тест 4: Порожній список
    input_4 = []
    print(f"Вхід: {input_4}")
    print(f"Результат: {list(capitalize_words(input_4))}")
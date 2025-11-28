from typing import Callable


# --- 1. Допоміжні функції (правила) ---

def has_uppercase(password: str) -> bool:
    """Перевіряє наявність хоча б однієї великої літери."""
    return any(char.isupper() for char in password)


def has_digit(password: str) -> bool:
    """Перевіряє наявність хоча б однієї цифри."""
    return any(char.isdigit() for char in password)


def is_long_enough(password: str) -> bool:
    """Перевіряє, чи довжина пароля не менше 8 символів."""
    return len(password) >= 8


def has_special_char(password: str) -> bool:
    """Перевіряє наявність спецсимволів із заданого набору."""
    special_chars = "!@#$%^&*()"
    return any(char in special_chars for char in password)


def no_spaces(password: str) -> bool:
    """Перевіряє відсутність пробілів."""
    return ' ' not in password


# --- 2. Основна функція ---

def validate_password(password: str) -> bool:
    """
    Перевіряє пароль за списком правил, використовуючи функцію all().
    Повертає True, якщо всі правила виконані, інакше False.
    """
    # Список функцій-правил
    rules: list[Callable[[str], bool]] = [
        has_uppercase,
        has_digit,
        is_long_enough,
        has_special_char,
        no_spaces
    ]

    # Перевіряємо, чи всі функції зі списку rules повертають True для даного пароля
    return all(rule(password) for rule in rules)


# --- 3. Запуск (Демонстрація) ---

if __name__ == "__main__":
    # Варіант А: Перевірка прикладів із завдання
    print("--- Перевірка прикладів ---")
    print(f"StrongPass1!:   {validate_password('StrongPass1!')}")  # Має бути True
    print(f"weakpass:       {validate_password('weakpass')}")  # Має бути False
    print(f"Short7!:        {validate_password('Short7!')}")  # Має бути False
    print(f"With Space1!:   {validate_password('With Space1!')}")  # Має бути False

    print("-" * 30)

    # Варіант Б: Введення користувачем (згідно загальних вимог)
    user_pass = input("Введіть ваш пароль для перевірки: ")
    is_valid = validate_password(user_pass)

    if is_valid:
        print("Результат: Пароль надійний (True)")
    else:
        print("Результат: Пароль ненадійний (False)")
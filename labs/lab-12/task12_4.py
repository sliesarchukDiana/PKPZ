from typing import Callable

def has_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)


def has_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def is_long_enough(password: str) -> bool:
    return len(password) >= 8


def has_special_char(password: str) -> bool:
    special_chars = "!@#$%^&*()"
    return any(char in special_chars for char in password)


def no_spaces(password: str) -> bool:
    return ' ' not in password

def validate_password(password: str) -> bool:
    rules: list[Callable[[str], bool]] = [
        has_uppercase,
        has_digit,
        is_long_enough,
        has_special_char,
        no_spaces
    ]

    return all(rule(password) for rule in rules)

if __name__ == "__main__":
    print("--- Перевірка прикладів ---")
    print(f"StrongPass1!:   {validate_password('StrongPass1!')}")
    print(f"weakpass:       {validate_password('weakpass')}")
    print(f"Short7!:        {validate_password('Short7!')}")
    print(f"With Space1!:   {validate_password('With Space1!')}")

    print("-" * 30)
    user_pass = input("Введіть ваш пароль для перевірки: ")
    is_valid = validate_password(user_pass)

    if is_valid:
        print("Результат: Пароль надійний (True)")
    else:
        print("Результат: Пароль ненадійний (False)")
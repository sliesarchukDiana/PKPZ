from typing import Iterable

def capitalize_words(words: Iterable[str]) -> Iterable[str]:
    return map(str.capitalize, words)

if __name__ == "__main__":
    input_1 = ["python", "java", "c++"]
    print(f"Вхід: {input_1}")
    print(f"Результат: {list(capitalize_words(input_1))}")
    print("-" * 20)
    input_2 = ("hello", "WORLD")
    print(f"Вхід: {input_2}")
    print(f"Результат: {tuple(capitalize_words(input_2))}")
    print("-" * 20)

    input_3 = [""]
    print(f"Вхід: {input_3}")
    print(f"Результат: {list(capitalize_words(input_3))}")
    print("-" * 20)

    input_4 = []
    print(f"Вхід: {input_4}")
    print(f"Результат: {list(capitalize_words(input_4))}")
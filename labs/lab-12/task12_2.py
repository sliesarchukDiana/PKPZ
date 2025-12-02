def filter_long_words(words: list[str]) -> list[str]:
    return list(filter(lambda w: len(w) > 3, words))

if __name__ == "__main__":
    test_1 = ["a", "the", "code", "Python", "is", "fun"]
    print(f"Вхід: {test_1}")
    print(f"Результат: {filter_long_words(test_1)}")
    print("-" * 20)

    test_2 = ["cat", "dog", "fish", "go", "egg"]
    print(f"Вхід: {test_2}")
    print(f"Результат: {filter_long_words(test_2)}")
    print("-" * 20)

    test_3 = ["", "aa", "bbb", "cccc", "ddddd"]
    print(f"Вхід: {test_3}")
    print(f"Результат: {filter_long_words(test_3)}")
    print("-" * 20)

    test_4 = []
    print(f"Вхід: {test_4}")
    print(f"Результат: {filter_long_words(test_4)}")
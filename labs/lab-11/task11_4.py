from typing import Iterator


def walk_tree(data: dict) -> Iterator[str]:
    for key, value in data.items():
        yield key
        if isinstance(value, dict):
            yield from walk_tree(value)


def main():
    print("\nТест 1:")
    tree_1 = {
        "a": {
            "b": {
                "c": 1
            }
        },
        "d": 2
    }
    print(f"Вхідні дані: {tree_1}")
    result_1 = list(walk_tree(tree_1))
    print(f"Результат: {result_1}")

    print("\nТест 2 (розгалужене дерево):")
    tree_2 = {
        "x": {"y": {"z": {}}},
        "m": {"n": 42}
    }
    print(f"Вхідні дані: {tree_2}")
    result_2 = list(walk_tree(tree_2))
    print(f"Результат: {result_2}")

    print("\nТест 3 (ігнорування не-словникових значень):")
    tree_3 = {
        "root": {
            "branch_1": "leaf string",
            "branch_2": {
                "sub_branch": 100
            }
        },
        "side_node": [1, 2, 3]
    }
    result_3 = list(walk_tree(tree_3))
    print(f"Результат: {result_3}")


if __name__ == "__main__":
    main()
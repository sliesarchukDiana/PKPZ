def input_array():
    n = int(input("Введіть кількість елементів масиву: "))
    arr = []
    for i in range(n):
        val = int(input(f"Елемент {i+1}: "))
        arr.append(val)
    return arr


def sum_between_min_max(arr):
    if not arr:
        return 0

    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    start = min(min_idx, max_idx)
    end = max(min_idx, max_idx)

    return sum(arr[start:end + 1])


def print_result(arr, result):
    print("\nМасив:", arr)
    print("Сума між мінімальним і максимальним (включно):", result)


def main():
    arr = input_array()
    result = sum_between_min_max(arr)
    print_result(arr, result)


if __name__ == "__main__":
    main()

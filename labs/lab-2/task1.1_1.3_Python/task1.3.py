import random

ROWS = 10     # вагони
SEATS = 20    # місць у вагоні


def generate_train():
    train = [[random.randint(0, 1) for _ in range(SEATS)] for _ in range(ROWS)]
    return train


def print_wagon(wagon):
    print("Місця у вагоні (1 – зайняте, 0 – вільне):")
    for i, seat in enumerate(wagon, start=1):
        print(f"{i:2d}:{seat}", end="  ")
        if i % 10 == 0:
            print()
    print()


def has_free_lower_seats(wagon):
    for i in range(0, SEATS, 2):
        if wagon[i] == 0:
            return True
    return False


def main():
    train = generate_train()
    wagon_num = int(input(f"Введіть номер вагону (1-{ROWS}): "))

    if not (1 <= wagon_num <= ROWS):
        print("Некоректний номер вагону.")
        return

    wagon = train[wagon_num - 1]
    print_wagon(wagon)

    if has_free_lower_seats(wagon):
        print("У цьому вагоні є вільні нижні місця.")
    else:
        print("У цьому вагоні всі нижні місця зайняті.")


if __name__ == "__main__":
    main()

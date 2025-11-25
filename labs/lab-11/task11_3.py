from typing import Iterator


def float_range(start: float, stop: float, step: float) -> Iterator[float]:
    if step == 0:
        raise ValueError("Step cannot be zero")

    precision = 10

    current = start

    if step > 0:
        while current < stop:
            yield round(current, precision)
            current += step
            current = round(current, precision)

    else:
        while current > stop:
            yield round(current, precision)
            current += step
            current = round(current, precision)


def main():
    while True:
        try:
            user_input = input("\nВведіть start, stop, step через пробіл (або 'q' для виходу): ")
            if user_input.lower() == 'q':
                break

            parts = [float(x) for x in user_input.split()]
            if len(parts) != 3:
                print("Потрібно ввести рівно 3 числа.")
                continue

            start, stop, step = parts

            gen = float_range(start, stop, step)
            print(f"Результат: {list(gen)}")

        except ValueError:
            print("Помилка: Введіть коректні числа.")
        except Exception as e:
            print(f"Помилка виконання: {e}")


if __name__ == "__main__":
    main()
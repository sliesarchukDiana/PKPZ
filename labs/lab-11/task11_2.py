class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        val = self.current
        self.current -= 1
        return val


def main():
    print("Введіть число, щоб запустити зворотний відлік до 0.")

    while True:
        user_input = input("\nВведіть ціле число 'start' (або 'q' для виходу): ")

        if user_input.lower() == 'q':
            break

        try:
            start_num = int(user_input)

            print(f"Запуск ітератора Countdown({start_num}):")
            counter = Countdown(start_num)

            print(f"Результат списком: {list(counter)}")

            print("Результат циклом: ", end="")
            for num in Countdown(start_num):
                print(num, end=" ")
            print()

        except ValueError:
            print("Помилка: Введіть коректне ціле число.")


if __name__ == "__main__":
    main()
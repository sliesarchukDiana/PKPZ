def filter_even_numbers_functional(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


def main():
    print("Ця програма відфільтровує парні числа зі введеного списку.")

    while True:
        try:
            user_input = input("\nВведіть цілі числа через пробіл (або 'q' для виходу): ")

            if user_input.lower() == 'q':
                break

            numbers = [int(x) for x in user_input.split()]

            even_numbers = filter_even_numbers_functional(numbers)

            print(f"Вхідний список: {numbers}")
            print(f"Результат (парні числа): {even_numbers}")

        except ValueError:
            print("Помилка: Будь ласка, вводьте коректні цілі числа, розділені пробілами.")


if __name__ == "__main__":
    main()
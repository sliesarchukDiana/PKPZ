def is_valid_coordinates(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


def is_attacking(figure_type, from_x, from_y, to_x, to_y):
    if from_x == to_x and from_y == to_y:
        return False

    if figure_type == "bishop":
        return abs(from_x - to_x) == abs(from_y - to_y)

    elif figure_type == "queen":
        return from_x == to_x or from_y == to_y or abs(from_x - to_x) == abs(from_y - to_y)

    elif figure_type == "rook":
        return from_x == to_x or from_y == to_y

    return False


def check_move(first_move_fig, coordinates):
    queen_x, queen_y = coordinates["white_queen"]
    rook_x, rook_y = coordinates["white_rook"]
    bishop_x, bishop_y = coordinates["black_bishop"]

    if first_move_fig == "white_queen":
        if is_attacking("queen", queen_x, queen_y, bishop_x, bishop_y):
            return "attack to bishop."
        elif is_attacking("bishop", bishop_x, bishop_y, rook_x, rook_y) and is_attacking("queen", queen_x, queen_y,
                                                                                         rook_x, rook_y):
            return "Defend from bishop."
        else:
            return "just move."

    elif first_move_fig == "white_rook":
        if is_attacking("rook", rook_x, rook_y, bishop_x, bishop_y):
            return "attack to bishop."
        elif is_attacking("bishop", bishop_x, bishop_y, queen_x, queen_y) and is_attacking("rook", rook_x, rook_y,
                                                                                           queen_x, queen_y):
            return "Defend from bishop."
        else:
            return "just move."

    elif first_move_fig == "black_bishop":
        if is_attacking("bishop", bishop_x, bishop_y, queen_x, queen_y):
            return "attack to queen."
        elif is_attacking("bishop", bishop_x, bishop_y, rook_x, rook_y):
            return "attack to rook."
        else:
            return "just move."

    return "Incorrect figure type."


def main():
    figure_coordinates = {}
    figures = ["white_queen", "white_rook", "black_bishop"]

    print("A program for determining the moves of a piece on a chessboard.")

    for figure in figures:
        while True:
            try:
                input_coordinates = input(f"Add coordinates {figure} (for example, 1,1): ")
                parts = input_coordinates.split(',')

                if len(parts) == 2:
                    x = int(parts[0].strip())
                    y = int(parts[1].strip())

                    if is_valid_coordinates(x, y):
                        figure_coordinates[figure] = (x, y)
                        break
                    else:
                        print("Error: Invalid coordinates. Try again")
                else:
                    print("Error: Use comma")
            except ValueError:
                print("Error: Please enter valid numbers")

    # Check for duplicate coordinates
    unique_coordinates = set()
    for coord in figure_coordinates.values():
        if coord in unique_coordinates:
            print("Error: Two figures on one cell. Program ending")
            return
        unique_coordinates.add(coord)

    print("\nChoose who makes the first move:")
    print("1. White Queen")
    print("2. White Rook")
    print("3. Black Bishop")
    choice = input("Your choice (1, 2 or 3): ")

    if choice == "1":
        result = check_move("white_queen", figure_coordinates)
        print(f"\nWhite Queen move: {result}")
    elif choice == "2":
        result = check_move("white_rook", figure_coordinates)
        print(f"\nWhite Rook move: {result}")
    elif choice == "3":
        result = check_move("black_bishop", figure_coordinates)
        print(f"\nBlack Bishop move: {result}")
    else:
        print("\nIncorrect choice. Program end.")


if __name__ == "__main__":
    main()
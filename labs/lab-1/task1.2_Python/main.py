import random

def check_point(x, y):
    parabola = -(x * x) + 2
    diagonal= x

    if x >= 0: #right side
        inside = parabola > y > 0
        on_border = y == diagonal or y == parabola
    else: #left side (x<= 0)
        inside = diagonal < y < parabola and y <= 0
        on_border = y == diagonal or y == parabola

    if inside:
        return "потрапив в мішень"
    elif on_border:
        return "на межі мішені"
    else:
        return "мішень не ушкоджена"

def generate_shots(n):
    shots = []
    for _ in range(n):
        x = round(random.uniform(-2, 2), 2)   # координати від -2 до 2
        y = round(random.uniform(-2, 2), 2)
        shots.append((x, y))
    return shots

def main():
    shots = generate_shots(10)
    print(f"{'№ пострілу':<10} {'Координати':<20} {'Результат'}")
    for i, (x, y) in enumerate(shots, start=1):
        result = check_point(x, y)
        print(f"{i:<10} ({x:>5}, {y:>5}){'':<5} {result}")

if __name__ == "__main__":
    main()

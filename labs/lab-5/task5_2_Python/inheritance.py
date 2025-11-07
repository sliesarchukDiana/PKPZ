class State:
    def __init__(self, name="Невідома", population=0, area=0):
        self.name = name
        self.population = population
        self.area = area

    def __del__(self):
        print("Лабораторна робота виконанна студенткою 2 курсу Слєсарчук Діаною Дмитрівною")

    def describe_system(self):
        return f"{self.name} — загальна форма державного устрою."

    def show(self):
        print(f"Назва: {self.name}")
        print(f"Населення: {self.population} млн")
        print(f"Площа: {self.area} км²")


class Republic(State):
    def __init__(self, name="Невідома республіка", population=0, area=0,
                 president="Невідомий", parliament="Однопалатний", term=5):
        super().__init__(name, population, area)
        self.president = president
        self.parliament = parliament
        self.term = term

    def describe_system(self):
        return f"{self.name} є республікою, де влада належить виборним органам."

    def show(self):
        super().show()
        print(f"Президент: {self.president}")
        print(f"Парламент: {self.parliament}")
        print(f"Термін повноважень: {self.term} років")
        print()


class Monarchy(State):
    def __init__(self, name="Невідома монархія", population=0, area=0,
                 monarch="Невідомий", dynasty="Невідома", hereditary=True):
        super().__init__(name, population, area)
        self.monarch = monarch
        self.dynasty = dynasty
        self.hereditary = hereditary

    def describe_system(self):
        return f"{self.name} є монархією, де влада належить монарху."

    def show(self):
        super().show()
        print(f"Монарх: {self.monarch}")
        print(f"Династія: {self.dynasty}")
        print(f"Спадкова влада: {'так' if self.hereditary else 'ні'}")
        print()


class Kingdom(Monarchy):
    def __init__(self, name="Невідоме королівство", population=0, area=0,
                 monarch="Невідомий", dynasty="Невідома", capital="Невідома столиця"):
        super().__init__(name, population, area, monarch, dynasty)
        self.capital = capital

    def describe_system(self):
        return f"{self.name} — королівство з монархом {self.monarch}."

    def show(self):
        super().show()
        print(f"Столиця: {self.capital}")
        print()

if __name__ == "__main__":
    s = State("Україна", 37.5, 603700)
    r = Republic("Франція", 68.4, 551695, "Емманюель Макрон", "Двопалатний", 5)
    m = Monarchy("Японія", 125.4, 377975, "Імператор Нарухіто", "Ямато", True)
    k = Kingdom("Іспанія", 47.6, 505990, "Король Філіп VI", "Бурбонів", "Мадрид")

    for obj in [s, r, m, k]:
        print("=" * 50)
        print(obj.describe_system())
        obj.show()

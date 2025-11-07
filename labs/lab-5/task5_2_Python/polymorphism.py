class Computer:
    def __init__(self, cpu_freq, cores, memory, disk):
        self.cpu_freq = cpu_freq        # МГц
        self.cores = cores              # кількість ядер
        self.memory = memory            # МБ
        self.disk = disk                # ГБ

    def cost(self):
        return (self.cpu_freq * self.cores) / 100 + (self.memory / 80) + (self.disk / 20)

    def is_suitable(self):
        return self.cpu_freq >= 2000 and self.cores >= 2 and self.memory >= 2048 and self.disk >= 320

    def info(self):
        return (
            f"Комп’ютер:\n"
            f"  Частота процесора: {self.cpu_freq} МГц\n"
            f"  Кількість ядер: {self.cores}\n"
            f"  Обсяг пам’яті: {self.memory} МБ\n"
            f"  Обсяг диска: {self.disk} ГБ\n"
            f"  Вартість: {self.cost():.2f} у.о.\n"
            f"  Придатний: {'Так' if self.is_suitable() else 'Ні'}\n"
        )


class Laptop(Computer):
    def __init__(self, cpu_freq, cores, memory, disk, battery_life):
        super().__init__(cpu_freq, cores, memory, disk)
        self.battery_life = battery_life  # хвилини

    def cost(self):
        base_cost = super().cost()
        return (base_cost + self.battery_life) / 10

    def is_suitable(self):
        # ноутбук придатний, якщо автономна робота ≥ 60 хв
        return self.battery_life >= 60

    def info(self):
        return (
            f"Ноутбук:\n"
            f"  Частота процесора: {self.cpu_freq} МГц\n"
            f"  Кількість ядер: {self.cores}\n"
            f"  Обсяг пам’яті: {self.memory} МБ\n"
            f"  Обсяг диска: {self.disk} ГБ\n"
            f"  Автономна робота: {self.battery_life} хв\n"
            f"  Вартість: {self.cost():.2f} у.о.\n"
            f"  Придатний: {'Так' if self.is_suitable() else 'Ні'}\n"
        )


class Tablet(Computer):
    def __init__(self, cpu_freq, cores, memory, disk, weight):
        super().__init__(cpu_freq, cores, memory, disk)
        self.weight = weight  # кг

    def cost(self):
        base_cost = super().cost()
        return base_cost / 10

    def info(self):
        return (
            f"Планшет:\n"
            f"  Частота процесора: {self.cpu_freq} МГц\n"
            f"  Кількість ядер: {self.cores}\n"
            f"  Обсяг пам’яті: {self.memory} МБ\n"
            f"  Обсяг диска: {self.disk} ГБ\n"
            f"  Вага: {self.weight} кг\n"
            f"  Вартість: {self.cost():.2f} у.о.\n"
            f"  Придатний: {'Так' if self.is_suitable() else 'Ні'}\n"
        )


# ====== ГОЛОВНА ЧАСТИНА ПРОГРАМИ ======

print("=== Введення даних для Комп’ютера ===")
cpu = float(input("Частота процесора (МГц): "))
cores = int(input("Кількість ядер: "))
memory = int(input("Пам’ять (МБ): "))
disk = int(input("Жорсткий диск (ГБ): "))

pc = Computer(cpu, cores, memory, disk)

print("\n=== Введення даних для Ноутбука ===")
cpu = float(input("Частота процесора (МГц): "))
cores = int(input("Кількість ядер: "))
memory = int(input("Пам’ять (МБ): "))
disk = int(input("Жорсткий диск (ГБ): "))
battery = int(input("Автономна робота (хв): "))

laptop = Laptop(cpu, cores, memory, disk, battery)

print("\n=== Введення даних для Планшета ===")
cpu = float(input("Частота процесора (МГц): "))
cores = int(input("Кількість ядер: "))
memory = int(input("Пам’ять (МБ): "))
disk = int(input("Жорсткий диск (ГБ): "))
weight = float(input("Вага (кг): "))

tablet = Tablet(cpu, cores, memory, disk, weight)

print("\n========== Інформація про створені об’єкти ==========")
print(pc.info())
print(laptop.info())
print(tablet.info())

# === Оновлення даних ===
print("=== Оновлення параметрів ===")
pc.memory += 1024
laptop.battery_life += 30
tablet.weight -= 0.1

print("\n========== Після оновлення ==========")
print(pc.info())
print(laptop.info())
print(tablet.info())

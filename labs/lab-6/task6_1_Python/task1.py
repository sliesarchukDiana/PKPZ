import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class Building(ABC):
    def __init__(self, address, street, area):
        self.address = address
        self.street = street
        self.area = area

    @abstractmethod
    def purpose(self):
        pass

    @abstractmethod
    def capacity(self):
        pass

    def show_info(self):
        return f"Адреса: {self.address}, Вулиця: {self.street}, Площа: {self.area} м²"

    def get_street(self):
        return self.street

class Barn(Building):
    def __init__(self, address, street, area, material, has_animals):
        super().__init__(address, street, area)
        self.material = material
        self.has_animals = has_animals

    def purpose(self):
        return "Призначення: зберігання тварин або інвентарю"

    def capacity(self):
        return f"Місткість: приблизно {int(self.area / 5)} тварин"

    def barn_info(self):
        return f"Матеріал: {self.material}, Є тварини: {'Так' if self.has_animals else 'Ні'}"

    def show_info(self):
        return f"[Сарай] {super().show_info()}, {self.barn_info()}, {self.purpose()}, {self.capacity()}"

class Storage(Building):
    def __init__(self, address, street, area, temperature, security):
        super().__init__(address, street, area)
        self.temperature = temperature
        self.security = security

    def purpose(self):
        return "Призначення: зберігання продуктів або матеріалів"

    def capacity(self):
        return f"Місткість: близько {int(self.area / 3)} одиниць товару"

    def storage_info(self):
        return f"Температура: {self.temperature}°C, Охорона: {'Так' if self.security else 'Ні'}"

    def show_info(self):
        return f"[Сховище] {super().show_info()}, {self.storage_info()}, {self.purpose()}, {self.capacity()}"

class BuildingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("База будівель")
        self.buildings = []

        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text="Тип будівлі:").grid(row=0, column=0, sticky="w")
        self.type_var = tk.StringVar(value="Barn")
        ttk.Combobox(frm, textvariable=self.type_var, values=["Barn", "Storage"], width=15).grid(row=0, column=1)

        ttk.Label(frm, text="Адреса:").grid(row=1, column=0, sticky="w")
        self.address_entry = ttk.Entry(frm, width=30)
        self.address_entry.grid(row=1, column=1)

        ttk.Label(frm, text="Вулиця:").grid(row=2, column=0, sticky="w")
        self.street_entry = ttk.Entry(frm, width=30)
        self.street_entry.grid(row=2, column=1)

        ttk.Label(frm, text="Площа (м²):").grid(row=3, column=0, sticky="w")
        self.area_entry = ttk.Entry(frm, width=30)
        self.area_entry.grid(row=3, column=1)

        ttk.Label(frm, text="Додаткові параметри:").grid(row=4, column=0, sticky="w")
        self.extra_entry = ttk.Entry(frm, width=30)
        self.extra_entry.grid(row=4, column=1)

        ttk.Label(frm, text="Додаткове поле 2 (True/False або число):").grid(row=5, column=0, sticky="w")
        self.extra2_entry = ttk.Entry(frm, width=30)
        self.extra2_entry.grid(row=5, column=1)

        ttk.Button(frm, text="Додати будівлю", command=self.add_building).grid(row=6, column=0, pady=10)
        ttk.Button(frm, text="Показати всі", command=self.show_all).grid(row=6, column=1, pady=10)

        ttk.Label(frm, text="Пошук по вулиці:").grid(row=7, column=0, sticky="w")
        self.search_entry = ttk.Entry(frm, width=30)
        self.search_entry.grid(row=7, column=1)

        ttk.Button(frm, text="Знайти", command=self.search_by_street).grid(row=8, column=0, pady=5)

        self.output = tk.Text(frm, width=80, height=15, wrap="word")
        self.output.grid(row=9, column=0, columnspan=2, pady=10)

    def add_building(self):
        try:
            address = self.address_entry.get()
            street = self.street_entry.get()
            area = float(self.area_entry.get())
            type_ = self.type_var.get()
            extra1 = self.extra_entry.get()
            extra2 = self.extra2_entry.get()

            if type_ == "Barn":
                has_animals = extra2.lower() in ["true", "1", "так", "yes"]
                obj = Barn(address, street, area, extra1, has_animals)
            else:
                security = extra2.lower() in ["true", "1", "так", "yes"]
                temperature = float(extra1)
                obj = Storage(address, street, area, temperature, security)

            self.buildings.append(obj)
            messagebox.showinfo("Успіх", "Будівлю додано!")
        except Exception as e:
            messagebox.showerror("Помилка", f"Невірні дані: {e}")

    def show_all(self):
        self.output.delete(1.0, tk.END)
        if not self.buildings:
            self.output.insert(tk.END, "База порожня.\n")
            return
        for b in self.buildings:
            self.output.insert(tk.END, b.show_info() + "\n\n")

    def search_by_street(self):
        street = self.search_entry.get().strip()
        self.output.delete(1.0, tk.END)
        found = [b for b in self.buildings if b.get_street().lower() == street.lower()]
        if not found:
            self.output.insert(tk.END, "Нічого не знайдено.\n")
        else:
            for b in found:
                self.output.insert(tk.END, b.show_info() + "\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BuildingApp(root)
    root.mainloop()

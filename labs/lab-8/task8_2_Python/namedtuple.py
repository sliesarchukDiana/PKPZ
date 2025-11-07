from tkinter import *
from collections import namedtuple
from tkinter import messagebox

Salary = namedtuple('Salary', ['m1', 'm2', 'm3', 'm4', 'm5', 'm6'])


def get_salary(employee, salary_monthly, bonus):
    mz = sum(salary_monthly) / len(salary_monthly)
    salary_vacation = 0.85 * mz + 0.95 * bonus
    return f"Співробітник {employee} – ваші відпускні нарахування за півроку становлять {salary_vacation:.2f}"


def calculate():
    try:
        employee = entry_name.get().strip()
        if not employee:
            messagebox.showerror("Помилка", "Введіть прізвище співробітника!")
            return

        # зчитуємо зарплати з полів
        salaries = [float(entries[i].get()) for i in range(6)]
        bonus = float(entry_bonus.get())

        salary_tuple = Salary(*salaries)
        result = get_salary(employee, salary_tuple, bonus)
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте, що всі введені дані є числами!")


# створюємо GUI
root = Tk()
root.title("Розрахунок відпускних")
root.geometry("450x400")
root.resizable(False, False)

Label(root, text="Прізвище співробітника:").pack(pady=5)
entry_name = Entry(root, width=30)
entry_name.pack()

frame_salaries = Frame(root)
frame_salaries.pack(pady=10)

entries = []
for i in range(6):
    Label(frame_salaries, text=f"Місяць {i + 1}:").grid(row=i, column=0, padx=5, pady=3, sticky="e")
    e = Entry(frame_salaries, width=10)
    e.grid(row=i, column=1, padx=5, pady=3)
    entries.append(e)

Label(root, text="Надбавка (грн):").pack(pady=5)
entry_bonus = Entry(root, width=15)
entry_bonus.pack()

Button(root, text="Розрахувати", command=calculate, bg="#4CAF50", fg="white").pack(pady=10)

label_result = Label(root, text="", wraplength=400, font=("Arial", 10, "bold"), justify="center")
label_result.pack(pady=10)

root.mainloop()

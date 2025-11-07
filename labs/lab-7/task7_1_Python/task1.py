import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_time():
    try:
        date_str = date_entry.get().strip()
        time_str = time_entry.get().strip()

        visit_datetime = datetime.strptime(f"{date_str} {time_str}", "%d%m%Y %H:%M:%S")
        now = datetime.now()

        if visit_datetime < now:
            messagebox.showwarning("Помилка", "Дата візиту вже минула.")
            return

        diff = visit_datetime - now
        hours_left = diff.total_seconds() / 3600

        if visit_datetime.hour < 12:
            part_of_day = "перша половина дня (до 12:00)"
        else:
            part_of_day = "друга половина дня (після 12:00)"

        result_label.config(
            text=f"До візиту залишилось {hours_left:.2f} годин.\n"
                 f"Візит буде у {part_of_day}."
        )

    except ValueError:
        messagebox.showerror("Помилка", "Перевірте формат введених даних!\n"
                                        "Дата: ДДММРРРР\nЧас: ГГ:ХХ:СС")

root = tk.Tk()
root.title("Візит до лікаря")
root.geometry("400x250")

tk.Label(root, text="Введіть дату візиту (ДДММРРРР):").pack(pady=5)
date_entry = tk.Entry(root, width=20)
date_entry.pack()

tk.Label(root, text="Введіть час візиту (ГГ:ХХ:СС):").pack(pady=5)
time_entry = tk.Entry(root, width=20)
time_entry.pack()

tk.Button(root, text="Обчислити", command=calculate_time).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 11), fg="black")
result_label.pack(pady=10)

root.mainloop()

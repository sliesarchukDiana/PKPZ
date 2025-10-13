import re
import tkinter as tk
from tkinter import messagebox

pattern = r"#[0-9A-Fa-f]{6}"

def find_colors():
    text = input_box.get("1.0", tk.END)
    matches = re.findall(pattern, text)
    result_box.delete("1.0", tk.END)
    if matches:
        for m in matches:
            result_box.insert(tk.END, m + "\n")
        count_label.config(text=f"Знайдено: {len(matches)} кольорів")
    else:
        count_label.config(text="Кольорів не знайдено")

def delete_color():
    color = color_entry.get().strip()
    text = input_box.get("1.0", tk.END)
    if color in text:
        new_text = text.replace(color, "")
        input_box.delete("1.0", tk.END)
        input_box.insert("1.0", new_text)
        find_colors()
    else:
        messagebox.showinfo("Інформація", "Вказаний колір не знайдено")

def replace_color():
    old = color_entry.get().strip()
    new = replace_entry.get().strip()
    text = input_box.get("1.0", tk.END)
    if old in text:
        new_text = text.replace(old, new)
        input_box.delete("1.0", tk.END)
        input_box.insert("1.0", new_text)
        find_colors()
    else:
        messagebox.showinfo("Інформація", "Вказаний колір не знайдено")

root = tk.Tk()
root.title("Hex Color Finder")
root.geometry("600x500")

tk.Label(root, text="Введіть текст:", font=("Arial", 12)).pack()
input_box = tk.Text(root, height=8)
input_box.pack(fill="x", padx=10)

tk.Button(root, text="Знайти кольори", command=find_colors).pack(pady=5)
count_label = tk.Label(root, text="Знайдено: 0 кольорів", font=("Arial", 10))
count_label.pack()

tk.Label(root, text="Результати:", font=("Arial", 12)).pack()
result_box = tk.Text(root, height=5)
result_box.pack(fill="x", padx=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Колір:").grid(row=0, column=0)
color_entry = tk.Entry(frame)
color_entry.grid(row=0, column=1)

tk.Label(frame, text="Замінити на:").grid(row=1, column=0)
replace_entry = tk.Entry(frame)
replace_entry.grid(row=1, column=1)

tk.Button(frame, text="Видалити", command=delete_color).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Замінити", command=replace_color).grid(row=1, column=2, padx=5)

root.mainloop()

import re
import tkinter as tk
from tkinter import messagebox


def is_lexicographic(word: str) -> bool:
    # перевіряє, чи букви в слові йдуть у порядку абетки
    return list(word) == sorted(word)


def find_and_remove():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("Помилка", "Введіть текст")
        return

    # знаходимо всі слова (латиниця або кирилиця)
    words = re.findall(r"[A-Za-zА-Яа-яЇїІіЄєҐґ]+", text)
    lex_words = [w for w in words if is_lexicographic(w.lower())]

    # показуємо знайдені слова
    result_box.delete("1.0", tk.END)
    if lex_words:
        for w in lex_words:
            result_box.insert(tk.END, w + "\n")
        count_label.config(text=f"Знайдено: {len(lex_words)} слів")
    else:
        result_box.insert(tk.END, "Немає таких слів\n")
        count_label.config(text="Знайдено: 0 слів")

    # видаляємо ці слова з тексту
    new_text = text
    for w in lex_words:
        new_text = re.sub(rf"\b{w}\b", "", new_text)
    new_text = re.sub(r"\s{2,}", " ", new_text).strip()

    output_box.delete("1.0", tk.END)
    output_box.insert("1.0", new_text)


# --- GUI ---
root = tk.Tk()
root.title("Видалення лексикографічних слів")
root.geometry("600x600")

tk.Label(root, text="Введіть текст:", font=("Arial", 12)).pack()
input_box = tk.Text(root, height=8, font=("Arial", 12))
input_box.pack(fill="x", padx=10)

tk.Button(root, text="Обробити", command=find_and_remove, font=("Arial", 12)).pack(pady=5)
count_label = tk.Label(root, text="Знайдено: 0 слів", font=("Arial", 10))
count_label.pack()

tk.Label(root, text="Слова з лексикографічним порядком:", font=("Arial", 12)).pack()
result_box = tk.Text(root, height=5, font=("Arial", 12))
result_box.pack(fill="x", padx=10)

tk.Label(root, text="Текст після видалення:", font=("Arial", 12)).pack(pady=(10, 0))
output_box = tk.Text(root, height=8, font=("Arial", 12))
output_box.pack(fill="x", padx=10)

root.mainloop()

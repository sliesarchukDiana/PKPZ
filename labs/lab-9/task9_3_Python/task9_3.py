import tkinter as tk
from tkinter import filedialog, messagebox


def load_expression():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            expr = f.read().strip()
        txt_expression.delete(0, tk.END)
        txt_expression.insert(0, expr)
    except:
        messagebox.showerror("Error", "Cannot read file.")


def check_parentheses():
    expr = txt_expression.get()
    result_list.delete(0, tk.END)

    stack = [0] * len(expr)
    top = -1

    pairs = []

    for i, ch in enumerate(expr):
        if ch == "(":
            top += 1
            stack[top] = i

        elif ch == ")":
            if top < 0:
                result_list.insert(tk.END, "Дужки НЕ збалансовані: зайва ')'")
                return
            pos_open = stack[top]
            top -= 1
            pairs.append((pos_open, i))

    if top != -1:
        result_list.insert(tk.END, "Дужки НЕ збалансовані: є незакриті '('")
        return

    pairs.sort(key=lambda x: x[1])

    result_list.insert(tk.END, "Дужки збалансовані.")
    result_list.insert(tk.END, "Пари (відкривна, закривна):")

    for op, cl in pairs:
        result_list.insert(tk.END, f"({op}, {cl})")

    global last_result
    last_result = result_list.get(0, tk.END)


def save_result():
    if not last_result:
        messagebox.showerror("Error", "No results to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as f:
        for line in last_result:
            f.write(line + "\n")

    messagebox.showinfo("Saved", "Результат збережено.")


root = tk.Tk()
root.title("Перевірка дужок у виразі")

frm = tk.Frame(root)
frm.pack(padx=10, pady=10)

tk.Label(frm, text="Математичний вираз:").grid(row=0, column=0)
txt_expression = tk.Entry(frm, width=80)
txt_expression.grid(row=1, column=0, padx=5, pady=5)

btn_load = tk.Button(frm, text="Завантажити файл", command=load_expression)
btn_load.grid(row=2, column=0, pady=5)

btn_check = tk.Button(frm, text="Перевірити", command=check_parentheses)
btn_check.grid(row=3, column=0, pady=5)

tk.Label(frm, text="Результат:").grid(row=4, column=0)
result_list = tk.Listbox(frm, width=80, height=12)
result_list.grid(row=5, column=0, pady=5)

btn_save = tk.Button(frm, text="Зберегти результат", command=save_result)
btn_save.grid(row=6, column=0, pady=10)

last_result = []

root.mainloop()

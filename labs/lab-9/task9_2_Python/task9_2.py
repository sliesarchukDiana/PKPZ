import tkinter as tk
from tkinter import filedialog, messagebox
import random

def load_list(target_box):
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = [line.strip() for line in f.readlines() if line.strip()]
        target_box.delete(0, tk.END)
        for item in data:
            target_box.insert(tk.END, item)
    except:
        messagebox.showerror("Error", "Cannot read file.")

def save_result(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return
    with open(file_path, "w", encoding="utf-8") as f:
        for row in data:
            f.write(f"{row[0]}  -  {row[1]}\n")
    messagebox.showinfo("Saved", "Result saved.")

def draw_pairs():
    team1 = list(box_team1.get(0, tk.END))
    team2 = list(box_team2.get(0, tk.END))

    if len(team1) != 10 or len(team2) != 10:
        messagebox.showerror("Error", "Each team must have exactly 10 athletes.")
        return

    n = random.randint(1, 10)
    m = random.randint(1, 10)

    lbl_params.config(text=f"n = {n}, m = {m}")

    used1 = set()
    used2 = set()
    pairs = []

    i = 0
    j = 0

    while len(pairs) < 10:
        count = 0
        while True:
            if i not in used1:
                count += 1
                if count == n:
                    used1.add(i)
                    p1 = team1[i]
                    break
            i = (i + 1) % len(team1)

        count = 0
        while True:
            if j not in used2:
                count += 1
                if count == m:
                    used2.add(j)
                    p2 = team2[j]
                    break
            j = (j + 1) % len(team2)

        pairs.append((p1, p2))

    list_result.delete(0, tk.END)
    for p in pairs:
        list_result.insert(tk.END, f"{p[0]}  -  {p[1]}")

    global last_result
    last_result = pairs

def save_last():
    if not last_result:
        messagebox.showerror("Error", "No results to save.")
        return
    save_result(last_result)


root = tk.Tk()
root.title("Tournament Draw")

frm = tk.Frame(root)
frm.pack(padx=10, pady=10)

tk.Label(frm, text="Team 1 (10 athletes)").grid(row=0, column=0)
box_team1 = tk.Listbox(frm, width=30, height=10)
box_team1.grid(row=1, column=0)
tk.Button(frm, text="Load Team 1", command=lambda: load_list(box_team1)).grid(row=2, column=0)

tk.Label(frm, text="Team 2 (10 athletes)").grid(row=0, column=1)
box_team2 = tk.Listbox(frm, width=30, height=10)
box_team2.grid(row=1, column=1)
tk.Button(frm, text="Load Team 2", command=lambda: load_list(box_team2)).grid(row=2, column=1)

lbl_params = tk.Label(frm, text="n = ?, m = ?")
lbl_params.grid(row=3, column=0, columnspan=2, pady=5)

tk.Button(frm, text="Draw Pairs", command=draw_pairs).grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(frm, text="Result:").grid(row=5, column=0, columnspan=2)
list_result = tk.Listbox(frm, width=60, height=10)
list_result.grid(row=6, column=0, columnspan=2)

tk.Button(frm, text="Save Result", command=save_last).grid(row=7, column=0, columnspan=2, pady=10)

last_result = []

root.mainloop()

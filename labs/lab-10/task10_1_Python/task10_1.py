import tkinter as tk
from tkinter import messagebox
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class QueueBasedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.left is None:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if node.right is None:
                node.right = new_node
                return
            else:
                q.append(node.right)

    def search(self, value):
        if not self.root:
            return False

        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.value == value:
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

    def delete(self, value):
        if not self.root:
            return False

        if self.root.value == value and not self.root.left and not self.root.right:
            self.root = None
            return True

        q = deque([self.root])
        node_to_delete = None
        last = None
        parent_of_last = None

        while q:
            node = q.popleft()
            if node.value == value:
                node_to_delete = node
            if node.left:
                parent_of_last = node
                last = node.left
                q.append(node.left)
            if node.right:
                parent_of_last = node
                last = node.right
                q.append(node.right)

        if node_to_delete:
            node_to_delete.value = last.value
            if parent_of_last.right == last:
                parent_of_last.right = None
            else:
                parent_of_last.left = None
            return True

        return False

    def inorder(self, node, res):
        if node:
            self.inorder(node.left, res)
            res.append(node.value)
            self.inorder(node.right, res)

    def preorder(self, node, res):
        if node:
            res.append(node.value)
            self.preorder(node.left, res)
            self.preorder(node.right, res)

    def postorder(self, node, res):
        if node:
            self.postorder(node.left, res)
            self.postorder(node.right, res)
            res.append(node.value)


class GUI:
    def __init__(self, root):
        self.tree = QueueBasedBinaryTree()

        self.root = root
        root.title("Бінарне дерево – Залізничні маршрути")

        tk.Label(root, text="Маршрут:").grid(row=0, column=0)
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=1, columnspan=2)

        tk.Button(root, text="Вставити", command=self.insert_item).grid(row=1, column=0)
        tk.Button(root, text="Видалити", command=self.delete_item).grid(row=1, column=1)
        tk.Button(root, text="Пошук", command=self.search_item).grid(row=1, column=2)

        tk.Button(root, text="Обхід (In-order)", command=lambda: self.traverse("in")).grid(row=2, column=0)
        tk.Button(root, text="Обхід (Pre-order)", command=lambda: self.traverse("pre")).grid(row=2, column=1)
        tk.Button(root, text="Обхід (Post-order)", command=lambda: self.traverse("post")).grid(row=2, column=2)

        tk.Label(root, text="Результат:").grid(row=3, column=0)
        self.output = tk.Text(root, height=10, width=55)
        self.output.grid(row=4, column=0, columnspan=3)

    def insert_item(self):
        val = self.entry.get().strip()
        if not val:
            messagebox.showerror("Помилка", "Введіть маршрут.")
            return
        self.tree.insert(val)
        self.output.insert(tk.END, f"Додано: {val}\n")

    def delete_item(self):
        val = self.entry.get().strip()
        if self.tree.delete(val):
            self.output.insert(tk.END, f"Видалено: {val}\n")
        else:
            self.output.insert(tk.END, f"Не знайдено: {val}\n")

    def search_item(self):
        val = self.entry.get().strip()
        found = self.tree.search(val)
        text = "Знайдено" if found else "Не знайдено"
        self.output.insert(tk.END, f"{text}: {val}\n")

    def traverse(self, t):
        res = []
        if t == "in":
            self.tree.inorder(self.tree.root, res)
        elif t == "pre":
            self.tree.preorder(self.tree.root, res)
        elif t == "post":
            self.tree.postorder(self.tree.root, res)

        self.output.insert(tk.END, " -> ".join(res) + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    GUI(root)
    root.mainloop()

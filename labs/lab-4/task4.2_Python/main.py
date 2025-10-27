def create_tf1():
    lines = [
        "HelloWorld",
        "ThisIsALine",
        "39jgiogjier5",
        "ABC987xyz",
        "42isAnswer"
    ]
    with open("TF_1.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def process_files():
    with open("TF_1.txt", "r", encoding="utf-8") as f1:
        content = f1.read()
    digits = "".join(ch for ch in content if ch.isdigit())
    others = "".join(ch for ch in content if not ch.isdigit() and ch != "\n")

    with open("TF_3.txt", "w", encoding="utf-8") as f3:
        f3.write(digits + others)

    with open("TF_3.txt", "r", encoding="utf-8") as f3:
        data = f3.read()

    with open("TF_2.txt", "w", encoding="utf-8") as f2:
        for i in range(0, len(data), 10):
            f2.write(data[i:i + 10] + "\n")

def print_tf2():
    with open("TF_2.txt", "r", encoding="utf-8") as f2:
        for line in f2:
            print(line.rstrip())

if __name__ == "__main__":
    create_tf1()
    process_files()
    print_tf2()

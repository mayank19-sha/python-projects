
import json
import os

File = "tasks.json"


def load_tasks():
    if not os.path.exists(File):
        return []

    with open(File, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(File, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("nothing yet")
        return

    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[]"
        print(f"{i}. {mark} {t['task']}")


def add_task(tasks, name):
    tasks.append({"task": name, "done": False})


def mark_done(tasks, num):
    tasks[num - 1]["done"] = True


def remove_task(tasks, num):
    tasks.pop(num - 1)


def main():
    tasks = load_tasks()

    while True:
        print("\n1 show | 2 add | 3 done | 4 remove | 5 exit")
        choice = input("> ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks, input("task: "))

        elif choice == "3":
            show_tasks(tasks)
            mark_done(tasks, int(input("which number: ")))

        elif choice == "4":
            show_tasks(tasks)
            remove_task(tasks, int(input("which number: ")))

        elif choice == "5":
            save_tasks(tasks)
            print("saved. bye")
            break


main()



import json
import os
from datetime import date

File = "tasks.json"


def load_data():
    if not os.path.exists(File):
        return []

    with open(File, "r") as f:
        return json.load(f)


def save_data(entries):
    with open(File, "w") as f:
        json.dump(entries, f, indent=2)


# ---- actions ----

def add_entry(entries):
    desc = input("Description: ")
    amount = float(input("Amount: "))
    category = input("Category (food/transport/other): ")
    typ = input("Type (income/expense): ").lower()

    entries.append({
        "description": desc,
        "amount": amount,
        "category": category,
        "type": typ,
        "date": str(date.today())
    })

    save_data(entries)
    print("Saved!")


def list_entries(entries):
    if not entries:
        print("No entries yet.")
        return

    for i, e in enumerate(entries, 1):
        sign = "+" if e["type"] == "income" else "-"

        print(
            f"{i}. {e['date']} {e['description']} "
            f"{sign}{e['amount']} ({e['category']})"
        )


def show_summary(entries):
    income = 0
    expense = 0
    cats = {}

    for e in entries:

        if e["type"] == "income":
            income += e["amount"]

        elif e["type"] == "expense":
            expense += e["amount"]

            category = e["category"]

            if category not in cats:
                cats[category] = 0

            cats[category] += e["amount"]

    balance = income - expense

    print(f"Income: {income}")
    print(f"Expense: {expense}")
    print(f"Balance: {balance}")

    print("\nExpenses by category:")

    for category in cats:
        print(f"{category}: {cats[category]}")


# ---- main loop ----

def main():
    entries = load_data()

    while True:
        print("\n1. Add")
        print("2. List")
        print("3. Summary")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            add_entry(entries)

        elif choice == "2":
            list_entries(entries)

        elif choice == "3":
            show_summary(entries)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()


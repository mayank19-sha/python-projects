
import random
import string
import json
import os

File = "tasks.json"


def load_data():
    if not os.path.exists(File):
        return []

    with open(File, "r") as f:
        return json.load(f)


def save_data(entries):
    with open(File, "w") as f:
        json.dump(entries, f, indent=2)


def add_password(entries):
    site = input("Site: ")
    username = input("Username: ")

    password = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=12
        )
    )

    print("Generated password:", password)

    entries.append({
        "site": site,
        "username": username,
        "password": password
    })

    save_data(entries)
    print("Password saved.")


def list_passwords(entries):
    if not entries:
        print("No passwords saved.")
        return

    for i, entry in enumerate(entries, start=1):
        print(f"\n{i}. Site: {entry['site']}")
        print(f"   Username: {entry['username']}")
        print(f"   Password: {entry['password']}")


def search_site(entries):
    site = input("Enter site to search: ").lower()

    found = False

    for entry in entries:
        if site in entry["site"].lower():
            print("\nSite:", entry["site"])
            print("Username:", entry["username"])
            print("Password:", entry["password"])
            found = True

    if not found:
        print("Site not found.")


def main():
    entries = load_data()

    while True:
        print("\n1. Add")
        print("2. List")
        print("3. Search by site")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            add_password(entries)

        elif choice == "2":
            list_passwords(entries)

        elif choice == "3":
            search_site(entries)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()


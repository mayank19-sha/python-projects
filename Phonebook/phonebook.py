phonebook = {}

def add_contact():
    name = input("Enter name: ")

    if name.strip() == "":
        print("Name can't be empty.")
        return

    number = input("Enter number: ")

    if len(number) != 10 or not number.isdigit():
        print("Enter exactly 10 digits.")
        return

    phonebook[name] = number
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ")

    if name in phonebook:
        print("Number is:", phonebook[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")

    if name not in phonebook:
        print("Contact not found.")
        return

    number = input("Enter new number: ")

    if len(number) != 10 or not number.isdigit():
        print("Enter exactly 10 digits.")
        return

    phonebook[name] = number
    print("Contact updated.")

def delete_contact():
    name = input("Enter name to delete: ")

    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def show_contacts():
    if phonebook:
        print("\nContacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

while True:
    print("\n===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show Contacts")
    print("6. Exit")

    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    if option == 1:
        add_contact()

    elif option == 2:
        search_contact()

    elif option == 3:
        update_contact()

    elif option == 4:
        delete_contact()

    elif option == 5:
        show_contacts()

    elif option == 6:
        print("Exiting...")
        break

    else:
        print("Invalid option! Please choose between 1 and 6.")
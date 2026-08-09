# 📱 Python Phonebook

A simple **command-line Phonebook application** built using Python. It allows users to add, search, update, delete, and display contacts.

The project uses a Python **dictionary** to store contact names and phone numbers.

## 📌 Features

* ➕ Add a new contact
* 🔍 Search for a contact
* ✏️ Update an existing contact
* 🗑️ Delete a contact
* 📋 Display all saved contacts
* 📞 Validates phone numbers to exactly 10 digits
* 🚫 Prevents empty names
* ⚠️ Handles invalid menu input
* 🔄 Runs continuously until the user chooses Exit

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionary
* Functions
* Loops
* Conditional statements
* Exception handling

No external libraries are required.

## 📂 Project Structure

```text
Python-Phonebook/
│
├── phonebook.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Python-Phonebook
```

### 3. Run the program

```bash
python phonebook.py
```

## 💻 Example Output

```text
===== PHONE BOOK =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show Contacts
6. Exit

Enter your option: 1
Enter name: Mayank
Enter number: 9876543210
Contact added.
```

### Show Contacts

```text
===== PHONE BOOK =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show Contacts
6. Exit

Enter your option: 5

Contacts:
Mayank: 9876543210
Rahul: 9876543211
```

### Search Contact

```text
Enter your option: 2
Enter name to search: Mayank
Number is: 9876543210
```

### Update Contact

```text
Enter your option: 3
Enter name to update: Mayank
Enter new number: 9123456789
Contact updated.
```

### Delete Contact

```text
Enter your option: 4
Enter name to delete: Mayank
Contact deleted.
```

## 🧠 How It Works

The phonebook is stored in a dictionary:

```python
phonebook = {}
```

The **name** is used as the dictionary key, while the **phone number** is stored as its value.

For example:

```python
phonebook = {
    "Mayank": "9876543210",
    "Rahul": "9876543211"
}
```

### Add Contact

The `add_contact()` function:

1. Takes the user's name.
2. Checks that the name isn't empty.
3. Takes the phone number.
4. Checks that it contains exactly 10 digits.
5. Stores the contact in the dictionary.

```python
phonebook[name] = number
```

### Search Contact

The `search_contact()` function checks whether the name exists in the dictionary:

```python
if name in phonebook:
    print("Number is:", phonebook[name])
```

### Update Contact

The `update_contact()` function first checks whether the contact exists. If it does, the stored number is replaced with the new number.

### Delete Contact

The `delete_contact()` function removes the contact using:

```python
del phonebook[name]
```

### Show Contacts

The `show_contacts()` function loops through the dictionary and displays every saved contact:

```python
for name, number in phonebook.items():
    print(f"{name}: {number}")
```

### Input Validation

The program validates phone numbers using:

```python
if len(number) != 10 or not number.isdigit():
    print("Enter exactly 10 digits.")
```

It also uses `try-except` to prevent the program from crashing when the user enters something other than a number in the menu.

## 📚 What I Learned

This project helped me practice:

* Python dictionaries
* Functions
* Function calls
* User input
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `return`
* `break` and `continue`
* Dictionary methods
* `in` operator
* `del`
* `.items()`
* `.strip()`
* `.isdigit()`
* `try-except`
* `ValueError` handling
* Input validation

## 🚀 Future Improvements

Possible improvements:

* 💾 Save contacts permanently using a file
* 🔐 Add password protection
* 📂 Use JSON or SQLite for storage
* 🔎 Search contacts by partial name
* 📱 Support multiple phone numbers per person
* 🔤 Sort contacts alphabetically
* 📊 Display the total number of contacts
* 🖥️ Create a GUI version using Tkinter or PySide6

## 👨‍💻 Author

**Mayank Sharma**

---

⭐ If you found this project useful, consider giving the repository a star!

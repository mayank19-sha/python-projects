# Password Manager

A simple Python-based password manager that generates, saves, lists, and searches passwords.

## Features

* Generate a random 12-character password
* Save passwords to a JSON file
* Store website, username, and password
* List all saved passwords
* Search passwords by website
* Persistent data storage using `tasks.json`
* Simple command-line interface

## Requirements

* Python 3.x
* No external libraries are required

The project uses Python's built-in modules:

* `random`
* `string`
* `json`
* `os`

## How to Run

1. Make sure Python is installed.

2. Open the project folder in a terminal.

3. Run:

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file.

## Menu

When the program starts, you will see:

```text
1. Add
2. List
3. Search by site
4. Exit
```

### 1. Add

Enter a website and username.

The program automatically generates a random 12-character password and saves it.

Example:

```text
Site: GitHub
Username: mayank19-sha
Generated password: A7kLm2Pq9Xz1
Password saved.
```

### 2. List

Displays all saved passwords.

```text
1. Site: GitHub
   Username: mayank19-sha
   Password: A7kLm2Pq9Xz1
```

### 3. Search by Site

Enter a website name to find matching saved accounts.

```text
Enter site to search: github

Site: GitHub
Username: mayank19-sha
Password: A7kLm2Pq9Xz1
```

### 4. Exit

Closes the program.

## Data Storage

The program stores the password information in:

```text
tasks.json
```

The file is automatically created when the first password is saved.

Example:

```json
[
  {
    "site": "GitHub",
    "username": "mayank19-sha",
    "password": "A7kLm2Pq9Xz1"
  }
]
```

## Project Structure

```text
Password-Manager/
│
├── main.py
├── tasks.json
└── README.md
```

`tasks.json` is created automatically by the program.

## How It Works

The program follows this basic flow:

```text
Start
  ↓
Load saved data
  ↓
Display menu
  ↓
User selects an option
  ↓
Add / List / Search
  ↓
Save changes to JSON
  ↓
Return to menu
  ↓
Exit
```

## Important Note

This is a **learning project**, not a secure production password manager.

Passwords are stored as plain text inside `tasks.json`. Anyone who can access this file can read the saved passwords.

For a real password manager, passwords should be encrypted and protected with proper authentication.

## Author

**Mayank Sharma**

## License

This project is created for educational and learning purposes.

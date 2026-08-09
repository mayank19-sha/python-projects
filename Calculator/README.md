# 🧮 Python Calculator

A simple command-line calculator built using **Python**.
This project performs basic arithmetic operations using separate functions and provides a menu-driven interface.

## 📌 Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🚫 Division-by-zero protection
* 🔄 Menu runs repeatedly until the user chooses Exit
* ❌ Invalid option handling
* 🧩 Uses separate functions for each operation

## 🛠️ Technologies Used

* **Python 3**
* No external libraries required

## 📂 Project Structure

```text
Python-Calculator/
│
├── calculator.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Python-Calculator
```

### 3. Run the program

```bash
python calculator.py
```

## 💻 Example

```text
Choose between 1, 2, 3, 4, 5

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your option: 1
Enter first number: 10
Enter second number: 5

10 + 5 = 15
```

Another example:

```text
Enter your option: 4
Enter first number: 10
Enter second number: 2

10 / 2 = 5.0
```

If the user tries to divide by zero:

```text
Enter your option: 4
Enter first number: 10
Enter second number: 0

Cannot divide by zero!
```

## 🧠 How It Works

The calculator uses four functions:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
```

The user selects an operation from the menu and enters two numbers. The selected function performs the calculation and displays the result.

The program continues running inside a `for` loop until the user selects **5. Exit**.

## 📚 What I Learned

Through this project, I practiced:

* Python functions
* Function parameters and return values
* `if`, `elif`, and `else`
* `for` loops
* `break`
* User input with `input()`
* Lists
* Basic error handling
* Arithmetic operators
* Menu-driven programs

## 🚀 Future Improvements

Possible improvements for this project:

* Add decimal number support using `float()`
* Add power and square-root operations
* Add a calculation history
* Add better input validation
* Convert the program into a GUI calculator
* Handle non-numeric input using `try-except`

## 👨‍💻 Author

**Mayank Sharma**

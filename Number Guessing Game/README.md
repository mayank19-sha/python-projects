# 🎯 Number Guessing Game

A simple command-line **Number Guessing Game** built using Python. The computer randomly selects a number between **1 and 100**, and the player has to guess it.

## 📌 Features

* 🎲 Generates a random number between 1 and 100
* ⌨️ Takes guesses from the user
* 📈 Tells the player if the guess is too high or too low
* 🔢 Counts the number of attempts
* 🏆 Displays the number of attempts when the correct answer is guessed
* 🔄 Continues until the player guesses correctly

## 🛠️ Technologies Used

* **Python 3**
* `random` module

No external libraries are required.

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── guessing_game.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Number-Guessing-Game
```

### 3. Run the program

```bash
python guessing_game.py
```

## 💻 Example Output

```text
Guess the number (1-100)
Your guess: 50
Too high!

Your guess: 25
Too low!

Your guess: 37
Too high!

Your guess: 32
Too low!

Your guess: 35
Correct! You got it in 5 attempts.
```

## 🧠 How It Works

First, the program generates a random number:

```python
number = random.randint(1, 100)
```

The `random.randint()` function generates a random integer between **1 and 100**.

An attempt counter is initialized:

```python
attempts = 0
```

The program then repeatedly asks the user for a guess using a `while True` loop:

```python
while True:
    guess = int(input("Your guess: "))
    attempts += 1
```

The guess is compared with the randomly generated number:

```python
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print(f"Correct! You got it in {attempts} attempts.")
    break
```

If the guess is correct, `break` stops the loop and the game ends.

## 📚 What I Learned

This project helped me practice:

* Python `while` loops
* `if`, `elif`, and `else`
* `break`
* User input using `input()`
* Type conversion using `int()`
* Variables and counters
* F-strings
* The `random` module
* Comparison operators

## 🚀 Future Improvements

Possible improvements:

* Add a maximum number of attempts
* Add difficulty levels
* Add a replay option
* Handle invalid/non-numeric input with `try-except`
* Give hints based on how close the guess is
* Keep track of the best score

## 👨‍💻 Author

**Mayank Sharma**

---

⭐ If you enjoyed this project, consider giving the repository a star!

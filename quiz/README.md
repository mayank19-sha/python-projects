# Python Quiz Game

A simple command-line quiz game written in Python.

The program asks multiple-choice questions, keeps track of the player's score, and saves the highest score in a JSON file.

## Features

* Multiple-choice questions
* Randomized question order
* Score tracking
* High-score system
* Saves high score using JSON
* Handles invalid input
* Handles empty or corrupted high-score files
* Simple command-line interface

## Requirements

* Python 3.x
* No external libraries are required

The project uses Python's built-in modules:

* `json`
* `random`

## How to Run

1. Clone or download the project.

2. Open the project folder in a terminal.

3. Run:

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file.

## How to Play

The program displays a question with three options.

Example:

```text
1. What is 2+2?
  1. 3
  2. 4
  3. 5

Your answer:
```

Enter the number corresponding to your answer.

### Correct Answer

```text
Your answer: 2
Correct!
```

### Wrong Answer

```text
Your answer: 1
Wrong! Answer was 4
```

At the end, your score is displayed:

```text
Final score: 2/3
```

## High Score

The program saves the highest score in:

```text
high_score.json
```

Example:

```json
{
  "high_score": 3
}
```

If you achieve a higher score than the previous high score:

```text
New high score!
```

Otherwise:

```text
High score remains: 2
```

## Input Validation

The program prevents invalid answers from crashing the program.

For example:

```text
Your answer: abc
Please enter a number.
```

And:

```text
Your answer: 5
Please enter a valid option.
```

## Project Structure

```text
Python-Quiz/
│
├── main.py
├── high_score.json
└── README.md
```

`high_score.json` is created automatically when a new high score is saved.

## How It Works

```text
Start
  ↓
Load high score
  ↓
Shuffle questions
  ↓
Display question
  ↓
Get user's answer
  ↓
Validate input
  ↓
Check answer
  ↓
Update score
  ↓
Repeat until all questions are completed
  ↓
Display final score
  ↓
Save new high score if achieved
  ↓
Exit
```

## Learning Concepts

This project demonstrates several basic Python concepts:

* Lists
* Dictionaries
* Functions
* Loops
* `if/else` conditions
* `try/except`
* File handling
* JSON
* Randomization
* User input
* Basic data validation

## Author

**Mayank Sharma**

## License

This project is created for educational and learning purposes.

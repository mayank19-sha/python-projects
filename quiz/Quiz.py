import json
import random

QUESTIONS = [
    {
        "question": "What is 2+2?",
        "options": ["3", "4", "5"],
        "answer": 1
    },
    {
        "question": "Capital of France?",
        "options": ["London", "Paris", "Rome"],
        "answer": 1
    },
    {
        "question": "Which is a Python data type?",
        "options": ["int", "car", "house"],
        "answer": 0
    },
]


def load_high_score():
    try:
        with open("high_score.json", "r") as f:
            return json.load(f).get("high_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0


def save_high_score(score):
    with open("high_score.json", "w") as f:
        json.dump({"high_score": score}, f)


def play():
    score = 0
    random.shuffle(QUESTIONS)

    for i, q in enumerate(QUESTIONS):
        print(f"\n{i + 1}. {q['question']}")

        for j, opt in enumerate(q["options"]):
            print(f"  {j + 1}. {opt}")

        while True:
            try:
                guess = int(input("Your answer: "))

                if 1 <= guess <= len(q["options"]):
                    guess -= 1
                    break
                else:
                    print("Please enter a valid option.")

            except ValueError:
                print("Please enter a number.")

        if guess == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Answer was {q['options'][q['answer']]}")

    print(f"\nFinal score: {score}/{len(QUESTIONS)}")
    return score


high = load_high_score()
new = play()

if new > high:
    print("New high score!")
    save_high_score(new)
else:
    print(f"High score remains: {high}")
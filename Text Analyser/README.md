# 📝 Python Sentence Analyzer

A simple command-line **Sentence Analyzer** built using Python. The program takes a sentence from the user and performs several basic string operations.

## 📌 Features

* 🔠 Converts the sentence to uppercase
* 🔡 Converts the sentence to lowercase
* 🔢 Counts the number of words
* 🔄 Replaces spaces with underscores
* 🔍 Checks whether the sentence starts with `"the"`
* ✂️ Displays the first 10 characters
* ⚠️ Handles sentences shorter than 10 characters

## 🛠️ Technologies Used

* **Python 3**
* Python String Methods

No external libraries are required.

## 📂 Project Structure

```text
Python-Sentence-Analyzer/
│
├── sentence_analyzer.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Python-Sentence-Analyzer
```

### 3. Run the program

```bash
python sentence_analyzer.py
```

## 💻 Example Output

```text
enter a sentence: The quick brown fox jumps

THE QUICK BROWN FOX JUMPS
the quick brown fox jumps
5
The_quick_brown_fox_jumps
True
The quick 
```

## 🧠 How It Works

The program first takes a sentence from the user and removes extra whitespace from the beginning and end:

```python
sentence = input("enter a sentence: ").strip()
```

### Convert to Uppercase

```python
print(sentence.upper())
```

Converts all letters to uppercase.

### Convert to Lowercase

```python
print(sentence.lower())
```

Converts all letters to lowercase.

### Count Words

```python
print(len(sentence.split()))
```

`split()` separates the sentence into words, and `len()` counts them.

### Replace Spaces

```python
print(sentence.replace(" ", "_"))
```

Replaces every space with an underscore.

### Check Starting Word

```python
print(sentence.lower().startswith("the"))
```

Converts the sentence to lowercase and checks whether it starts with `"the"`.

For example:

```text
The computer is fast
```

Output:

```text
True
```

### Display First 10 Characters

```python
if len(sentence) > 10:
    print(sentence[:10])
else:
    print("sentence is too short")
```

If the sentence contains more than 10 characters, the first 10 characters are displayed.

Otherwise, the program displays:

```text
sentence is too short
```

## 📚 What I Learned

This project helped me practice:

* `input()`
* Variables
* Strings
* `.strip()`
* `.upper()`
* `.lower()`
* `.split()`
* `.replace()`
* `.startswith()`
* `len()`
* String slicing
* `if-else` statements

## 🚀 Future Improvements

Possible improvements:

* Count characters excluding spaces
* Count vowels and consonants
* Count a specific word
* Find the longest word
* Check whether the sentence is a palindrome
* Display the most frequently used word
* Add better handling for multiple spaces

## 👨‍💻 Author

**Mayank Sharma**

---

⭐ If you found this project useful, consider giving the repository a star!

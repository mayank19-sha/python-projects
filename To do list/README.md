# ✅ Python To-Do List

A simple command-line **To-Do List application** built using Python. The program allows users to add, view, complete, and remove tasks.

Unlike a basic temporary to-do list, this project uses a **JSON file** to save tasks, so your tasks remain available even after closing the program.

## 📌 Features

* 📋 Show all tasks
* ➕ Add new tasks
* ✅ Mark tasks as completed
* 🗑️ Remove tasks
* 💾 Automatically save tasks to a JSON file when exiting
* 📂 Load previously saved tasks when the program starts
* 🔄 Simple menu-driven interface

## 🛠️ Technologies Used

* **Python 3**
* `json` module
* `os` module
* File handling
* Lists and dictionaries
* Functions
* Loops
* Conditional statements

No external libraries are required.

## 📂 Project Structure

```text
Python-To-Do-List/
│
├── todo.py
├── tasks.json
└── README.md
```

> `tasks.json` is created automatically when the program saves your tasks.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Python-To-Do-List
```

### 3. Run the program

```bash
python todo.py
```

## 💻 Example Output

```text
1 show | 2 add | 3 done | 4 remove | 5 exit
> 2
task: Learn Python

1 show | 2 add | 3 done | 4 remove | 5 exit
> 2
task: Practice Git

1 show | 2 add | 3 done | 4 remove | 5 exit
> 1

1. [] Learn Python
2. [] Practice Git
```

### Mark a Task as Done

```text
1 show | 2 add | 3 done | 4 remove | 5 exit
> 3

1. [] Learn Python
2. [] Practice Git

which number: 1
```

The task will then appear as:

```text
1. [x] Learn Python
2. [] Practice Git
```

### Remove a Task

```text
1 show | 2 add | 3 done | 4 remove | 5 exit
> 4

1. [x] Learn Python
2. [] Practice Git

which number: 2
```

The selected task is removed from the list.

## 🧠 How It Works

### Loading Tasks

The program checks whether `tasks.json` exists:

```python
if not os.path.exists(File):
    return []
```

If the file doesn't exist, an empty task list is returned.

If it exists, the program loads the saved JSON data:

```python
with open(File, "r") as f:
    return json.load(f)
```

### Adding Tasks

A task is stored as a dictionary:

```python
{"task": name, "done": False}
```

For example:

```json
[
  {
    "task": "Learn Python",
    "done": false
  },
  {
    "task": "Practice Git",
    "done": true
  }
]
```

### Showing Tasks

The program uses `enumerate()` to give each task a number:

```python
for i, t in enumerate(tasks, 1):
```

It then checks whether the task is completed:

```python
mark = "[x]" if t["done"] else "[]"
```

### Marking Tasks as Done

The selected task is changed from:

```python
"done": False
```

to:

```python
"done": True
```

### Removing Tasks

The selected task is removed using:

```python
tasks.pop(num - 1)
```

`num - 1` is used because Python list indexes start from `0`, while the user sees task numbers starting from `1`.

### Saving Tasks

When the user chooses Exit, the tasks are written to `tasks.json`:

```python
json.dump(tasks, f, indent=2)
```

The `indent=2` makes the JSON file easier to read.

## 📚 What I Learned

This project helped me practice:

* Python functions
* Lists
* Dictionaries
* `while` loops
* `if`, `elif`, and `else`
* `return`
* `break`
* `enumerate()`
* List indexing
* `append()`
* `pop()`
* File handling
* JSON data
* `json.load()`
* `json.dump()`
* `os.path.exists()`
* Menu-driven programs

## 🚀 Future Improvements

Possible improvements:

* ✏️ Edit existing tasks
* 🔍 Search tasks
* 🗂️ Add task categories
* 📅 Add deadlines
* ⭐ Add task priorities
* 📊 Show completed/pending task counts
* ⚠️ Handle invalid task numbers
* 🛡️ Handle invalid JSON files
* 💾 Save after every change instead of only when exiting
* 🖥️ Create a GUI version

## 👨‍💻 Author

**Mayank Sharma**

---

⭐ If you found this project useful, consider giving the repository a star!

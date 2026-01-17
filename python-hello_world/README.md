# Python - Hello, World

## Project Overview
This project introduces absolute beginners to core Python basics: running scripts, printing text and numbers, working with strings, and following coding style (pycodestyle). Each small task focuses on one idea, so you build confidence step by step.

## Resources
- Learn to Program (playlist)
- Whetting Your Appetite
- Using the Python Interpreter
- An Informal Introduction to Python (through 3.1.2 Strings)
- How To Use String Formatters in Python 3
- Pycodestyle – Style Guide for Python Code

## Learning Objectives (mapped to tasks)
- Use the Python interpreter and run scripts (`./file.py`) — tasks 0–7
- Print text and variables with `print()` — tasks 0–3
- Format values with f-strings — tasks 1, 2, 4
- Work with strings: concatenation and repetition — tasks 3, 4
- Apply indexing and slicing for substrings — tasks 3, 5, 6
- Follow Python style with `pycodestyle` — all tasks

## Task-by-Task Explanations

### 0. Hello, print
- **What it does:** Prints a sentence with a leading quote.
- **Concept:** Basic `print()`, escaping quotes.
- **Output example:**
	```
	"Programming is like building a multilingual puzzle
	```
- **Constraint:** Keep shebang `#!/usr/bin/python3`, no extra text.

### 1. Print integer
- **What it does:** Prints an integer followed by text on one line.
- **Concept:** f-strings with integers (no casting).
- **Output example:** `98 Battery street`
- **Constraint:** Do not cast number to string; use `f"{number}"`.

### 2. Print float
- **What it does:** Prints a float with exactly 2 decimal places.
- **Concept:** f-strings with format specifier `:.2f`.
- **Output example:** `Float: 3.14`
- **Constraint:** No string casting; use f-string formatting.

### 3. Print string
- **What it does:** Prints the string 3 times, then its first 9 characters.
- **Concepts:** String repetition (`str * 3`) and slicing (`str[:9]`).
- **Output example:**
	```
	Holberton SchoolHolberton SchoolHolberton School
	Holberton
	```
- **Constraint:** No loops/conditionals; only repetition and slicing.

### 4. Play with strings
- **What it does:** Builds `"Welcome to Holberton School!"` by joining two variables.
- **Concept:** String concatenation and f-strings.
- **Output example:** `Welcome to Holberton School!`
- **Constraint:** Use provided vars `str1`, `str2`; no new vars.

### 5. Copy - Cut - Paste
- **What it does:** Extracts parts of `word` (first 3, last 2, middle) and prints them.
- **Concepts:** Slicing with positive/negative indices.
- **Output example:**
	```
	First 3 letters: Hol
	Last 2 letters: on
	Middle word: olberto
	```
- **Constraint:** No loops/conditionals; use slicing only.

### 6. Create a new sentence
- **What it does:** Rebuilds `object-oriented programming with Python` from slices of a long string.
- **Concepts:** String slicing and concatenation without new literals.
- **Output example:** `object-oriented programming with Python`
- **Constraints:** Exactly 5 lines; no new variables; no new string literals; use slices of the given `str` only.

### 7. Easter Egg
- **What it does:** Prints “The Zen of Python, by Tim Peters”.
- **Concept:** Importing a module (`import this`) to emit text.
- **Constraint:** Script length under 98 characters.

## Key Python Concepts Used
- **f-strings:** Embed values directly: `f"Float: {number:.2f}"`.
- **String slicing:** `word[:3]`, `word[-2:]`, `word[1:-1]` to grab parts of a string.
- **Indexing:** Access characters by position; negative indices count from the end.
- **String concatenation:** Join pieces with `+` or by building new strings from slices.
- **String repetition:** Multiply strings, e.g., `str * 3` to repeat text.
- **Formatting floats:** Use format spec `:.2f` inside f-strings for fixed decimals.

## Code Listings (for reference)
```python
# 0. Hello, print
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")

# 1. Print integer
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")

# 2. Print float
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")

# 3. Print string
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])

# 4. Play with strings
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")

# 5. Copy - Cut - Paste
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

# 6. Create a new sentence
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)

# 7. Easter Egg
#!/usr/bin/python3
import this
```

## Conventions Used
- Shebang on line 1: `#!/usr/bin/python3`
- Every file ends with a newline and is executable (`chmod +x file.py`).
- No loops or conditionals where instructions forbid them—use slicing, concatenation, and f-strings instead.
- Style checked with `pycodestyle` (2.7.*).

## How to Run
- Make scripts executable (one time): `chmod +x 2-print.py 3-print_number.py 4-print_float.py 5-print_string.py 6-concat.py 7-edges.py 8-concat_edges.py 9-easter_egg.py`
- Run a script from the project folder: `./4-print_float.py`
- Expected output appears immediately in the terminal.

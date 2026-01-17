# Python - Hello, World

This project is a gentle entry to Python, focusing on the core syntax elements you will use everywhere: printing, string handling, slicing, and respecting pycodestyle. Below you will find the reference resources, learning objectives, and a short walk-through of each task we implemented.

## Resources
- Learn to Program (playlist)
- Whetting Your Appetite
- Using the Python Interpreter
- An Informal Introduction to Python (through 3.1.2 Strings)
- How To Use String Formatters in Python 3
- Pycodestyle – Style Guide for Python Code

## Learning Objectives
- Use the Python interpreter
- Print text and variables with `print()`
- Work with strings, concatenation, and repetition
- Apply indexing and slicing for substrings
- Follow the official Python coding style with `pycodestyle`

## Task Notes and Key Constructs
- **0. Hello, print**: Basic `print()` with an escaped quote; shebang `#!/usr/bin/python3` and executable bit required.
- **1. Print integer**: `f"{number} Battery street"`—uses f-strings, no casting to `str`.
- **2. Print float**: `f"Float: {number:.2f}"`—format specifier `:.2f` for 2 decimals.
- **3. Print string**: String repetition (`str * 3`) and slicing (`str[:9]`) for prefixes.
- **4. Play with strings**: Concatenate pieces using existing vars: `str1 = str1 + " " + str2`; then print the composed sentence.
- **5. Copy - Cut - Paste**: Slice pieces from `word`:
	- `word_first_3 = word[:3]`
	- `word_last_2 = word[-2:]`
	- `middle_word = word[1:-1]`
- **6. Create a new sentence**: Build `"object-oriented programming with Python"` only from slices of the provided `str`, no new literals or vars:
	- `str = str[39:67] + str[107:112] + str[:6]`
- **7. Easter Egg**: Print the Zen of Python in under 98 chars of source by `import this`.

## Conventions Used
- Shebang on line 1: `#!/usr/bin/python3`
- Every file ends with a newline and is executable (`chmod +x file.py`).
- No loops or conditionals where the instructions forbid them—use slicing, concatenation, and f-strings instead.
- Style checked with `pycodestyle` (2.7.*).

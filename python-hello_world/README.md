# Python - Hello, World

## Project Overview
This project teaches absolute beginners the foundational building blocks of Python: running scripts, printing output, working with strings, and writing clean code. Each task is self-contained and focuses on one core concept, allowing you to build mastery step by step.

## Resources
Before starting, review these materials:
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt) (playlist)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (through 3.1.2 Strings)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)

## Learning Objectives
By completing this project, you will be able to:
- Run Python scripts using the interpreter
- Print text and variables with `print()`
- Format output using f-strings
- Manipulate strings with concatenation, repetition, and slicing
- Extract substrings using indexing and negative indices
- Follow the official Python coding style (pycodestyle)

---

## Task 0: Hello, print

### Goal
Print a sentence that begins with a double quote character.

### Code
**File:** `2-print.py`
```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — **Shebang**. Tells the system to run this file with Python 3.
- **Line 2:** `print("\"Programming is like building a multilingual puzzle")` — Prints the text. The `\"` is an **escape sequence** that prints a literal `"` character.

### Output
```
"Programming is like building a multilingual puzzle
```

### How to Run This Task
```bash
chmod +x 2-print.py
./2-print.py
```
- `chmod +x` makes the file executable
- `./2-print.py` runs the script

---

## Task 1: Print integer

### Goal
Print an integer variable followed by text on the same line, without manually converting it to a string.

### Code
**File:** `3-print_number.py`
```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2:** `number = 98` — Assigns the integer `98` to the variable `number`.
- **Line 3:** `print(f"{number} Battery street")` — Uses an **f-string** to embed the variable directly into the text. No type casting is needed.

**Constraint:** You cannot use `str(number)`. F-strings handle this automatically.

### Output
```
98 Battery street
```

### How to Run This Task
```bash
chmod +x 3-print_number.py
./3-print_number.py
```

---

## Task 2: Print float

### Goal
Print a floating-point number with exactly 2 decimal places.

### Code
**File:** `4-print_float.py`
```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2:** `number = 3.14159` — Assigns a float value.
- **Line 3:** `print(f"Float: {number:.2f}")` — Uses an f-string with the format specifier `:.2f` to display exactly 2 decimal places.

**Constraint:** You cannot cast `number` to a string. Use f-string formatting instead.

### Output
```
Float: 3.14
```

### How to Run This Task
```bash
chmod +x 4-print_float.py
./4-print_float.py
```

---

## Task 3: Print string

### Goal
Print a string 3 times in a row, then print its first 9 characters on a new line.

### Code
**File:** `5-print_string.py`
```python
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2:** `str = "Holberton School"` — Assigns a string.
- **Line 3:** `print(str * 3)` — **String repetition**. Multiplying a string by 3 repeats it 3 times.
- **Line 4:** `print(str[:9])` — **String slicing**. `[:9]` means "from the start up to (but not including) index 9."

**Constraint:** No loops or conditionals allowed. Use string operations only.

### Output
```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

### How to Run This Task
```bash
chmod +x 5-print_string.py
./5-print_string.py
```

---

## Task 4: Play with strings

### Goal
Build the sentence "Welcome to Holberton School!" by combining two existing variables.

### Code
**File:** `6-concat.py`
```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2-3:** `str1 = "Holberton"` and `str2 = "School"` — Two string variables.
- **Line 4:** `str1 = str1 + " " + str2` — **String concatenation**. Joins `str1`, a space, and `str2` into one string, then reassigns it to `str1`.
- **Line 5:** `print(f"Welcome to {str1}!")` — Uses an f-string to embed the combined value.

**Constraint:** Must use both `str1` and `str2`. No new variables allowed.

### Output
```
Welcome to Holberton School!
```

### How to Run This Task
```bash
chmod +x 6-concat.py
./6-concat.py
```

---

## Task 5: Copy - Cut - Paste

### Goal
Extract and print the first 3 letters, last 2 letters, and middle portion of a word using slicing.

### Code
**File:** `7-edges.py`
```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2:** `word = "Holberton"` — The string to slice.
- **Line 3:** `word_first_3 = word[:3]` — Slice from start to index 3 (characters at positions 0, 1, 2).
- **Line 4:** `word_last_2 = word[-2:]` — **Negative indexing**. `-2:` means "start 2 characters from the end to the end."
- **Line 5:** `middle_word = word[1:-1]` — From index 1 to one before the last character (excludes first and last).
- **Lines 6-8:** Print each sliced result using f-strings.

**Constraint:** No loops or conditionals. Use slicing only.

### Output
```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

### How to Run This Task
```bash
chmod +x 7-edges.py
./7-edges.py
```

---

## Task 6: Create a new sentence

### Goal
Build the phrase "object-oriented programming with Python" using only slices from a provided long string.

### Code
**File:** `8-concat_edges.py`
```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Lines 2-3:** `str = "Python is..."` — A long string split across two lines using `\` (line continuation).
- **Line 4:** `str = str[39:67] + str[107:112] + str[:6]` — Slices three parts:
  - `str[39:67]` → `"object-oriented programming"`
  - `str[107:112]` → `" with"`
  - `str[:6]` → `"Python"`
  - Concatenates them to form `"object-oriented programming with Python"`
- **Line 5:** `print(str)` — Prints the reassembled string.

**Constraints:** Exactly 5 lines. No new variables. No new string literals.

### Output
```
object-oriented programming with Python
```

### How to Run This Task
```bash
chmod +x 8-concat_edges.py
./8-concat_edges.py
```

---

## Task 7: Easter Egg

### Goal
Print "The Zen of Python, by Tim Peters" and the full Zen text using fewer than 98 characters of source code.

### Code
**File:** `9-easter_egg.py`
```python
#!/usr/bin/python3
import this
```

### Line-by-Line Explanation
- **Line 1:** `#!/usr/bin/python3` — Shebang line.
- **Line 2:** `import this` — Imports a special Python module that automatically prints the Zen of Python when loaded.

**Constraint:** The entire script must be under 98 characters.

### Output
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
...
```
(Full Zen output displayed)

### How to Run This Task
```bash
chmod +x 9-easter_egg.py
./9-easter_egg.py
```

---

## Making Python Scripts Executable

### What does `chmod +x` mean?
- `chmod` changes file permissions
- `+x` adds **execute permission**, allowing the file to run as a program

### Why use `./script.py` instead of `python3 script.py`?
- `./script.py` runs the file directly using the shebang interpreter
- `python3 script.py` explicitly calls Python, ignoring the shebang
- The `./` prefix tells the shell to look in the current directory

### When is execution permission needed?
- Only when running scripts with `./filename`
- Not needed if you run with `python3 filename`

---

## Common Beginner Mistakes

### 1. Forgetting the Shebang
❌ **Wrong:**
```python
print("Hello")
```
✅ **Correct:**
```python
#!/usr/bin/python3
print("Hello")
```

### 2. Missing Execute Permission
❌ **Error:** `bash: ./script.py: Permission denied`  
✅ **Fix:** Run `chmod +x script.py` first

### 3. Using Forbidden Constructs
❌ **Wrong (Task 3):**
```python
for i in range(3):
    print(str)
```
✅ **Correct:**
```python
print(str * 3)
```

### 4. Casting When Not Allowed
❌ **Wrong (Task 1):**
```python
print(str(number) + " Battery street")
```
✅ **Correct:**
```python
print(f"{number} Battery street")
```

---

## Key Takeaways

By completing this project, you have learned:
- ✅ How to write and execute Python scripts with proper shebang lines
- ✅ The `print()` function for displaying output
- ✅ F-strings for embedding variables and formatting numbers
- ✅ String operations: concatenation (`+`), repetition (`*`), slicing (`[:]`)
- ✅ Indexing with positive and negative indices
- ✅ How to follow Python coding conventions (pycodestyle)
- ✅ Problem-solving under constraints (no loops, no casting, etc.)

---

## Repository Information
- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-hello_world`
- **Files:** `2-print.py`, `3-print_number.py`, `4-print_float.py`, `5-print_string.py`, `6-concat.py`, `7-edges.py`, `8-concat_edges.py`, `9-easter_egg.py`

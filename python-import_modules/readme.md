# Python: Import & Modules

This project introduces the basics of **importing modules** in Python, how to use functions from other files, and why modular code is important.

---

## 📚 Project Overview

You will learn:
- How to use the `import` statement to bring in code from other files (modules)
- How to call functions defined in another Python file
- Why modular programming makes your code easier to organize and reuse

---

## 🧠 Learning Objectives

- **What is a module?**
  A module is a file containing Python code (functions, variables, etc.) that you can use in other programs.

- **How to import a module:**
  Use `import module_name` or `from module_name import function_name`.

- **Why use modules?**
  - Organize code into logical files
  - Reuse code without copying and pasting
  - Make your programs easier to read and maintain

- **The `__name__ == "__main__"` trick:**
  This lets you write code that only runs when the file is executed directly, not when it is imported.

---

## 📝 Task Explanation

### 0. Import a simple function from a simple file

**Goal:**
Import the function `add` from the file `add_0.py` and use it to add two numbers.

**Logic:**
- Import the `add` function using `from add_0 import add`
- Define two variables, `a` and `b`
- Print the result using string formatting

**Python Concepts Used:**
- `import` statement
- Function call
- String formatting with `.format()`
- The `__name__ == "__main__"` check

**Example Output:**
```
1 + 2 = 3
```

---

## 🗂️ File Descriptions

- **0-add.py**
  Main script. Imports the `add` function and prints the sum of two numbers.

- **add_0.py**
  Contains the `add(a, b)` function, which returns the sum of `a` and `b`.

---

## 🐍 Python Keywords & Concepts Reference

- **import**: Used to bring in code from another file.
- **from ... import ...**: Import specific functions or variables from a module.
- **def**: Used to define a function.
- **return**: Used to return a value from a function.
- **if __name__ == "__main__":**: Ensures code only runs when the file is executed directly.

---

## 📝 Example: How importing works

Suppose you have two files:

**add_0.py**
```python
def add(a, b):
    return a + b
```

**0-add.py**
```python
from add_0 import add
print(add(1, 2))  # Output: 3
```

---

## 🛠️ How to Run

1. Make sure both `0-add.py` and `add_0.py` are in the same directory.
2. Run the main script:
   ```bash
   ./0-add.py
   ```
   or
   ```bash
   python3 0-add.py
   ```

---

## 📖 Resources

- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [PEP8 Style Guide](https://peps.python.org/pep-0008/)
- [Python String Formatting](https://docs.python.org/3/library/string.html#formatstrings)

---

## 💡 Tips

- Always use clear and descriptive names for your modules and functions.
- Use the `__name__ == "__main__"` check to make your scripts reusable as both standalone programs and importable modules.

---

Happy coding!

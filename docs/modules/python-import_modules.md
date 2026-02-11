# Module: python-import_modules

## 1. Executive Summary

This module teaches **code modularization** — the ability to split functionality across files and import it where needed. Students learn `import` mechanics, `from...import` syntax, `sys.argv` for command-line arguments, the `if __name__ == "__main__"` guard pattern, and module introspection with `dir()`. These skills are essential for organizing any non-trivial Python project and building command-line tools.

---

## 2. Deep Concept Breakdown

### 2.1 Python Import System

**Formal definition:** The import system allows loading code from other modules (Python files) into the current namespace. Python searches `sys.path` for modules.

```python
import module_name                    # Import entire module
from module_name import function      # Import specific name
from module_name import func1, func2  # Import multiple names
```

**Runtime behavior:**
1. Python checks `sys.modules` cache first.
2. If not cached, Python searches `sys.path` directories.
3. The module is executed (top-to-bottom) on first import.
4. Subsequent imports reuse the cached module object.

**Common mistakes:**
- Circular imports (module A imports B, B imports A).
- Importing mutable objects — changes to imported mutable objects affect all importers.
- Assuming import order doesn't matter (it does, for side effects).

### 2.2 The `__name__` Guard

**Formal definition:** `__name__` is a special variable that equals `"__main__"` when a script is run directly, or the module's name when imported.

```python
if __name__ == "__main__":
    # This code runs only when the file is executed directly
    main()
```

**Production relevance:** Every Python package's entry point uses this pattern. It prevents unintended code execution during imports and enables modules to serve dual roles as both importable libraries and standalone scripts.

### 2.3 Command-Line Arguments

**Formal definition:** `sys.argv` is a list of strings representing command-line arguments. `sys.argv[0]` is the script name.

```python
import sys

script_name = sys.argv[0]       # "my_script.py"
first_arg = sys.argv[1]         # First user-provided argument
all_args = sys.argv[1:]         # All arguments except script name
```

**Production best practice:** For complex CLI tools, use `argparse` or `click` instead of raw `sys.argv` parsing.

### 2.4 Module Introspection with `dir()`

**Formal definition:** `dir(obj)` returns a sorted list of names in the object's namespace. Without arguments, it returns names in the current scope.

```python
import math
dir(math)      # ['acos', 'asin', 'atan', ..., 'tau']
dir()          # Names in current scope
```

---

## 3. Task-Level Static Analysis

### Task: 0-add.py

- **Problem statement:** Import `add` from `add_0.py` and print the result of `1 + 2`.
- **Design approach:** `from add_0 import add` with `__name__` guard.
- **OOP principles:** None — procedural.
- **Control flow:** Linear — import, compute, print.
- **Time complexity:** O(1)
- **Real-world analogy:** Importing a utility function from a shared library module.

### Task: 1-calculation.py

- **Problem statement:** Import four arithmetic functions and demonstrate each.
- **Design approach:** `from calculator_1 import add, sub, mul, div` with formatted output.
- **Control flow:** Sequential — four function calls.
- **Time complexity:** O(1)
- **Real-world analogy:** Using a math utility library in a financial calculation service.

### Task: 2-args.py

- **Problem statement:** Print the count and list of CLI arguments with proper grammar.
- **Design approach:** `sys.argv` length check with grammar-aware singular/plural output.
- **Control flow:** Conditional (0, 1, or many args) followed by iteration.
- **Edge-case coverage:** Handles 0 arguments ("No arguments"), 1 argument ("1 argument"), and n arguments ("n arguments").
- **Time complexity:** O(n) where n = number of arguments.
- **Real-world analogy:** CLI help/usage messages in command-line tools.

### Task: 3-infinite_add.py

- **Problem statement:** Sum all CLI arguments as integers.
- **Design approach:** Loop over `sys.argv[1:]`, convert each to `int()`, accumulate sum.
- **Control flow:** Accumulator loop.
- **Edge-case coverage:** ⚠️ No error handling for non-integer arguments.
- **Time complexity:** O(n)
- **Potential improvements:** Add `try`/`except ValueError` for invalid inputs.
- **Real-world analogy:** Batch processing numeric data from CLI input.

### Task: 4-hidden_discovery.py

- **Problem statement:** Import a hidden module and list all non-private attributes.
- **Design approach:** `dir()` introspection with string filtering (`not name.startswith("__")`).
- **Control flow:** Import → filter → print loop.
- **Time complexity:** O(n) where n = number of attributes.
- **Real-world analogy:** Plugin discovery — dynamically detecting available features in a module.

### Task: 5-variable_load.py

- **Problem statement:** Import a variable from another module and print it.
- **Design approach:** `from variable_load_5 import a`.
- **Control flow:** Linear.
- **Time complexity:** O(1)
- **Real-world analogy:** Loading configuration constants from a config module.

### Supporting Module: add_0.py

- **Purpose:** Helper module providing `add(a, b)` function.
- **Quality:** Clean implementation with docstring.

### Supporting Module: calculator_1.py

- **Purpose:** Helper module providing `add`, `sub`, `mul`, `div` functions.
- **Quality:** Good docstrings on all functions. Note: `div()` uses `int(a/b)` instead of `a // b` for integer division.

### Supporting Module: variable_load_5.py

- **Purpose:** Exports a single variable `a = 98`.
- **Quality:** Simple and correct.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Separation of Concerns | ✅ | Utility functions in separate modules (`add_0.py`, `calculator_1.py`) |
| Module Guard | ✅ | `if __name__ == "__main__"` in `0-add.py`, `1-calculation.py` |
| Defensive Programming | ⚠️ | Missing in `3-infinite_add.py` (no input validation) |
| Introspection | ✅ | `4-hidden_discovery.py` uses `dir()` for dynamic discovery |

---

## 5. Built-ins & Keywords Deep Dive

### `import` and `from...import`

```python
import os                           # Full module import
from os.path import join, exists    # Selective import
from os import *                    # Wildcard import (discouraged)
import numpy as np                  # Aliased import
```

### `sys.argv`

```python
import sys
# Command: python script.py hello 42
sys.argv[0]    # "script.py"
sys.argv[1]    # "hello"
sys.argv[2]    # "42" (always a string)
len(sys.argv)  # 3
```

### `dir()`

```python
class MyClass:
    x = 1
    def method(self): pass

dir(MyClass)
# ['__class__', '__dict__', ..., 'method', 'x']

obj = MyClass()
dir(obj)
# ['__class__', '__dict__', ..., 'method', 'x']
```

### `__import__()`

```python
# Dynamic import (used in test files)
module = __import__("module_name")
func = getattr(module, "function_name")

# Equivalent to:
import module_name
func = module_name.function_name
```

**Note:** `__import__()` is used in the curriculum's test files for dynamic loading. In production, prefer `importlib.import_module()`.

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between `import module` and `from module import function`? How do they affect the namespace?
2. Explain how Python's import caching works. What is `sys.modules`?
3. What is a circular import? How can it be resolved?
4. Why is `from module import *` considered bad practice?
5. Explain the purpose of `if __name__ == "__main__"`. What value does `__name__` have when a module is imported vs. run directly?

### Practical Coding Questions

1. Write a CLI tool that accepts `--help`, `--verbose`, and a filename argument using `sys.argv`.
2. Create a module that exports three functions and a constant, with an `if __name__ == "__main__"` block that tests each function.
3. Write a function that dynamically imports a module by name and calls a specified function from it.
4. Implement a `sum_args.py` script that sums all CLI arguments, handling non-numeric inputs gracefully.
5. Write a script that lists all public functions (not starting with `_`) in a given module name provided as a CLI argument.

### Debugging Scenarios

1. A developer writes `from math import *` and later calls `log("message")`. It crashes with `TypeError`. Why?
2. Two modules import each other: `a.py` imports from `b.py`, and `b.py` imports from `a.py`. One of them gets `ImportError`. Explain the cause and fix.

### System Design Question

1. Design a plugin system where third-party developers can drop Python files into a `plugins/` directory, and your application automatically discovers and loads them. What import mechanisms would you use? How would you handle errors in plugin code?

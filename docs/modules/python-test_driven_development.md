# Module: python-test_driven_development

## 1. Executive Summary

This module introduces **Test-Driven Development (TDD)** — the practice of writing tests before implementation. Students learn to use Python's `doctest` and `unittest` frameworks, design comprehensive test suites covering edge cases, and write functions with clear contracts. TDD is a cornerstone of professional software engineering, ensuring correctness, enabling refactoring, and serving as executable documentation.

---

## 2. Deep Concept Breakdown

### 2.1 Test-Driven Development Methodology

**Formal definition:** TDD follows the Red-Green-Refactor cycle:
1. **Red:** Write a failing test that defines expected behavior.
2. **Green:** Write the minimum code to make the test pass.
3. **Refactor:** Improve the implementation without changing behavior.

**Production relevance:** TDD is standard practice at companies like Google, Microsoft, and Thoughtworks. It reduces bug density, improves design, and provides regression safety nets.

### 2.2 Doctest

**Formal definition:** Doctest embeds test cases inside docstrings as interactive Python sessions.

```python
def add(a, b):
    """
    Add two numbers.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b
```

**Execution:** `python -m doctest -v module.py` or `python -m doctest tests/file.txt`

**Limitations:** Doctests are fragile for complex output (dictionaries, floating-point numbers). They cannot easily test exceptions with custom messages.

### 2.3 Unittest

**Formal definition:** `unittest` is Python's standard testing framework, inspired by JUnit. It uses class-based test organization with assertion methods.

```python
import unittest

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
```

**Key assertions:**
- `assertEqual(a, b)` — values are equal
- `assertRaises(Error)` — exception is raised
- `assertIsNone(x)` — value is None
- `assertTrue(x)` / `assertFalse(x)` — boolean checks

### 2.4 Input Validation Patterns

The functions in this module demonstrate a consistent validation pattern:

```python
def func(param):
    if not isinstance(param, int):
        raise TypeError("param must be an integer")
    if param < 0:
        raise ValueError("param must be >= 0")
    # ... implementation
```

This pattern appears in `0-add_integer.py`, `2-matrix_divided.py`, `3-say_my_name.py`, `4-print_square.py`, and `5-text_indentation.py`.

---

## 3. Task-Level Static Analysis

### Task: 0-add_integer.py

- **Problem statement:** Add two integers, converting floats to ints first.
- **Design approach:** Type validation with `isinstance()`, float-to-int conversion, then addition.
- **Edge-case coverage:** Handles `float('inf')` and `float('nan')` via `int()` conversion errors. Tested in `tests/0-add_integer.txt`.
- **Time complexity:** O(1)
- **Potential improvements:** Error message says "must be an integer" but accepts floats — slightly misleading.
- **Real-world analogy:** API parameter validation with type coercion.

### Task: 2-matrix_divided.py

- **Problem statement:** Divide all elements of a matrix by a divisor, rounding to 2 decimal places.
- **Design approach:** Comprehensive validation (matrix structure, element types, row sizes, divisor type, division by zero).
- **Edge-case coverage:** Tested with `float('inf')`, uneven rows, zero divisor, non-numeric elements.
- **Time complexity:** O(m × n) where m = rows, n = columns.
- **Space complexity:** O(m × n) — creates a new matrix.
- **Potential improvements:** Repeated error message strings could be constants.
- **Real-world analogy:** Normalizing a dataset — dividing all values by a scaling factor.

### Task: 3-say_my_name.py

- **Problem statement:** Print a formatted full name with string type validation.
- **Design approach:** `isinstance()` checks for both parameters.
- **Edge-case coverage:** Tested with empty strings, non-string types, missing arguments.
- **Time complexity:** O(1)
- **Real-world analogy:** User registration form validation.

### Task: 4-print_square.py

- **Problem statement:** Print a square using `#` characters.
- **Design approach:** Type and value validation, then nested `print("#" * size)`.
- **Edge-case coverage:** Handles float input (raises TypeError), negative size, zero size.
- **Time complexity:** O(n²) for printing.
- **Real-world analogy:** Rendering a fixed-size UI component.

### Task: 5-text_indentation.py

- **Problem statement:** Format text with double newlines after `.`, `?`, `:`.
- **Design approach:** Character-by-character iteration with buffer accumulation.
- **Control flow:** Buffer collects characters until a delimiter is found, then flushes with newlines.
- **Edge-case coverage:** Consecutive delimiters, leading/trailing spaces per line.
- **Time complexity:** O(n) — single pass through the string.
- **Space complexity:** O(n) for the buffer.
- **Potential improvements:** String concatenation in loop could use `io.StringIO` for better performance.
- **Real-world analogy:** Text preprocessing for NLP pipelines or email formatting.

### Task: 6-max_integer.py

- **Problem statement:** Find the maximum integer in a list.
- **Design approach:** Linear scan with comparison.
- **Edge-case coverage:** Empty list returns `None`.
- **Time complexity:** O(n)
- **Potential improvements:** Mutable default `list=[]` AND shadows built-in `list`.
- **Real-world analogy:** Finding the highest bid in an auction system.

### Task: tests/6-max_integer_test.py

- **Problem statement:** Unit tests for `max_integer()`.
- **Design approach:** `unittest.TestCase` with multiple test methods.
- **Test coverage:** Tests ordered list, unordered, single element, empty list, negative numbers, duplicates.
- **Real-world analogy:** Production-grade test suite for a utility function.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| TDD Methodology | ✅ | Tests exist before or alongside implementations |
| Input Validation | ✅ | Every function validates types and values |
| Defensive Programming | ✅ | Comprehensive edge-case handling |
| Contract Design | ✅ | Doctest files serve as executable contracts |
| Separation of Tests | ✅ | Tests in separate `tests/` directory |

---

## 5. Built-ins & Keywords Deep Dive

### `isinstance()`

```python
isinstance(42, int)           # True
isinstance(3.14, (int, float))  # True — multiple types
isinstance(True, int)          # True — bool is subclass of int!
isinstance(True, bool)         # True
```

**Warning:** `isinstance(True, int)` returns `True`. To exclude booleans: `isinstance(x, int) and not isinstance(x, bool)`.

### `type()`

```python
type(42)          # <class 'int'>
type("hello")     # <class 'str'>
type(42) is int   # True — exact type match (no inheritance)
```

### `round()`

```python
round(3.14159, 2)    # 3.14
round(2.5)           # 2   — banker's rounding (rounds to nearest even)
round(3.5)           # 4
```

**Warning:** Python uses "banker's rounding" (round half to even), not traditional rounding. This can surprise developers.

### `doctest` module

```python
# Run doctests from command line:
# python -m doctest -v tests/0-add_integer.txt

# Run doctests programmatically:
import doctest
doctest.testmod(verbose=True)
```

### `unittest` module

```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(my_func(1), 2)

    def test_raises(self):
        with self.assertRaises(TypeError):
            my_func("string")

if __name__ == "__main__":
    unittest.main()
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is TDD? Describe the Red-Green-Refactor cycle.
2. What is the difference between `doctest` and `unittest`? When would you use each?
3. Why is testing important in production software? What types of bugs do tests prevent?
4. What is code coverage? Is 100% coverage always desirable?
5. Explain the testing pyramid (unit tests, integration tests, end-to-end tests). Where does each type fit?

### Practical Coding Questions

1. Write a function and its complete doctest suite that validates an email address format.
2. Create a unittest test class for a `Calculator` class with `add`, `subtract`, `multiply`, and `divide` methods.
3. Write a parameterized test (using `unittest.subTest`) that tests a function with 10 different inputs.
4. Implement a function that parses dates from strings, with tests covering valid formats, invalid formats, and edge cases.
5. Write tests for a function that should raise different exceptions for different invalid inputs.

### Debugging Scenarios

1. A doctest fails because the expected output is `{1: 'a', 2: 'b'}` but the actual output has different key ordering. How do you fix the test?
2. A unittest passes when run alone but fails when run with the full test suite. What could cause this? How do you debug it?

### System Design Question

1. Design a testing strategy for a REST API with 20 endpoints. How would you organize unit tests, integration tests, and end-to-end tests? What tools and patterns would you use? How would you handle test data setup and teardown?

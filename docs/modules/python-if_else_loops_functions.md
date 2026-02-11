# Module: python-if_else_loops_functions

## 1. Executive Summary

This module transitions students from basic output to **control flow** — the ability to make decisions, repeat actions, and organize code into reusable units. It covers conditionals (`if`/`elif`/`else`), loops (`for`/`while`), functions (`def`), and low-level character manipulation using ASCII codes. These are the building blocks of all algorithmic thinking and are directly applicable to backend business logic, request routing, and data processing.

---

## 2. Deep Concept Breakdown

### 2.1 Conditional Statements

**Formal definition:** Conditional statements evaluate boolean expressions and execute code blocks based on their truthiness.

```python
if condition:
    # executes when condition is truthy
elif other_condition:
    # executes when first is falsy, second is truthy
else:
    # executes when all conditions are falsy
```

**Runtime behavior:** Python evaluates conditions top-to-bottom. Short-circuit evaluation applies: in `a and b`, if `a` is falsy, `b` is never evaluated.

**Truthiness rules:**
- Falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`
- Truthy: Everything else

**Common mistakes:**
- Using `==` when `is` is appropriate (identity vs equality).
- Forgetting that `elif` is checked only if previous conditions were falsy.

### 2.2 For Loops

**Formal definition:** `for` loops iterate over any iterable object (list, range, string, etc.), binding each element to a loop variable.

```python
for i in range(10):         # iterates 0..9
    print(i)

for char in "hello":        # iterates over characters
    print(char)

for i in range(start, stop, step):
    print(i)
```

**Performance notes:** `range()` produces values lazily (it is an iterator in Python 3), so `range(1_000_000)` does not create a million-element list in memory.

### 2.3 Functions

**Formal definition:** A function is a named, reusable block of code that accepts parameters, executes a body, and optionally returns a value.

```python
def function_name(param1, param2=default_value):
    """Docstring describing the function."""
    # body
    return result
```

**Scope:** Variables defined inside a function are local. Python follows the LEGB rule (Local → Enclosing → Global → Built-in) for name resolution.

**Common mistakes:**
- Forgetting `return` — the function implicitly returns `None`.
- Modifying a mutable default argument.

### 2.4 ASCII Manipulation

**Formal definition:** `ord()` converts a character to its ASCII/Unicode code point; `chr()` converts a code point back to a character.

```python
ord('a')     # 97
ord('z')     # 122
chr(65)      # 'A'
chr(97)      # 'a'
```

**Common mistakes:** Using magic numbers (97, 122) instead of `ord('a')`, `ord('z')`.

### 2.5 The Modulo Operator

```python
10 % 3       # 1   — remainder of division
-7 % 10      # 3   — Python's modulo always returns non-negative for positive divisor
15 % 5       # 0   — divisible check
```

**Production relevance:** Used for FizzBuzz-style logic, circular array indexing, hash table implementations, and pagination calculations.

---

## 3. Task-Level Static Analysis

### Task: 0-positive_or_negative.py

- **Problem statement:** Generate a random number and classify it as positive, negative, or zero.
- **Design approach:** `random.randint(-10, 10)` followed by `if`/`elif`/`else` chain.
- **OOP principles:** None — procedural.
- **Control flow:** Three-branch conditional.
- **Edge-case coverage:** Zero is handled as a distinct case.
- **Time complexity:** O(1)
- **Space complexity:** O(1)
- **Real-world analogy:** Input validation in a form handler — classifying user input into categories.

### Task: 1-last_digit.py

- **Problem statement:** Extract and classify the last digit of a random number.
- **Design approach:** Modulo operation with special handling for negative numbers.
- **Control flow:** Extraction followed by three-branch conditional.
- **Edge-case coverage:** Negative modulo behavior correctly handled.
- **Time complexity:** O(1)
- **Potential improvements:** Document Python's modulo behavior for negative numbers more prominently.
- **Real-world analogy:** Check digit validation (e.g., Luhn algorithm for credit cards).

### Task: 2-print_alphabet.py

- **Problem statement:** Print the lowercase alphabet on a single line.
- **Design approach:** `for` loop over `range(97, 123)` with `chr()` conversion.
- **Time complexity:** O(1) — fixed 26 iterations.
- **Real-world analogy:** Generating character sets for input validation or password policies.

### Task: 3-print_alphabt.py

- **Problem statement:** Print the alphabet excluding 'e' and 'q'.
- **Design approach:** Loop with conditional skip using ASCII code comparison.
- **Potential improvements:** Use `chr()` comparisons instead of magic numbers: `chr(i) not in ('e', 'q')`.
- **Real-world analogy:** Filtering characters for sanitization (e.g., removing special characters from usernames).

### Task: 4-print_hexa.py

- **Problem statement:** Print numbers 0–98 in decimal and hexadecimal format.
- **Design approach:** Loop with dual format specifiers (`:d` and `:x`).
- **Time complexity:** O(n) where n=99.
- **Real-world analogy:** Debug output for memory addresses or color codes.

### Task: 5-print_comb2.py

- **Problem statement:** Print all two-digit numbers (00–99) with comma separation.
- **Design approach:** Single loop with zero-padded formatting and conditional trailing comma.
- **Time complexity:** O(n) where n=100.
- **Real-world analogy:** Generating formatted option lists for dropdowns or reports.

### Task: 6-print_comb3.py

- **Problem statement:** Print all unique two-digit combinations where the second digit is greater.
- **Design approach:** Nested loops with inner loop starting at `i + 1`.
- **Time complexity:** O(n²) — specifically C(10,2) = 45 combinations.
- **Real-world analogy:** Generating unique pair combinations (e.g., tournament matchups, A/B test pairs).

### Task: 7-islower.py

- **Problem statement:** Check if a character is lowercase without using `str.islower()`.
- **Design approach:** ASCII range check using `ord()`.
- **Control flow:** Boolean return based on range comparison.
- **Potential improvements:** Replace magic numbers 97/122 with `ord('a')`/`ord('z')`.
- **Real-world analogy:** Custom input validation for password strength checkers.

### Task: 8-uppercase.py

- **Problem statement:** Convert a string to uppercase without using `str.upper()`.
- **Design approach:** ASCII manipulation — subtract 32 from lowercase character codes.
- **Time complexity:** O(n) where n is string length.
- **Potential improvements:** Use `ord('a')` and `ord('A')` instead of magic number 32.
- **Real-world analogy:** Case-insensitive comparison in database queries.

### Task: 9-print_last_digit.py

- **Problem statement:** Print and return the last digit of a number.
- **Design approach:** `abs()` + modulo 10.
- **Edge-case coverage:** Handles negative numbers via `abs()`.
- **Real-world analogy:** Extracting check digits from identifiers.

### Task: 10-add.py

- **Problem statement:** Add two integers.
- **Design approach:** Direct `return a + b`.
- **Time complexity:** O(1)
- **Real-world analogy:** Arithmetic operations in a calculator service or shopping cart total.

### Task: 11-pow.py

- **Problem statement:** Compute a raised to the power of b.
- **Design approach:** Python's `**` operator.
- **Time complexity:** O(log b) — Python uses fast exponentiation.
- **Real-world analogy:** Cryptographic operations, compound interest calculations.

### Task: 12-fizzbuzz.py

- **Problem statement:** Classic FizzBuzz — print 1–100 with Fizz/Buzz/FizzBuzz substitutions.
- **Design approach:** Loop with modulo checks, `i % 15` checked first for FizzBuzz.
- **Time complexity:** O(n) where n=100.
- **Edge-case coverage:** Correct ordering of conditions (15 before 3 and 5).
- **Real-world analogy:** The most common technical interview screening question; demonstrates understanding of modular arithmetic and conditional logic.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Defensive Programming | ✅ | `1-last_digit.py` — handles negative modulo edge case |
| Constraint-Based Design | ✅ | `7-islower.py`, `8-uppercase.py` — manual ASCII without built-ins |
| Early Return | ❌ | Most functions use full conditional chains |

---

## 5. Built-ins & Keywords Deep Dive

### `range()`

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(10, 0, -1)  # 10, 9, 8, ..., 1
```

`range()` returns a lazy iterator — memory-efficient for large ranges.

### `chr()` and `ord()`

```python
chr(65)    # 'A'
ord('A')   # 65
chr(ord('a') + 3)  # 'd' — arithmetic on character codes
```

### `abs()`

```python
abs(-5)      # 5
abs(3.14)    # 3.14
abs(0)       # 0
```

### `random.randint()`

```python
import random
random.randint(1, 10)    # Random integer in [1, 10] (inclusive both ends)
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. Explain the difference between `for` and `while` loops. When would you choose one over the other?
2. What is short-circuit evaluation in Python? Give an example with `and` and `or`.
3. Explain Python's LEGB scope rule. What happens when a local variable has the same name as a global?
4. Why does `range()` not create a list in Python 3? What design pattern does this follow?
5. What are the truthiness rules in Python? Name all falsy values.

### Practical Coding Questions

1. Write a function that determines if a year is a leap year using only `if`/`elif`/`else`.
2. Implement FizzBuzz for numbers 1–n where n is a parameter.
3. Write a function that converts a string to alternating case (e.g., `"hello"` → `"hElLo"`) using only `ord()` and `chr()`.
4. Write a function that prints a multiplication table for n×n using nested loops.
5. Implement a function that returns the nth Fibonacci number using a loop (not recursion).

### Debugging Scenarios

1. A function uses `if x = 5` instead of `if x == 5`. What error occurs, and why?
2. A loop uses `for i in range(len(my_list))` and modifies `my_list` inside the loop. What unexpected behavior might occur?

### System Design Question

1. Design a simple rule engine that evaluates a series of conditions on incoming data (e.g., age >= 18, country in ["US", "CA"]) and returns a decision. How would you organize the conditional logic to be extensible and maintainable?

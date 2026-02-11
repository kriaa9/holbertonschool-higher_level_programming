# Module: python-hello_world

## 1. Executive Summary

This module is the entry point to the Python curriculum. It introduces the most fundamental operations in any programming language: producing output and manipulating text. Students learn `print()`, string formatting with f-strings, string repetition, string slicing, and the Zen of Python. Every subsequent module builds on the output mechanics established here.

---

## 2. Deep Concept Breakdown

### 2.1 The `print()` Function

**Formal definition:** `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)` is a built-in function that writes string representations of objects to a text stream.

**Python syntax:**
```python
print("Hello, World!")
print(f"Value: {x}")
print("no newline", end="")
```

**Runtime behavior:** `print()` calls `str()` on each argument, joins them with `sep`, appends `end`, and writes to `file`. By default, output is line-buffered when connected to a terminal.

**Common mistakes:**
- Forgetting that `print()` returns `None`, not the string.
- Using `+` for concatenation inside `print()` instead of commas or f-strings.

**Production best practice:** In production code, prefer the `logging` module over `print()` for its configurability, log levels, and output routing.

### 2.2 F-Strings (Formatted String Literals)

**Formal definition:** F-strings (PEP 498, Python 3.6+) allow embedding expressions inside string literals using `{expression}` syntax, with optional format specifications.

**Python syntax:**
```python
name = "World"
pi = 3.14159
print(f"Hello, {name}!")        # Expression embedding
print(f"Pi: {pi:.2f}")          # Format specification
print(f"{'centered':^20}")      # Alignment
```

**Performance notes:** F-strings are evaluated at runtime and are faster than `str.format()` and `%` formatting because they are compiled to efficient bytecode.

**Common mistakes:**
- Using f-strings with expressions that have side effects.
- Forgetting the `f` prefix, resulting in literal `{variable}` in output.

### 2.3 String Slicing

**Formal definition:** String slicing extracts a substring using `string[start:stop:step]` notation, where `start` is inclusive and `stop` is exclusive.

**Python syntax:**
```python
word = "Holberton"
word[:3]      # "Hol"     — first 3 characters
word[-2:]     # "on"      — last 2 characters
word[1:-1]    # "olberto" — exclude first and last
word[::2]     # "Hleto"   — every other character
```

**Memory model implications:** Slicing creates a *new string object*. Strings are immutable in Python, so slicing never modifies the original.

**Common mistakes:**
- Off-by-one errors with stop index (it is exclusive).
- Assuming slicing modifies the original string.

### 2.4 String Repetition

**Formal definition:** The `*` operator on strings creates a new string by repeating the original a specified number of times.

```python
"abc" * 3    # "abcabcabc"
"-" * 40     # "----------------------------------------"
```

### 2.5 Escape Characters

**Formal definition:** Escape sequences allow embedding special characters in strings using backslash notation.

```python
print("\"quoted\"")    # "quoted"
print("line1\nline2")  # Two lines
print("tab\there")     # Tab character
```

---

## 3. Task-Level Static Analysis

### Task: 2-print.py

- **Problem statement:** Print a specific string containing escaped quotes.
- **Design approach:** Direct `print()` call with escaped double quote.
- **Control flow:** Linear — single statement execution.
- **Edge-case coverage:** N/A — no input.
- **Time complexity:** O(1)
- **Space complexity:** O(1)
- **Real-world analogy:** Outputting a formatted log message with special characters.

### Task: 3-print_number.py

- **Problem statement:** Print an integer variable alongside text using f-string formatting.
- **Design approach:** Variable assignment followed by f-string interpolation.
- **Control flow:** Linear.
- **Edge-case coverage:** N/A — hardcoded value.
- **Time complexity:** O(1)
- **Space complexity:** O(1)
- **Real-world analogy:** Printing a configuration value alongside its label.

### Task: 4-print_float.py

- **Problem statement:** Print a float with exactly 2 decimal places.
- **Design approach:** F-string with `:.2f` format specification.
- **Control flow:** Linear.
- **Edge-case coverage:** N/A — hardcoded value.
- **Time complexity:** O(1)
- **Space complexity:** O(1)
- **Potential improvements:** Consider using `Decimal` for financial calculations where floating-point precision matters.
- **Real-world analogy:** Formatting currency amounts in an e-commerce system.

### Task: 5-print_string.py

- **Problem statement:** Repeat a string 3 times and extract its first 9 characters.
- **Design approach:** String repetition with `*` operator and slicing with `[:9]`.
- **Control flow:** Linear.
- **Edge-case coverage:** N/A — hardcoded value.
- **Time complexity:** O(n) where n is string length × repetitions.
- **Space complexity:** O(n) for the repeated string.
- **Potential improvements:** Variable named `str` shadows the built-in type. Rename to `text` or `word`.
- **Real-world analogy:** Generating repeated patterns for output formatting (e.g., progress bars, separators).

### Task: 6-concat.py

- **Problem statement:** Concatenate two strings with a space and print a welcome message.
- **Design approach:** String concatenation with `+` operator, then f-string for final output.
- **Control flow:** Linear.
- **Time complexity:** O(n + m) where n, m are string lengths.
- **Space complexity:** O(n + m) for the concatenated string.
- **Real-world analogy:** Building full names from first/last name fields in a user profile.

### Task: 7-edges.py

- **Problem statement:** Extract first 3, last 2, and middle characters from a string.
- **Design approach:** Three slice operations: `[:3]`, `[-2:]`, `[1:-1]`.
- **Control flow:** Linear.
- **Time complexity:** O(n) for each slice (creating new string objects).
- **Space complexity:** O(n) for the sliced strings.
- **Real-world analogy:** Parsing structured strings (e.g., extracting area codes from phone numbers).

### Task: 8-concat_edges.py

- **Problem statement:** Extract and concatenate specific substrings from a long string.
- **Design approach:** Hard-coded index slicing with concatenation.
- **Control flow:** Linear.
- **Potential improvements:** Replace magic numbers with named constants or computed indices using `str.find()`.
- **Real-world analogy:** Extracting fields from fixed-width text records.

### Task: 9-easter_egg.py

- **Problem statement:** Print "The Zen of Python" by Tim Peters.
- **Design approach:** `import this` — a built-in Easter egg module.
- **Control flow:** Module import triggers side effect (printing).
- **Real-world analogy:** Understanding that Python has a philosophy — PEP 20 guides idiomatic Python design.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Encapsulation | ❌ | N/A — no classes |
| Abstraction | ❌ | N/A — no functions |
| Defensive Programming | ❌ | No input validation (all values hardcoded) |

This module is purely procedural — it establishes the "Hello, World" foundation without introducing any design patterns.

---

## 5. Built-ins & Keywords Deep Dive

### `print()`

```python
print("Hello")              # Basic output
print("a", "b", sep="-")   # Custom separator: "a-b"
print("no newline", end="") # Suppress newline
```

The `print()` function is the primary output mechanism. It accepts `*args` (variadic positional arguments), allowing multiple values to be printed in a single call.

### F-String Formatting

```python
x = 42
f"{x}"        # "42"       — basic interpolation
f"{x:05d}"    # "00042"    — zero-padded width 5
f"{x:>10}"    # "        42" — right-aligned width 10
f"{3.14:.1f}" # "3.1"      — 1 decimal place
```

### String Slicing

```python
s = "Python"
s[0]       # "P"     — first character
s[-1]      # "n"     — last character
s[2:4]     # "th"    — characters at index 2 and 3
s[::-1]    # "nohtyP" — reversed string
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between `print(x)` and `return x` in a function?
2. Explain how f-strings differ from `str.format()` and `%` formatting in terms of performance and readability.
3. What does "strings are immutable" mean in Python? What are the implications for string manipulation?
4. How does Python's string interning work, and when might two string variables with the same content share the same memory address?
5. What is the Zen of Python, and how does `import this` work internally?

### Practical Coding Questions

1. Write a function that takes a float and returns it formatted as a currency string (e.g., `"$1,234.56"`).
2. Given a string, extract the first word and the last word using only slicing (no `split()`).
3. Write a one-liner that reverses a string using slicing.
4. Create a function that masks a credit card number, showing only the last 4 digits: `"**** **** **** 1234"`.
5. Write a function that centers a title within a 60-character-wide line using f-string formatting.

### Debugging Scenarios

1. A developer writes `f"{name} has {count} items"` but `name` is `None`. What happens? How should this be handled?
2. The code `str = "hello"` followed by `str(42)` crashes. Explain why and fix it.

### System Design Question

1. Design a logging system that formats log messages with timestamps, severity levels, and contextual data. How would f-strings and string formatting be used? What are the trade-offs between f-strings, `%` formatting, and `str.format()` in a high-throughput logging context?

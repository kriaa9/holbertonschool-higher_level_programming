# Python: if/else, loops, and functions

Beginner-friendly documentation for the Holberton project that practices
control flow, iteration, and function basics. Every script in this folder
is documented so you can explain the project without Google.

---

## Project Overview

- Practice core Python control flow: `if/elif/else`, `for`, `while`.
- Use arithmetic operators and formatting for readable output.
- Learn how functions work: parameters, `return`, and scope.
- Build intuition for iteration, conditions, and simple algorithms.

Why control flow matters: it decides which code runs, how often, and in
what order. Combined with functions, it lets you compose reusable logic.

Skills gained:
- Read and write conditional logic
- Iterate with loops and `range()`
- Format strings and numbers
- Define functions and return values
- Reason about variable scope and tracebacks

---

## Learning Objectives

### Indentation
Python uses indentation to define blocks. Misaligned indentation raises
`IndentationError`. Always indent consistently (PEP 8: 4 spaces).

### `if`, `elif`, `else`
Choose a path based on conditions. Only one branch runs:
```py
if cond_a:
		...
elif cond_b:
		...
else:
		...
```

### Comments
Explain intent or tricky logic. Use `#` for inline comments and docstrings
(`"""..."""`) for modules/functions.

### Variable assignment
Bind names to values: `x = 10`. Python is dynamically typed—types are
attached to values, not variables.

### Loops: `while` and `for`
- `for` iterates over sequences or ranges.
- `while` repeats while a condition is `True`.

### `break` and `continue`
- `break` exits the loop early.
- `continue` skips to the next iteration.

### `else` on loops
Runs when the loop completes naturally (no `break`).

### `pass`
Placeholder that does nothing. Useful for stubs.

### `range()`
Generates arithmetic progressions. Commonly `range(start, stop)` or
`range(start, stop, step)`. Stop is exclusive.

### Functions and calls
Define with `def name(params):` and call with `name(args)`. Use `return`
to send a result back to the caller.

### `return` behavior
- `return value` ends the function and yields `value`.
- No `return` means `None` is returned.

### Variable scope
- Local: inside a function.
- Global: module-level. Avoid modifying globals; pass values explicitly.

### Tracebacks
Error reports that show where and why code failed. Read the last lines for
the exception type and message.

### Arithmetic operators
`+`, `-`, `*`, `/` (float division), `//` (floor division), `%` (modulo),
`**` (power). Beware `%` on negatives in Python: `-12 % 10 == 8`.

---

## Tasks Explanation

### 0. Positive anything is better than negative nothing
- Goal: classify a random integer as positive, zero, or negative.
- Logic: `if number > 0`, `elif number == 0`, `else` negative.
- Concepts: `if/elif/else`, formatting.
- Keywords: `random.randint`, conditional branches.
- Example: `-3 is negative`.

### 1. The last digit
- Goal: print the last digit of a random number with a description.
- Logic: compute `last_digit`; adjust for negatives using the task rule.
- Concepts: modulo, string formatting, conditionals.
- Keywords: `%`, concatenation for long lines.
- Example: `Last digit of 98 is 8 and is greater than 5`.

### 2. The alphabet game
- Goal: print lowercase alphabet on one line.
- Logic: iterate ASCII codes 97..122, use `chr()`.
- Concepts: `for`, `range`, `chr`, `end=''`.
- Example: `abcdefghijklmnopqrstuvwxyz`.

### 3. Alphabet soup
- Goal: print alphabet excluding `e` and `q`.
- Logic: conditional skip for codes 101 and 113.
- Concepts: filtering in loops.

### 4. Hexadecimal printing
- Goal: print `i = 0xhex` for `i` in 0..98.
- Logic: format with `{:d}` and `{:x}`.
- Concepts: format specifiers.

### 5. 00...99
- Goal: print all numbers `00` to `99` separated by `, `.
- Logic: zero-pad with `{:02d}`; omit trailing comma for `99`.
- Concepts: formatting, conditional last element.

### 6. Combinations of two digits
- Goal: print pairs `ab` where `a < b` (no repeats or reversed pairs).
- Logic: nested loops; special case final pair `89` newline only.
- Concepts: nested loops, formatted output.

### 7. `islower`
- Goal: return `True` if `c` is lowercase.
- Logic: check `97 <= ord(c) <= 122`.
- Concepts: ASCII, `ord()`.

### 8. To uppercase
- Goal: print a string in uppercase followed by newline.
- Logic: if lowercase (`97..122`), convert via `chr(ord(c)-32)`.
- Concepts: iteration, ASCII math, formatting.

### 9. Last digit comparison
- Goal: print and return the last digit of `number`.
- Logic: `abs(number) % 10` for a predictable digit; print without newline.
- Concepts: modulo, `abs`, `return`.

### 10. `a + b`
- Goal: return sum of two integers.
- Logic: `a + b`.
- Concepts: function definition, return value.

### 11. `a ^ b`
- Goal: return `a ** b`.
- Logic: use exponentiation operator `**`. Supports negative exponents.
- Concepts: arithmetic operators, power.

### 12. Fizz Buzz
- Goal: print 1..100 separated by spaces with Fizz/Buzz/FizzBuzz rules.
- Logic: check `% 15` first, then `% 3`, then `% 5`; else print number.
- Concepts: modulo, ordering of conditions, printing with `end=' '`.

---

## Python Keywords & Concepts Reference

- `if`, `elif`, `else`: conditional branching; only one path runs.
- `for`, `while`: loops for iteration and repeated actions.
- `break`, `continue`, `pass`: exit loop, skip iteration, do nothing.
- `def`, `return`: define functions and return values.
- `range`: generate integer sequences for looping.
- `%` (modulo): remainder after division; note Python's behavior on
	negatives.
- Comparison operators: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- String formatting: `"{}".format(x)`, `{:02d}` for zero-padding, `{:x}`
	for hex.

---

## Resources

- More Control Flow Tools (Python docs): explains advanced flow features
	such as list comprehensions and `pass`.
- IndentationError: understand why Python enforces indentation and how to
	fix common mistakes.
- String formatters in Python 3: reference for `format()` and specifiers.
- Learn to Program 2: Looping: beginner-focused explanation of `for`/`while`.
- Pycodestyle Style Guide: rules used to validate code style (PEP 8).
- `python3 help()` and `man`: get built-in documentation and manual pages.

---

## How to Run

Each script is executable. Examples:

```bash
./0-positive_or_negative.py
./2-print_alphabet.py
python3 -c "from 12-fizzbuzz import fizzbuzz; fizzbuzz(); print()"
```

Use `pycodestyle` to check style:

```bash
pycodestyle .
```

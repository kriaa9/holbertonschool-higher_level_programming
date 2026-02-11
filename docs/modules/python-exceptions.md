# Module: python-exceptions

## 1. Executive Summary

This module teaches **exception handling** — the mechanism by which Python programs detect, report, and recover from runtime errors. Students learn `try`/`except`/`finally` blocks, multiple exception types, exception propagation, and explicit `raise` statements. These patterns are critical for building resilient backend systems that gracefully handle invalid input, network failures, and resource constraints.

---

## 2. Deep Concept Breakdown

### 2.1 The Exception Model

**Formal definition:** An exception is an event that disrupts normal program flow. When an exception is raised, Python unwinds the call stack searching for a matching `except` handler.

```python
try:
    risky_operation()
except SpecificError as e:
    handle_error(e)
except (TypeError, ValueError):
    handle_type_or_value_error()
except Exception as e:
    handle_any_exception(e)
else:
    runs_only_if_no_exception()
finally:
    always_runs()
```

**Runtime behavior:**
1. Code in `try` block executes normally.
2. If an exception occurs, execution jumps to the first matching `except` clause.
3. `else` runs only if no exception occurred.
4. `finally` always runs — even if an exception is re-raised or `return` is called.

### 2.2 Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── TypeError
    ├── ValueError
    ├── IndexError
    ├── KeyError
    ├── ZeroDivisionError
    ├── FileNotFoundError
    ├── NameError
    └── ... (many more)
```

**Best practice:** Catch specific exceptions, not bare `except:` or `except Exception:`. Catching too broadly masks bugs.

### 2.3 The `raise` Statement

```python
raise TypeError("size must be an integer")   # Raise with message
raise ValueError                              # Raise without message
raise                                         # Re-raise current exception
```

### 2.4 The `finally` Clause

**Formal definition:** The `finally` block guarantees execution regardless of whether an exception occurred, was caught, or was re-raised.

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print(f"Inside result: {result}")
    return result
```

**Production relevance:** `finally` is essential for resource cleanup — closing database connections, releasing file handles, unlocking mutexes.

### 2.5 Exception-Based Control Flow

Python uses exceptions for control flow more liberally than many languages (EAFP — "Easier to Ask Forgiveness than Permission"):

```python
# EAFP style (Pythonic)
try:
    value = my_dict[key]
except KeyError:
    value = default

# LBYL style (non-Pythonic)
if key in my_dict:
    value = my_dict[key]
else:
    value = default
```

---

## 3. Task-Level Static Analysis

### Task: 0-safe_print_list.py

- **Problem statement:** Print up to `x` elements from a list, catching `IndexError`.
- **Design approach:** `try`/`except IndexError` inside a loop, counting successful prints.
- **Control flow:** Loop with exception-based termination.
- **Edge-case coverage:** Handles `x > len(my_list)` via `IndexError` catch.
- **Time complexity:** O(min(x, n)) where n = list length.
- **Potential improvements:** Mutable default argument `my_list=[]`.
- **Real-world analogy:** Paginated data display — show up to N items, handling shorter result sets.

### Task: 1-safe_print_integer.py

- **Problem statement:** Print a value as integer if possible, return success boolean.
- **Design approach:** `try` format as `{:d}`, catch `ValueError` and `TypeError`.
- **Control flow:** Try-except with boolean return.
- **Edge-case coverage:** Handles strings, floats, None, lists — any non-integer type.
- **Time complexity:** O(1)
- **Real-world analogy:** Input validation — attempting to parse user input as a specific type.

### Task: 2-safe_print_list_integers.py

- **Problem statement:** Print only integers from a mixed-type list.
- **Design approach:** Format as integer, `continue` on `ValueError`/`TypeError`.
- **Control flow:** Loop with exception-based filtering using `continue`.
- **Time complexity:** O(n)
- **Potential improvements:** Mutable default argument `my_list=[]`.
- **Real-world analogy:** Data cleansing — extracting valid numeric values from mixed data.

### Task: 3-safe_print_division.py

- **Problem statement:** Divide two numbers safely, always printing the result.
- **Design approach:** `try`/`except ZeroDivisionError`/`finally` pattern.
- **Control flow:** Exception handling with guaranteed output via `finally`.
- **Edge-case coverage:** Division by zero returns `None`, still prints.
- **Time complexity:** O(1)
- **Real-world analogy:** Database transaction with guaranteed audit logging in `finally`.

### Task: 4-list_division.py

- **Problem statement:** Divide corresponding elements of two lists, handling all error types.
- **Design approach:** Multiple `except` clauses for `TypeError`, `ZeroDivisionError`, `IndexError`.
- **Control flow:** Loop with multi-exception handling and `finally` for appending results.
- **Edge-case coverage:** Type mismatch, division by zero, lists of different lengths.
- **Time complexity:** O(n) where n = `list_length` parameter.
- **Real-world analogy:** Batch processing with per-item error handling — failed items don't stop the batch.

### Task: 5-raise_exception.py

- **Problem statement:** Raise a `TypeError`.
- **Design approach:** Direct `raise TypeError`.
- **Time complexity:** O(1)
- **Real-world analogy:** Explicit validation failure in a constructor or API endpoint.

### Task: 6-raise_exception_msg.py

- **Problem statement:** Raise a `NameError` with a custom message.
- **Design approach:** `raise NameError(message)`.
- **Time complexity:** O(1)
- **Real-world analogy:** Custom error messages for API validation responses.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| EAFP (Ask Forgiveness) | ✅ | `0-safe_print_list.py` — catches IndexError rather than checking bounds |
| Resource Cleanup | ✅ | `3-safe_print_division.py` — `finally` guarantees output |
| Defensive Programming | ✅ | `4-list_division.py` — handles three distinct error types |
| Error Propagation | ✅ | `5-raise_exception.py`, `6-raise_exception_msg.py` — explicit `raise` |
| Graceful Degradation | ✅ | `1-safe_print_integer.py` — returns `False` instead of crashing |

---

## 5. Built-ins & Keywords Deep Dive

### `try` / `except` / `else` / `finally`

```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Error: {e}")     # "Error: invalid literal for int()..."
else:
    print("Success!")         # Only runs if no exception
finally:
    print("Cleanup")          # Always runs
```

### `raise`

```python
raise ValueError("invalid input")          # Raise with message
raise TypeError                             # Raise without message

try:
    int("abc")
except ValueError:
    raise   # Re-raise the caught exception (preserves traceback)
```

### Exception chaining

```python
try:
    int("abc")
except ValueError as original:
    raise RuntimeError("conversion failed") from original
```

### Built-in Exception Types Used

| Exception | When Raised | Example Trigger |
|---|---|---|
| `TypeError` | Wrong type passed | `"hello" + 5` |
| `ValueError` | Right type, wrong value | `int("abc")` |
| `IndexError` | Index out of range | `[1,2,3][5]` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `NameError` | Undefined variable | `print(undefined_var)` |
| `KeyError` | Missing dictionary key | `{}["missing"]` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between `except Exception` and bare `except:`?
2. Explain the execution order of `try`/`except`/`else`/`finally`. When does `else` run?
3. What is EAFP vs LBYL? Which does Python prefer and why?
4. What is exception chaining (`raise ... from ...`)? When would you use it?
5. Why should you avoid catching generic `Exception` in production code?

### Practical Coding Questions

1. Write a function that safely converts a string to an integer, returning a default value on failure.
2. Implement a retry decorator that catches specified exceptions and retries up to N times with exponential backoff.
3. Write a function that reads a JSON file and returns its contents, handling `FileNotFoundError`, `json.JSONDecodeError`, and `PermissionError` separately.
4. Create a custom exception class `ValidationError` with a `field` attribute and a descriptive message.
5. Write a context manager that suppresses specified exception types (similar to `contextlib.suppress`).

### Debugging Scenarios

1. A developer catches `Exception` in a loop but notices the loop never terminates. The actual issue is a `KeyboardInterrupt`. Explain why it isn't caught and how to handle it.
2. A function with `finally: return result` always returns `None` even when the try block succeeds. Explain the behavior.

### System Design Question

1. Design an error handling strategy for a REST API that: (a) returns appropriate HTTP status codes for different error types, (b) logs errors with context, (c) doesn't expose internal details to clients, and (d) supports error aggregation for monitoring. What exception hierarchy would you define?

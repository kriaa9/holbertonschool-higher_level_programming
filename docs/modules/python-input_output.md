# Module: python-input_output

## 1. Executive Summary

This module teaches **file I/O operations** and **JSON serialization** — the skills needed to persist data beyond program execution. Students learn to read, write, and append files using context managers (`with` statement), convert Python objects to JSON strings and back, save/load objects to/from JSON files, and design self-serializing classes (the `Student` class). Advanced tasks include Pascal's triangle generation, log parsing from stdin, and file content manipulation. These skills directly support backend tasks like configuration management, data import/export, and API response formatting.

---

## 2. Deep Concept Breakdown

### 2.1 File Operations

**Formal definition:** File I/O in Python uses the `open()` built-in with context managers to ensure proper resource cleanup.

```python
# Reading
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Writing (overwrites)
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")

# Appending
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line")
```

**File modes:**
| Mode | Description |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write (truncates existing content) |
| `"a"` | Append |
| `"x"` | Exclusive creation (fails if file exists) |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) |

### 2.2 The `with` Statement (Context Managers)

**Formal definition:** The `with` statement ensures that resources are properly acquired and released, even if exceptions occur.

```python
with open("file.txt") as f:
    data = f.read()
# f is automatically closed here, even if an exception occurred
```

**Behind the scenes:** The `with` statement calls `__enter__()` on entry and `__exit__()` on exit. `__exit__()` is guaranteed to run.

### 2.3 JSON Serialization

**Formal definition:** JSON (JavaScript Object Notation) is a text-based data interchange format. Python's `json` module provides serialization (`dumps`/`dump`) and deserialization (`loads`/`load`).

```python
import json

# Python object → JSON string
json.dumps({"name": "Alice", "age": 30})    # '{"name": "Alice", "age": 30}'

# JSON string → Python object
json.loads('{"name": "Alice", "age": 30}')  # {'name': 'Alice', 'age': 30}

# Python object → JSON file
with open("data.json", "w") as f:
    json.dump({"key": "value"}, f)

# JSON file → Python object
with open("data.json", "r") as f:
    data = json.load(f)
```

**Type mapping:**

| Python | JSON |
|---|---|
| `dict` | object |
| `list` | array |
| `str` | string |
| `int`, `float` | number |
| `True`/`False` | true/false |
| `None` | null |

**Limitation:** JSON cannot serialize sets, tuples (become arrays), datetime objects, or custom class instances without custom encoders.

### 2.4 Object Serialization Pattern

The `Student` class demonstrates the complete serialization lifecycle:

```python
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
```

This pattern is the foundation for ORM-style object persistence.

---

## 3. Task-Level Static Analysis

### Task: 0-read_file.py

- **Problem statement:** Read and print a UTF-8 text file.
- **Design approach:** Context manager with `f.read()`.
- **OOP principles:** None — utility function.
- **Time complexity:** O(n) where n = file size.
- **Real-world analogy:** Loading a configuration file at application startup.

### Task: 1-write_file.py

- **Problem statement:** Write a string to a file, return characters written.
- **Design approach:** Context manager with `f.write()`, `mode="w"`.
- **Edge-case coverage:** Creates file if it doesn't exist; overwrites if it does.
- **Time complexity:** O(n) where n = string length.
- **Real-world analogy:** Saving user preferences or generated reports.

### Task: 2-append_write.py

- **Problem statement:** Append text to a file, return characters appended.
- **Design approach:** Context manager with `mode="a"`.
- **Time complexity:** O(n) where n = text length.
- **Real-world analogy:** Appending log entries to a log file.

### Task: 3-to_json_string.py

- **Problem statement:** Convert a Python object to a JSON string.
- **Design approach:** `return json.dumps(my_obj)`.
- **Time complexity:** O(n) where n = object complexity.
- **Real-world analogy:** Formatting API response bodies.

### Task: 4-from_json_string.py

- **Problem statement:** Parse a JSON string to a Python object.
- **Design approach:** `return json.loads(my_str)`.
- **Time complexity:** O(n) where n = string length.
- **Real-world analogy:** Parsing API request bodies.

### Task: 5-save_to_json_file.py

- **Problem statement:** Save a Python object to a JSON file.
- **Design approach:** Context manager with `json.dump()`.
- **Real-world analogy:** Saving application state to disk.

### Task: 6-load_from_json_file.py

- **Problem statement:** Load a Python object from a JSON file.
- **Design approach:** Context manager with `json.load()`.
- **Real-world analogy:** Loading saved application state.

### Task: 7-add_item.py

- **Problem statement:** CLI tool that appends arguments to a JSON list file.
- **Design approach:** Load existing list (or create empty), extend with `sys.argv[1:]`, save.
- **Control flow:** Try loading existing file → catch error → default to empty list → extend → save.
- **Edge-case coverage:** Handles missing file on first run.
- **Real-world analogy:** CLI bookmark manager or task list tool.

### Task: 8-class_to_json.py

- **Problem statement:** Convert a class instance to a dictionary.
- **Design approach:** `return obj.__dict__`.
- **OOP principles:** Introspection — `__dict__` contains all instance attributes.
- **Real-world analogy:** Django's `model_to_dict()` or DRF serializer `to_representation()`.

### Task: 9-student.py

- **Problem statement:** Student class with `to_json()` method.
- **Design approach:** Returns `self.__dict__` for full serialization.
- **OOP principles:** Self-serialization — object knows how to convert itself.
- **Real-world analogy:** Django REST Framework serializer `to_representation()`.

### Task: 10-student.py

- **Problem statement:** Enhanced `to_json()` with attribute filtering.
- **Design approach:** If `attrs` is a list of strings, filter `__dict__` to include only those keys.
- **OOP principles:** Selective serialization — API field selection (GraphQL-like).
- **Real-world analogy:** API response with `fields` query parameter to select returned attributes.

### Task: 11-student.py

- **Problem statement:** Add `reload_from_json()` for deserialization.
- **Design approach:** Iterates over dict items, uses `setattr()` to update instance.
- **OOP principles:** Deserialization — reconstruct object state from dict.
- **Real-world analogy:** ORM `refresh_from_db()` or API `PATCH` request handling.

### Task: 12-pascal_triangle.py

- **Problem statement:** Generate Pascal's triangle as a list of lists.
- **Design approach:** Iterative construction — each row's element is sum of two elements above.
- **Time complexity:** O(n²) where n = number of rows.
- **Space complexity:** O(n²) for the entire triangle.
- **Real-world analogy:** Combinatorics calculations, binomial coefficients.

### Task: 100-append_after.py

- **Problem statement:** Insert text after lines containing a search string.
- **Design approach:** Read all lines, iterate, insert after matches, write back.
- **Time complexity:** O(n) where n = number of lines.
- **Real-world analogy:** Configuration file patching — inserting directives after specific markers.

### Task: 101-stats.py

- **Problem statement:** Parse HTTP log lines from stdin, aggregate file sizes and status codes.
- **Design approach:** Line-by-line stdin parsing with periodic summary output every 10 lines.
- **Edge-case coverage:** Handles `KeyboardInterrupt` gracefully.
- **Real-world analogy:** Real-time log analysis pipeline (similar to `awk`-based monitoring).

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Encapsulation | ✅ | `Student` class — controlled serialization |
| Self-Serialization | ✅ | `9-student.py` through `11-student.py` — `to_json()`/`reload_from_json()` |
| Context Manager | ✅ | All file operations use `with` statement |
| Defensive Programming | ✅ | `7-add_item.py` — handles missing file |
| Pipeline Pattern | ✅ | `101-stats.py` — stdin → parse → aggregate → output |

---

## 5. Built-ins & Keywords Deep Dive

### `with` statement

```python
with open("file.txt", "r") as f:
    data = f.read()
# f.__exit__() called automatically — file is closed
```

### `json.dumps()` / `json.loads()`

```python
json.dumps({"a": 1}, indent=4)      # Pretty-printed JSON string
json.dumps({"a": 1}, sort_keys=True) # Sorted keys
json.loads('{"a": 1}')               # Python dict
```

### `json.dump()` / `json.load()`

```python
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)     # Write to file

with open("data.json", "r") as f:
    data = json.load(f)              # Read from file
```

### `setattr()` / `getattr()`

```python
setattr(obj, "name", "Alice")    # obj.name = "Alice"
getattr(obj, "name")             # "Alice"
getattr(obj, "missing", None)    # None (with default)
```

### `__dict__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.__dict__    # {'x': 1, 'y': 2}
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between `json.dump()` and `json.dumps()`? When would you use each?
2. Explain context managers and the `with` statement. What methods must an object implement to be used with `with`?
3. What Python types cannot be serialized to JSON by default? How would you handle them?
4. What is the difference between reading a file with `f.read()`, `f.readline()`, and `f.readlines()`?
5. Explain the difference between text mode and binary mode when opening files.

### Practical Coding Questions

1. Write a function that merges two JSON files into one, handling key conflicts by keeping the value from the second file.
2. Implement a `JSONDatabase` class that stores records in a JSON file with `insert()`, `find()`, `update()`, and `delete()` methods.
3. Write a custom JSON encoder that handles `datetime`, `set`, and `Decimal` types.
4. Create a function that compares two JSON files and returns their differences.
5. Implement a log rotation system that creates new log files when the current one exceeds a size limit.

### Debugging Scenarios

1. A developer opens a file with `open("data.txt")` (without `with`) and the program crashes midway. The file is never closed, causing resource leaks. Explain the fix.
2. `json.dumps(data)` raises `TypeError: Object of type set is not JSON serializable`. The developer has `{"tags": {"python", "java"}}`. How should this be handled?

### System Design Question

1. Design a file-based caching system for a web application. Requirements: (a) cache API responses as JSON files, (b) implement TTL-based expiration, (c) handle concurrent reads/writes safely, (d) support cache invalidation by key pattern. What file organization, serialization format, and locking strategy would you use?

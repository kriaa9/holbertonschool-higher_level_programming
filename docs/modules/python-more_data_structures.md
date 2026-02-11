# Module: python-more_data_structures

## 1. Executive Summary

This module extends data structure mastery to **dictionaries**, **sets**, **list/dict comprehensions**, and **functional programming tools** (`lambda`, `map()`). Students learn to model key-value relationships, perform set operations, transform data concisely with comprehensions, and solve complex algorithmic problems (Roman numeral conversion). These skills directly support backend tasks like caching, data transformation pipelines, and configuration management.

---

## 2. Deep Concept Breakdown

### 2.1 Dictionaries

**Formal definition:** A dictionary is a mutable, unordered (insertion-ordered in Python 3.7+) mapping of unique keys to values. Implemented as a hash table in CPython.

```python
d = {"name": "Alice", "age": 30}
d["name"]                  # "Alice" — O(1) average lookup
d["email"] = "a@b.com"    # Add new key-value pair
del d["age"]               # Remove key
d.get("missing", "default") # Safe access with default
```

**Performance notes:**
- Lookup: O(1) average, O(n) worst case (hash collisions)
- Insert/Delete: O(1) average
- Memory: Higher overhead than lists due to hash table structure
- Keys must be hashable (immutable types: str, int, tuple)

### 2.2 Sets

**Formal definition:** A set is an unordered collection of unique, hashable elements. Supports mathematical set operations.

```python
s = {1, 2, 3, 3}           # {1, 2, 3} — duplicates removed
s.add(4)                    # {1, 2, 3, 4}
{1,2,3} & {2,3,4}         # {2, 3}    — intersection
{1,2,3} | {2,3,4}         # {1,2,3,4} — union
{1,2,3} ^ {2,3,4}         # {1, 4}    — symmetric difference
{1,2,3} - {2,3,4}         # {1}       — difference
```

### 2.3 Comprehensions

**List comprehension:**
```python
[x**2 for x in range(5)]                    # [0, 1, 4, 9, 16]
[x for x in range(10) if x % 2 == 0]        # [0, 2, 4, 6, 8]
```

**Dict comprehension:**
```python
{k: v*2 for k, v in {"a": 1, "b": 2}.items()}  # {"a": 2, "b": 4}
```

**Nested comprehension:**
```python
[[col**2 for col in row] for row in matrix]  # Square each element
```

### 2.4 Lambda Functions

**Formal definition:** A `lambda` is an anonymous, single-expression function.

```python
square = lambda x: x**2     # Equivalent to def square(x): return x**2
add = lambda a, b: a + b    # Multi-parameter lambda
```

**Production best practice:** Lambdas are best used inline with `map()`, `filter()`, `sorted()`. For anything complex, define a named function.

### 2.5 `map()` and `filter()`

```python
list(map(lambda x: x*2, [1, 2, 3]))       # [2, 4, 6]
list(filter(lambda x: x > 2, [1, 2, 3]))  # [3]
```

**Modern Python preference:** List comprehensions are generally preferred over `map()`/`filter()` for readability.

---

## 3. Task-Level Static Analysis

### Task: 0-square_matrix_simple.py

- **Problem statement:** Square all elements in a 2D matrix.
- **Design approach:** Nested list comprehension.
- **Time complexity:** O(m × n)
- **Space complexity:** O(m × n) — creates new matrix.
- **Potential improvements:** Default parameter `matrix=[]` is a mutable default anti-pattern.
- **Real-world analogy:** Applying a transformation to every cell in a spreadsheet.

### Task: 1-search_replace.py

- **Problem statement:** Replace all occurrences of a value in a list.
- **Design approach:** Conditional list comprehension.
- **Time complexity:** O(n)
- **Space complexity:** O(n) — creates new list.
- **Real-world analogy:** Find-and-replace in a text editor or database update query.

### Task: 2-uniq_add.py

- **Problem statement:** Sum only the unique elements of a list.
- **Design approach:** Convert to `set()` for deduplication, then `sum()`.
- **Time complexity:** O(n) for set creation + O(k) for sum where k = unique count.
- **Real-world analogy:** Counting unique visitors to a website.

### Task: 3-common_elements.py

- **Problem statement:** Return elements common to two sets.
- **Design approach:** Set intersection with `&` operator.
- **Time complexity:** O(min(len(a), len(b)))
- **Real-world analogy:** Finding shared tags between two items, mutual friends.

### Task: 4-only_diff_elements.py

- **Problem statement:** Return elements in either set but not both.
- **Design approach:** Set symmetric difference with `^` operator.
- **Time complexity:** O(len(a) + len(b))
- **Real-world analogy:** Detecting changed files between two directory snapshots.

### Task: 5-number_keys.py

- **Problem statement:** Count the number of keys in a dictionary.
- **Design approach:** `len(a_dictionary)`.
- **Time complexity:** O(1)
- **Real-world analogy:** Counting fields in a JSON object.

### Task: 6-print_sorted_dictionary.py

- **Problem statement:** Print dictionary entries sorted by key.
- **Design approach:** `sorted()` on dictionary keys, then iterate.
- **Time complexity:** O(n log n) for sorting.
- **Real-world analogy:** Displaying configuration settings in alphabetical order.

### Task: 7-update_dictionary.py

- **Problem statement:** Add or update a key-value pair.
- **Design approach:** Direct assignment `d[key] = value`.
- **Time complexity:** O(1)
- **Real-world analogy:** Updating a cache entry or user profile field.

### Task: 8-simple_delete.py

- **Problem statement:** Delete a key from a dictionary if it exists.
- **Design approach:** Check existence with `in` before `del`.
- **Time complexity:** O(1)
- **Real-world analogy:** Removing a session variable on logout.

### Task: 9-multiply_by_2.py

- **Problem statement:** Create a new dictionary with all values doubled.
- **Design approach:** Dictionary comprehension.
- **Time complexity:** O(n)
- **Real-world analogy:** Applying a scaling factor to all metrics in a report.

### Task: 10-best_score.py

- **Problem statement:** Return the key with the highest value.
- **Design approach:** Linear scan tracking max value and key.
- **Edge-case coverage:** Returns `None` for empty dictionary.
- **Time complexity:** O(n)
- **Potential improvements:** Could use `max(d, key=d.get)` for conciseness.
- **Real-world analogy:** Finding the top-scoring student or best-selling product.

### Task: 11-multiply_list_map.py

- **Problem statement:** Multiply all list elements using `map()` and `lambda`.
- **Design approach:** `list(map(lambda x: x * number, my_list))`.
- **Time complexity:** O(n)
- **Potential improvements:** Default parameter `my_list=[]` is a mutable default.
- **Real-world analogy:** Applying a discount percentage to all product prices.

### Task: 12-roman_to_int.py

- **Problem statement:** Convert a Roman numeral string to an integer.
- **Design approach:** Dictionary lookup with reverse iteration for subtractive notation.
- **Edge-case coverage:** Handles `None` and non-string input.
- **Time complexity:** O(n) where n = string length.
- **Space complexity:** O(1) — fixed-size lookup dictionary.
- **Real-world analogy:** Parsing structured text formats — similar to date parsing or version string interpretation.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Functional Programming | ✅ | `11-multiply_list_map.py` — `map()` with `lambda` |
| Defensive Programming | ✅ | `12-roman_to_int.py` — type checking for input |
| Data Transformation | ✅ | `0-square_matrix_simple.py`, `9-multiply_by_2.py` — comprehensions |
| Set Theory | ✅ | `3-common_elements.py`, `4-only_diff_elements.py` |

---

## 5. Built-ins & Keywords Deep Dive

### `sorted()`

```python
sorted([3, 1, 2])                    # [1, 2, 3]
sorted("hello")                       # ['e', 'h', 'l', 'l', 'o']
sorted(d.items(), key=lambda x: x[1]) # Sort dict by value
```

### `lambda`

```python
f = lambda x, y: x + y
f(3, 4)    # 7

# Common use: sorting key
sorted(students, key=lambda s: s["gpa"])
```

### `map()`

```python
list(map(str, [1, 2, 3]))              # ["1", "2", "3"]
list(map(lambda x: x.upper(), words))  # Uppercase all words
```

### `sum()`

```python
sum([1, 2, 3])         # 6
sum([1, 2, 3], 10)     # 16 — with initial value
```

### `set` operations

```python
a = {1, 2, 3}
b = {3, 4, 5}
a & b       # {3}        — intersection
a | b       # {1,2,3,4,5} — union
a - b       # {1, 2}     — difference
a ^ b       # {1,2,4,5}  — symmetric difference
a <= b      # False      — subset check
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between a dictionary and a list? When would you choose one over the other?
2. Explain how Python's dictionary is implemented internally (hash table). What happens during a hash collision?
3. What makes an object "hashable"? Why can't lists be dictionary keys?
4. What is the difference between `dict.get(key)` and `dict[key]`?
5. Explain the difference between `map()` with `lambda` and a list comprehension. Which is preferred in modern Python?

### Practical Coding Questions

1. Write a function that counts the frequency of each word in a string and returns a dictionary.
2. Implement a function that merges two dictionaries, summing values for shared keys.
3. Write a function that inverts a dictionary (keys become values, values become keys). Handle duplicate values.
4. Implement `groupby` — given a list of dicts, group them by a specified key.
5. Write a function that finds the first non-repeating character in a string using a dictionary.

### Debugging Scenarios

1. A developer uses `d = dict.fromkeys(["a", "b", "c"], [])` and appends to `d["a"]`. All values change. Why?
2. A set comprehension `{x for x in [[1], [2], [3]]}` raises `TypeError`. Explain why.

### System Design Question

1. Design an in-memory caching system (like a simplified Redis) that supports `get`, `set`, `delete`, and `keys` operations with O(1) average time complexity. What data structure would you use? How would you handle cache eviction?

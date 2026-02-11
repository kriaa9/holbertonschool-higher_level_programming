# Module: python-data_structures

## 1. Executive Summary

This module introduces Python's core sequential data structures: **lists** and **tuples**. Students learn to create, access, modify, slice, and iterate over these structures. Key operations include list manipulation (append, replace, delete), tuple packing/unpacking, matrix handling, and finding extremes. These skills are foundational for data processing, algorithm design, and understanding how objects store collections of data internally.

---

## 2. Deep Concept Breakdown

### 2.1 Lists

**Formal definition:** A list is a mutable, ordered sequence of elements. Lists are implemented as dynamic arrays in CPython.

```python
my_list = [1, 2, 3]        # Creation
my_list[0]                   # Access: 1
my_list.append(4)            # Mutation: [1, 2, 3, 4]
my_list[1] = 20              # Replacement: [1, 20, 3, 4]
del my_list[0]               # Deletion: [20, 3, 4]
```

**Memory model:** Lists store references (pointers) to objects, not the objects themselves. This means a list of integers holds pointers to int objects. Dynamic resizing uses amortized O(1) appends by over-allocating memory.

**Performance notes:**
- Index access: O(1)
- Append: O(1) amortized
- Insert at beginning: O(n)
- Search (linear): O(n)
- Slice: O(k) where k is slice length

### 2.2 Tuples

**Formal definition:** A tuple is an immutable, ordered sequence. Once created, its elements cannot be changed.

```python
my_tuple = (1, 2, 3)        # Creation
single = (42,)               # Single-element tuple (note the comma)
a, b = (1, 2)               # Unpacking
```

**Memory model:** Tuples are more memory-efficient than lists because CPython caches small tuples and their fixed size allows optimized allocation.

**When to use tuples vs lists:**
- Tuples: fixed-structure data (coordinates, RGB colors, database rows), dictionary keys, function return values.
- Lists: dynamic collections that grow/shrink.

### 2.3 List Slicing

```python
my_list = [0, 1, 2, 3, 4, 5]
my_list[2:4]      # [2, 3]       — elements at index 2, 3
my_list[:3]       # [0, 1, 2]    — first 3
my_list[3:]       # [3, 4, 5]    — from index 3 onward
my_list[::2]      # [0, 2, 4]    — every other element
my_list[::-1]     # [5, 4, 3, 2, 1, 0] — reversed
```

**Important:** Slicing a list creates a **shallow copy** — the new list holds references to the same objects.

### 2.4 The `del` Statement

```python
del my_list[2]       # Remove element at index 2
del my_list[1:3]     # Remove slice
del my_list          # Delete the variable itself
```

### 2.5 Nested Lists (Matrices)

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2]    # 6 — row 1, column 2
```

---

## 3. Task-Level Static Analysis

### Task: 0-print_list_integer.py

- **Problem statement:** Print each integer in a list, one per line.
- **Design approach:** Loop with `.format()` for integer-specific output.
- **Time complexity:** O(n)
- **Space complexity:** O(1)
- **Real-world analogy:** Iterating over query results to display each record.

### Task: 1-element_at.py

- **Problem statement:** Return element at a given index, or `None` if out of bounds.
- **Design approach:** Boundary check before index access.
- **Edge-case coverage:** Handles negative indices and indices >= length.
- **Time complexity:** O(1)
- **Real-world analogy:** Safe array access in API response parsing.

### Task: 2-replace_in_list.py

- **Problem statement:** Replace element at given index in a list.
- **Design approach:** Boundary check followed by in-place modification.
- **Edge-case coverage:** Returns unmodified list for out-of-bounds indices.
- **Time complexity:** O(1) for the replacement.
- **Real-world analogy:** Updating a record in an in-memory collection.

### Task: 3-print_reversed_list_integer.py

- **Problem statement:** Print list elements in reverse order.
- **Design approach:** `reversed()` built-in iterator.
- **Time complexity:** O(n)
- **Space complexity:** O(1) — `reversed()` returns an iterator, not a new list.
- **Real-world analogy:** Displaying recent activity in reverse chronological order.

### Task: 4-new_in_list.py

- **Problem statement:** Replace element in a copy of the list (original unchanged).
- **Design approach:** `my_list[:]` creates a shallow copy before modification.
- **Edge-case coverage:** Returns copy for out-of-bounds indices.
- **Time complexity:** O(n) for the copy.
- **Real-world analogy:** Immutable update pattern — create a new version rather than mutating shared state.

### Task: 5-no_c.py

- **Problem statement:** Remove all 'c' and 'C' characters from a string.
- **Design approach:** Character-by-character iteration with string concatenation.
- **Time complexity:** O(n²) worst case due to string concatenation in a loop.
- **Potential improvements:** Use `''.join(c for c in s if c not in 'cC')` or `s.replace('c','').replace('C','')`.
- **Real-world analogy:** Input sanitization — removing prohibited characters from user input.

### Task: 6-print_matrix_integer.py

- **Problem statement:** Print a 2D matrix with proper formatting.
- **Design approach:** Nested loops with conditional spacing (no trailing space).
- **Time complexity:** O(m × n) where m = rows, n = columns.
- **Real-world analogy:** Rendering tabular data in a CLI application.

### Task: 7-add_tuple.py

- **Problem statement:** Add two tuples element-wise (first 2 elements).
- **Design approach:** Pad short tuples with `(0, 0)` before indexing.
- **Edge-case coverage:** Handles tuples shorter than 2 elements, longer tuples (only first 2 used).
- **Time complexity:** O(1)
- **Real-world analogy:** Vector addition — combining coordinates or offsets.

### Task: 8-multiple_returns.py

- **Problem statement:** Return tuple of (length, first character) or (0, None) for empty string.
- **Design approach:** Conditional check for empty string.
- **Edge-case coverage:** Empty string returns `(0, None)`.
- **Time complexity:** O(1)
- **Real-world analogy:** Functions that return multiple related values (e.g., HTTP response with status and body).

### Task: 9-max_integer.py

- **Problem statement:** Find the maximum integer in a list without using `max()`.
- **Design approach:** Linear scan with comparison.
- **Edge-case coverage:** Returns `None` for empty list.
- **Time complexity:** O(n)
- **Potential improvements:** Could use built-in `max()`, but constraint-based learning prohibits it.
- **Real-world analogy:** Finding the highest score, largest file, or most expensive item.

### Task: 10-divisible_by_2.py

- **Problem statement:** Return boolean list indicating even/odd for each element.
- **Design approach:** Loop with modulo check, building result list.
- **Time complexity:** O(n)
- **Potential improvements:** Could use list comprehension: `[x % 2 == 0 for x in my_list]`.
- **Real-world analogy:** Batch classification — tagging items based on a property.

### Task: 11-delete_at.py

- **Problem statement:** Delete element at given index (in-place).
- **Design approach:** Boundary check followed by `del` statement.
- **Time complexity:** O(n) — deletion requires shifting subsequent elements.
- **Real-world analogy:** Removing a record from an ordered collection.

### Task: 12-switch.py

- **Problem statement:** Swap two variables.
- **Design approach:** Pythonic tuple unpacking: `a, b = b, a`.
- **Time complexity:** O(1)
- **Real-world analogy:** Swapping database records during sorting operations.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Defensive Programming | ✅ | `1-element_at.py`, `2-replace_in_list.py` — boundary checks |
| Immutable Update | ✅ | `4-new_in_list.py` — copies before modifying |
| In-Place Mutation | ✅ | `2-replace_in_list.py`, `11-delete_at.py` |
| Constraint-Based | ✅ | `9-max_integer.py` — no `max()` allowed |

---

## 5. Built-ins & Keywords Deep Dive

### `len()`

```python
len([1, 2, 3])        # 3
len("hello")           # 5
len({"a": 1, "b": 2}) # 2
```

### `reversed()`

```python
list(reversed([1, 2, 3]))    # [3, 2, 1]
for item in reversed(range(5)):
    print(item)               # 4, 3, 2, 1, 0
```

Returns an iterator — memory-efficient, does not create a new list.

### `del`

```python
my_list = [1, 2, 3, 4]
del my_list[1]      # [1, 3, 4]
del my_list[0:2]    # [4]
```

### `sorted()` vs `.sort()`

```python
original = [3, 1, 2]
sorted(original)        # [1, 2, 3] — returns new list
original                # [3, 1, 2] — unchanged

original.sort()         # None — modifies in place
original                # [1, 2, 3]
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between a list and a tuple in Python? When should you use each?
2. Explain shallow copy vs deep copy. What does `my_list[:]` create?
3. How are Python lists implemented internally? What is their time complexity for common operations?
4. What happens when you slice beyond the bounds of a list (e.g., `[1,2,3][0:100]`)?
5. Why can tuples be used as dictionary keys but lists cannot?

### Practical Coding Questions

1. Write a function that rotates a list by k positions to the right.
2. Implement a function that flattens a 2D matrix into a 1D list.
3. Write a function that returns the second-largest element in a list without sorting.
4. Implement `zip()` manually using only lists and loops.
5. Write a function that removes duplicates from a list while preserving order.

### Debugging Scenarios

1. A developer writes `new_list = old_list` and modifies `new_list`. The original `old_list` also changes. Why? How to fix?
2. The code `t = (1); t[0]` raises `TypeError: 'int' object is not subscriptable`. What went wrong?

### System Design Question

1. Design an in-memory task queue that supports `enqueue`, `dequeue`, and `peek` operations. Would you use a list, a deque, or a custom structure? Discuss the trade-offs.

# Python3: Mutable, Immutable... everything is object

![Placeholder cover image](https://via.placeholder.com/1400x500.png?text=Python3+Mutable+vs+Immutable+Everything+Is+Object)

Published URL placeholders (replace after publishing):

- Medium: <https://medium.com/@your-username/python3-mutable-immutable-everything-is-object>
- LinkedIn: <https://www.linkedin.com/pulse/python3-mutable-immutable-everything-object-your-name>

## Introduction

When you start Python, you quickly learn variables, lists, strings, and functions.
What is easy to miss at first is this: Python variables do not store values directly.
They store references to objects.

That single idea explains many behaviors that look surprising at first:

- Why changing one list can change another variable.
- Why `==` and `is` can give different answers.
- Why some function calls modify your data and others do not.

This article walks through the core model behind Python objects, with practical examples you can run right away.

## `id` and `type`: identity and nature of objects

Two built-ins are essential when reasoning about objects:

- `type(obj)` tells you what kind of object it is.
- `id(obj)` gives the identity of the object (unique during its lifetime).

```python
x = 42
print(type(x))  # <class 'int'>
print(id(x))    # example: 140188418979344 (value varies)
```

If two names point to the same object, their `id` is the same.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True
print(a is b)          # True
```

## Mutable objects

A mutable object can be changed in place after creation.
Common mutable types include:

- `list`
- `dict`
- `set`

### Example: aliasing + mutation

```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)
print(l1)  # [1, 2, 3, 4]
print(l2)  # [1, 2, 3, 4]
```

Both names point to the same list, so in-place mutation is visible from both.

### `+` vs `+=` on lists

```python
a = [1, 2, 3]
first_id = id(a)

a = a + [4]       # creates a new list
print(id(a) == first_id)  # False

b = [1, 2, 3]
second_id = id(b)

b += [4]           # mutates in place for lists
print(id(b) == second_id)  # True
```

This difference is critical in debugging and API design.

## Immutable objects

An immutable object cannot be changed after creation.
Common immutable types include:

- `int`
- `float`
- `str`
- `tuple`

### Rebinding is not mutation

```python
n = 5
before = id(n)

n = n + 1  # creates a new int object
after = id(n)

print(before == after)  # False
```

The original integer is not modified. The name `n` is rebound to a new object.

### Tuples and subtle syntax

```python
print(type((1, 2)))  # <class 'tuple'>
print(type((1)))     # <class 'int'>
print(type((1,)))    # <class 'tuple'>
```

A single-element tuple needs a trailing comma.

## Why this matters

Understanding mutability and identity helps you:

- Avoid accidental side effects.
- Write safer function interfaces.
- Predict performance and memory behavior.
- Debug aliasing bugs faster.

If your function should not modify caller data, copy mutable inputs.

```python
def safe_add_item(items, value):
    copy = items[:]   # shallow copy
    copy.append(value)
    return copy
```

## How Python passes arguments to functions

Python uses pass-by-assignment (also described as pass-by-object-reference).
A function receives a reference to the same object.

### Mutation inside function affects caller (mutable object)

```python
def append_item(lst):
    lst.append(4)

data = [1, 2, 3]
append_item(data)
print(data)  # [1, 2, 3, 4]
```

### Rebinding inside function does not affect caller

```python
def rebind_list(lst):
    lst = [99, 100]

data = [1, 2, 3]
rebind_list(data)
print(data)  # [1, 2, 3]
```

`lst = [99, 100]` only changes the local name inside the function.

## Practical checklist

Use this quick checklist while coding:

- Need value comparison? Use `==`.
- Need identity comparison? Use `is`.
- Working with mutable inputs? Decide if in-place changes are intended.
- Need isolation? Create a copy (shallow or deep depending on nested data).

## Conclusion

Everything in Python is an object, and names are references.
Once this model clicks, many confusing behaviors become predictable:

- Aliasing explains shared updates.
- Immutability explains rebinding.
- `is` vs `==` explains identity vs value.
- Function argument behavior follows naturally from references.

Master these ideas early, and your Python code becomes clearer, safer, and easier to reason about.

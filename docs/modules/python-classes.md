# Module: python-classes

## 1. Executive Summary

This module marks the transition from procedural to **object-oriented programming**. Through a progressively complex `Square` class (7 iterations), students learn class definition, the `__init__` constructor, private attributes via name mangling, property decorators for controlled access, input validation, instance methods, and visual output. This module establishes the encapsulation principle that underlies all subsequent OOP modules.

---

## 2. Deep Concept Breakdown

### 2.1 Class Definition

**Formal definition:** A class is a blueprint for creating objects. It defines attributes (data) and methods (behavior) that its instances will have.

```python
class Square:
    """Represents a square."""
    pass
```

**Runtime behavior:** When Python encounters `class Square:`, it creates a class object in memory. This object serves as a factory for creating instances via `Square()`.

### 2.2 The `__init__` Constructor

**Formal definition:** `__init__` is a special method (dunder method) called automatically when an instance is created. It initializes instance attributes.

```python
class Square:
    def __init__(self, size=0):
        self.__size = size
```

**Memory model:** `self` is a reference to the newly created instance. `self.__size` creates an instance attribute bound to that specific object.

**Common mistakes:**
- Forgetting `self` as the first parameter.
- Confusing `__init__` with a constructor — technically, `__new__` creates the object; `__init__` initializes it.

### 2.3 Private Attributes (Name Mangling)

**Formal definition:** Prefixing an attribute with double underscores (`__name`) triggers Python's name mangling, which renames it to `_ClassName__name` to prevent accidental access from outside the class.

```python
class Square:
    def __init__(self, size):
        self.__size = size    # Stored as _Square__size

s = Square(5)
# s.__size         → AttributeError
# s._Square__size  → 5 (still accessible, but discouraged)
```

**Important:** Name mangling is a convention enforcement, not true access control. Python follows the "we're all consenting adults" philosophy.

### 2.4 Properties

**Formal definition:** Properties provide a Pythonic way to define getter/setter methods that look like regular attribute access.

```python
class Square:
    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```

**Runtime behavior:** `square.size` calls the getter; `square.size = 5` calls the setter. The attribute appears public but access is mediated.

**Production relevance:** Properties are used extensively in Django models, SQLAlchemy, and data classes to add validation, computed attributes, and lazy loading.

### 2.5 Input Validation in Constructors

The module establishes a validation pattern that recurs throughout the curriculum:

```python
if not isinstance(value, int):
    raise TypeError("size must be an integer")
if value < 0:
    raise ValueError("size must be >= 0")
```

This pattern ensures objects are always in a valid state — a key principle of encapsulation.

---

## 3. Task-Level Static Analysis

### Task: 0-square.py

- **Problem statement:** Define an empty `Square` class.
- **Design approach:** `class Square: pass` with docstring.
- **OOP principles:** Class definition — the simplest possible class.
- **Time complexity:** O(1) for instantiation.
- **Real-world analogy:** Defining a database table schema before adding columns.

### Task: 1-square.py

- **Problem statement:** Add a private `size` attribute to `Square`.
- **Design approach:** `__init__` with `self.__size = size`.
- **OOP principles:** Encapsulation — private attribute via name mangling.
- **Edge-case coverage:** No validation yet — accepts any value.
- **Real-world analogy:** Initial model definition with fields but no constraints.

### Task: 2-square.py

- **Problem statement:** Add type and value validation for `size`.
- **Design approach:** `isinstance()` check + non-negative check in `__init__`.
- **OOP principles:** Encapsulation — objects enforce their own invariants.
- **Edge-case coverage:** Rejects non-integers and negative values.
- **Time complexity:** O(1) for validation.
- **Real-world analogy:** Database column constraints (`NOT NULL`, `CHECK >= 0`).

### Task: 3-square.py

- **Problem statement:** Add an `area()` method.
- **Design approach:** `return self.__size * self.__size`.
- **OOP principles:** Instance methods — behavior tied to object state.
- **Time complexity:** O(1)
- **Real-world analogy:** Computed property on a domain model (e.g., `Order.total()`).

### Task: 4-square.py

- **Problem statement:** Add property getter and setter for `size`.
- **Design approach:** `@property` decorator for getter, `@size.setter` for setter with validation.
- **OOP principles:** Full encapsulation — external code uses `square.size` but validation is enforced.
- **Control flow:** Setter validates before assignment; raises on invalid input.
- **Real-world analogy:** Django model field with `validators` parameter.

### Task: 5-square.py

- **Problem statement:** Add `my_print()` method to visualize the square with `#`.
- **Design approach:** Loop printing `"#" * self.__size` for each row.
- **Edge-case coverage:** Size 0 prints empty line.
- **Time complexity:** O(n²) for printing n×n square.
- **Real-world analogy:** Rendering a UI component based on its dimensions.

### Task: 6-square.py

- **Problem statement:** Add `position` attribute for offsetting square output.
- **Design approach:** Tuple validation (must be tuple of 2 non-negative integers), horizontal offset with spaces, vertical offset with newlines.
- **OOP principles:** Multi-property class with cross-property coordination.
- **Edge-case coverage:** Position validation handles non-tuples, wrong-length tuples, negative values.
- **Potential improvements:** The error message reads `"position must be a tuple of 2 positive integers"` but the validation accepts 0 (i.e., non-negative integers). The message should say `"non-negative integers"` to accurately reflect the accepted range (0 and above).
- **Real-world analogy:** CSS positioning — `margin-left` and `margin-top` for an HTML element.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Encapsulation | ✅ | All files — private attributes with controlled access |
| Invariant Enforcement | ✅ | `2-square.py` onward — constructor and setter validation |
| Progressive Enhancement | ✅ | Each file adds one feature to the previous version |
| Information Hiding | ✅ | `__size`, `__position` — name-mangled attributes |
| Defensive Programming | ✅ | Type and value checks in constructors and setters |

---

## 5. Built-ins & Keywords Deep Dive

### `class` keyword

```python
class MyClass:
    class_attr = "shared"      # Class attribute

    def __init__(self, value):
        self.instance_attr = value  # Instance attribute

    def method(self):
        return self.instance_attr
```

### `self`

```python
class Square:
    def __init__(self, size):
        self.__size = size     # self refers to the instance being created

    def area(self):
        return self.__size ** 2  # self refers to the calling instance
```

`self` is not a keyword — it is a convention. The first parameter of any instance method receives the instance reference.

### `isinstance()`

```python
isinstance(5, int)         # True
isinstance(5, (int, float))  # True — checks against multiple types
isinstance(True, int)       # True — bool is a subclass of int
```

### `@property` decorator

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Read-only computed property."""
        return 3.14159 * self._radius ** 2
```

### `__dict__`

```python
s = Square(5)
s.__dict__    # {'_Square__size': 5}  — instance's attribute dictionary
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is encapsulation? How does Python implement it differently from Java or C++?
2. Explain Python's name mangling. Is `__attribute` truly private?
3. What is the difference between `@property` and a regular getter/setter method?
4. What is the difference between `__init__` and `__new__`? When would you override `__new__`?
5. What are class attributes vs instance attributes? How does Python resolve attribute lookup?

### Practical Coding Questions

1. Design a `BankAccount` class with `balance` (private, non-negative), `deposit()`, `withdraw()`, and `get_balance()`.
2. Create a `Temperature` class with a `celsius` property that automatically updates a `fahrenheit` property and vice versa.
3. Implement a `Password` class that validates minimum length, uppercase, lowercase, and digit requirements in its setter.
4. Write a `Counter` class that tracks how many times it has been incremented, with a read-only `count` property.
5. Design a `Color` class that accepts RGB values (0–255) with validation in the constructor.

### Debugging Scenarios

1. A developer accesses `square._Square__size` directly and sets it to `-5`. The square now has an invalid state. How could the class design prevent this?
2. A class defines `def __init__(size)` (missing `self`) and `Square(5)` raises `TypeError: __init__() takes 1 positional argument but 2 were given`. Explain the error.

### System Design Question

1. Design a `Configuration` class for a web application that: (a) loads settings from a file, (b) validates all values on assignment, (c) provides read-only access to sensitive values like database passwords, and (d) supports default values. How would you use properties, private attributes, and validation?

# Module: python-more_classes

## 1. Executive Summary

This module deepens OOP knowledge through a progressively complex `Rectangle` class (10 iterations). Students learn magic methods (`__str__`, `__repr__`, `__del__`), class attributes for instance tracking, customizable print symbols, static methods for comparison, and class methods for factory patterns. This module bridges basic OOP (encapsulation) and advanced OOP (inheritance, polymorphism) by introducing the full object lifecycle and class-level behavior.

---

## 2. Deep Concept Breakdown

### 2.1 Magic Methods (Dunder Methods)

**Formal definition:** Magic methods are special methods with double-underscore prefixes and suffixes that Python calls implicitly in response to specific operations.

#### `__str__` — Human-readable representation

```python
def __str__(self):
    if self.__width == 0 or self.__height == 0:
        return ""
    return "\n".join(["#" * self.__width for _ in range(self.__height)])
```

Called by `print(obj)`, `str(obj)`, and f-strings.

#### `__repr__` — Developer representation

```python
def __repr__(self):
    return f"Rectangle({self.__width}, {self.__height})"
```

Called by `repr(obj)` and in the interactive interpreter. Should return a string that could recreate the object: `eval(repr(obj)) == obj`.

#### `__del__` — Destructor

```python
def __del__(self):
    Rectangle.number_of_instances -= 1
    print("Bye rectangle...")
```

Called when the object is garbage collected. **Warning:** The timing of `__del__` is non-deterministic — never rely on it for critical cleanup. Use context managers instead.

### 2.2 Class Attributes

**Formal definition:** Class attributes are shared across all instances of a class, unlike instance attributes which are per-object.

```python
class Rectangle:
    number_of_instances = 0    # Shared by all instances
    print_symbol = "#"         # Customizable per-instance or per-class

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1    # Modify via class name
        self.__width = width                   # Instance attribute
```

**Attribute lookup order:** Instance → Class → Parent classes (MRO).

### 2.3 Static Methods

**Formal definition:** A static method belongs to the class namespace but does not receive `self` or `cls`. It is a utility function that is logically related to the class.

```python
@staticmethod
def bigger_or_equal(rect_1, rect_2):
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if not isinstance(rect_2, Rectangle):
        raise TypeError("rect_2 must be an instance of Rectangle")
    if rect_1.area() >= rect_2.area():
        return rect_1
    return rect_2
```

### 2.4 Class Methods and Factory Pattern

**Formal definition:** A class method receives the class itself (`cls`) as its first argument, enabling alternative constructors and factory patterns.

```python
@classmethod
def square(cls, size=0):
    return cls(size, size)    # Creates a new Rectangle with width == height
```

**Production relevance:** Factory methods are used extensively in Django (`Model.objects.create()`), SQLAlchemy (`Session.query()`), and Python's standard library (`datetime.fromtimestamp()`, `dict.fromkeys()`).

### 2.5 Object Lifecycle

```
1. __new__()    → Creates the instance (allocates memory)
2. __init__()   → Initializes the instance (sets attributes)
3. ... usage ...
4. __del__()    → Cleanup (called during garbage collection)
```

---

## 3. Task-Level Static Analysis

### Task: 0-rectangle.py

- **Problem statement:** Define an empty Rectangle class.
- **Design approach:** `class Rectangle: pass`.
- **Real-world analogy:** Declaring a database model before adding fields.

### Task: 1-rectangle.py

- **Problem statement:** Add `width` and `height` properties with validation.
- **Design approach:** Private attributes with property decorators, `TypeError`/`ValueError` validation.
- **OOP principles:** Encapsulation with controlled access.
- **Real-world analogy:** Form field definitions with built-in validation.

### Task: 2-rectangle.py

- **Problem statement:** Add `area()` and `perimeter()` methods.
- **Design approach:** Simple arithmetic methods. Perimeter returns 0 if width or height is 0.
- **Edge-case coverage:** Zero dimensions handled.
- **Time complexity:** O(1)
- **Real-world analogy:** Computed fields on a domain model.

### Task: 3-rectangle.py

- **Problem statement:** Add `__str__` for visual representation using `#`.
- **Design approach:** String building with `"\n".join()`.
- **Edge-case coverage:** Empty rectangle returns empty string.
- **Real-world analogy:** Admin display representation in Django.

### Task: 4-rectangle.py

- **Problem statement:** Add `__repr__` for reproducible representation.
- **Design approach:** Returns `Rectangle(width, height)` string.
- **OOP principles:** The `eval(repr(obj))` contract.
- **Real-world analogy:** Object serialization for logging and debugging.

### Task: 5-rectangle.py

- **Problem statement:** Add `__del__` destructor with goodbye message.
- **Design approach:** Print message on garbage collection.
- **OOP principles:** Object lifecycle management.
- **Real-world analogy:** Resource cleanup — closing database connections, releasing file handles.

### Task: 6-rectangle.py

- **Problem statement:** Track active instances with a class attribute.
- **Design approach:** Increment in `__init__`, decrement in `__del__`.
- **OOP principles:** Class attributes for shared state.
- **Real-world analogy:** Connection pool tracking — knowing how many connections are active.

### Task: 7-rectangle.py

- **Problem statement:** Customizable print symbol.
- **Design approach:** `print_symbol` class attribute, used via `str(self.print_symbol)`.
- **OOP principles:** Configurable class behavior.
- **Real-world analogy:** Theme configuration — changing the visual representation without modifying logic.

### Task: 8-rectangle.py

- **Problem statement:** Static method to compare rectangles by area.
- **Design approach:** `@staticmethod` with type validation, returns the larger rectangle.
- **OOP principles:** Static methods — class-related utilities without instance binding.
- **Real-world analogy:** Comparison utilities in sorting algorithms or ranking systems.

### Task: 9-rectangle.py

- **Problem statement:** Class method factory for creating squares.
- **Design approach:** `@classmethod def square(cls, size)` returns `cls(size, size)`.
- **OOP principles:** Factory pattern — alternative constructor.
- **Real-world analogy:** `datetime.now()`, `dict.fromkeys()`, `Path.home()`.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Encapsulation | ✅ | All files — private attributes with properties |
| Factory Method | ✅ | `9-rectangle.py` — `square()` class method |
| Observer Pattern (weak) | ✅ | `6-rectangle.py` — instance count tracking |
| Repr Contract | ✅ | `4-rectangle.py` — `eval(repr(obj))` reproducibility |
| Progressive Enhancement | ✅ | Each file builds on the previous |
| Resource Tracking | ✅ | `6-rectangle.py` — class-level instance counting |

---

## 5. Built-ins & Keywords Deep Dive

### `__str__` vs `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"    # For developers

    def __str__(self):
        return f"({self.x}, {self.y})"          # For users

p = Point(1, 2)
repr(p)     # "Point(1, 2)"
str(p)      # "(1, 2)"
print(p)    # "(1, 2)" — uses __str__
```

**Rule of thumb:** If you implement only one, implement `__repr__`. If `__str__` is missing, Python falls back to `__repr__`.

### `@staticmethod`

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b    # No access to self or cls

MathUtils.add(1, 2)     # 3 — called on the class
```

### `@classmethod`

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_string(cls, data):
        name, email = data.split(",")
        return cls(name, email)

user = User.from_string("Alice,alice@example.com")
```

### `__del__`

```python
class Resource:
    def __del__(self):
        print("Resource released")

r = Resource()
del r    # "Resource released" — but timing is not guaranteed
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the difference between `__str__` and `__repr__`? When is each called?
2. Explain the difference between class attributes and instance attributes. How does attribute lookup work?
3. What is a static method? How does it differ from a class method and an instance method?
4. What is the Factory Method pattern? Give an example from Python's standard library.
5. Why is relying on `__del__` for resource cleanup considered bad practice?

### Practical Coding Questions

1. Implement a `Vector` class with `__repr__`, `__str__`, `__add__`, `__mul__` (scalar), and `__eq__` magic methods.
2. Create a `ConnectionPool` class that tracks active connections with a class attribute, and includes `acquire()` and `release()` class methods.
3. Write a `Money` class with a `from_string()` class method that parses strings like `"$42.50"`.
4. Implement a `Logger` class with a `number_of_logs` class attribute and `__del__` that writes a final log entry.
5. Design a `Shape` class with a `from_dict()` factory method that creates the appropriate subclass based on a `"type"` key.

### Debugging Scenarios

1. A developer modifies `rectangle.print_symbol = [1, 2]` and `print(rectangle)` crashes. Explain why and how `str()` conversion in `__str__` prevents this.
2. `Rectangle.number_of_instances` shows 5 but only 3 rectangles are in scope. What happened to the other 2? How does `__del__` interact with garbage collection?

### System Design Question

1. Design a `DatabaseConnection` class that: (a) tracks all active connections via a class attribute, (b) provides a `connect()` class method, (c) limits total connections to a configurable maximum, and (d) properly cleans up on `__del__`. Discuss the limitations of this approach and alternatives (connection pool pattern, context managers).

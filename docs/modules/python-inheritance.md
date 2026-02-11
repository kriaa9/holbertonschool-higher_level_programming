# Module: python-inheritance

## 1. Executive Summary

This module introduces **inheritance** — the OOP mechanism that enables code reuse and polymorphism through class hierarchies. Students build a `BaseGeometry → Rectangle → Square` hierarchy, learning single and multi-level inheritance, `super()` for constructor chaining, `isinstance()`/`issubclass()` for type introspection, method overriding, and input validation at the base class level. This module is the bridge between basic OOP and advanced design patterns.

---

## 2. Deep Concept Breakdown

### 2.1 Inheritance

**Formal definition:** Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass), enabling code reuse and specialization.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):       # Method override
        return "Woof!"

class Puppy(Dog):          # Multi-level inheritance
    pass
```

**Memory model:** When accessing an attribute, Python follows the Method Resolution Order (MRO): instance → class → parent → grandparent → ... → `object`.

### 2.2 The `super()` Function

**Formal definition:** `super()` returns a proxy object that delegates method calls to the next class in the MRO. It enables cooperative multiple inheritance.

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
```

In this module, `super()` is used implicitly through inherited methods like `integer_validator()`.

### 2.3 Type Introspection

```python
isinstance(obj, ClassName)     # True if obj is instance of class or subclass
issubclass(Child, Parent)      # True if Child inherits from Parent
type(obj)                       # Returns exact type (no inheritance)
type(obj) is ClassName         # Exact type match
```

**Key distinction:**
- `isinstance(True, int)` → `True` (bool inherits from int)
- `type(True) is int` → `False` (exact type is bool, not int)

### 2.4 Method Overriding

**Formal definition:** A subclass can redefine a method from its parent, providing specialized behavior while maintaining the same interface.

```python
class Rectangle(BaseGeometry):
    def area(self):
        return self.__width * self.__height   # Overrides BaseGeometry.area()

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    def __str__(self):   # Overrides Rectangle.__str__()
        return "[Square] {}/{}".format(self.__size, self.__size)
```

### 2.5 Abstract Method Pattern (Pre-ABC)

Before introducing the `abc` module, this module uses an exception-based pattern to simulate abstract methods:

```python
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
```

This forces subclasses to override `area()` — though it only fails at runtime, not at class definition time (unlike `@abstractmethod`).

---

## 3. Task-Level Static Analysis

### Task: 0-lookup.py

- **Problem statement:** Return all attributes and methods of an object.
- **Design approach:** `return dir(obj)`.
- **OOP principles:** Introspection — runtime discovery of object capabilities.
- **Time complexity:** O(n) where n = number of attributes.
- **Real-world analogy:** Reflection-based serialization, plugin discovery.

### Task: 1-my_list.py

- **Problem statement:** Custom list class with a `print_sorted()` method.
- **Design approach:** `class MyList(list)` with `print_sorted()` using `sorted(self)`.
- **OOP principles:** Inheriting from built-in types, extending without overriding.
- **Edge-case coverage:** Tested with empty lists, negatives, duplicates (in `tests/1-my_list.txt`).
- **Real-world analogy:** Django's `QuerySet` — extending built-in collections with domain-specific methods.

### Task: 2-is_same_class.py

- **Problem statement:** Check if an object is exactly an instance of a class (not a subclass).
- **Design approach:** `return type(obj) is a_class`.
- **OOP principles:** Exact type matching vs. polymorphic type checking.
- **Real-world analogy:** Strict type validation in serialization — handling `int` differently from `bool`.

### Task: 3-is_kind_of_class.py

- **Problem statement:** Check if an object is an instance of a class or any of its subclasses.
- **Design approach:** `return isinstance(obj, a_class)`.
- **OOP principles:** Polymorphic type checking — the Liskov Substitution Principle.
- **Real-world analogy:** API parameter validation — accepting any numeric type.

### Task: 4-inherits_from.py

- **Problem statement:** Check if an object inherits from a class (is subclass instance but not exact).
- **Design approach:** `return isinstance(obj, a_class) and type(obj) is not a_class`.
- **OOP principles:** Distinguishing direct instances from inherited ones.
- **Real-world analogy:** Detecting framework-provided subclasses vs. user-defined classes.

### Task: 5-base_geometry.py

- **Problem statement:** Empty `BaseGeometry` class.
- **Design approach:** `class BaseGeometry: pass`.
- **Real-world analogy:** Defining a base interface before adding methods.

### Task: 6-base_geometry.py

- **Problem statement:** Add `area()` that raises `Exception`.
- **Design approach:** `raise Exception("area() is not implemented")`.
- **Potential improvements:** Should use `NotImplementedError` instead of generic `Exception`.
- **Real-world analogy:** Template Method pattern — declaring intent without implementation.

### Task: 7-base_geometry.py

- **Problem statement:** Add `integer_validator(name, value)` method.
- **Design approach:** Validates type (excluding bool) and positive value.
- **Edge-case coverage:** Rejects booleans (`isinstance(value, bool)` check), zero, negatives, strings, floats, None, lists, dicts, tuples (all tested in `tests/7-base_geometry.txt`).
- **Real-world analogy:** Generic field validator reusable across multiple model fields.

### Task: 8-rectangle.py

- **Problem statement:** `Rectangle(BaseGeometry)` with validated width and height.
- **Design approach:** Constructor uses `self.integer_validator()` from parent class.
- **OOP principles:** Inheritance-based validation — subclass leverages parent's utility method.
- **Real-world analogy:** Django model field validation inherited from base model.

### Task: 9-rectangle.py

- **Problem statement:** Add `area()` and `__str__()` to Rectangle.
- **Design approach:** `area()` returns width × height; `__str__()` returns `[Rectangle] w/h`.
- **OOP principles:** Method override, polymorphic representation.
- **Real-world analogy:** API resource serialization — each model defines its own string format.

### Task: 10-square.py

- **Problem statement:** `Square(Rectangle)` with validated size.
- **Design approach:** Constructor calls `super().__init__(size, size)`.
- **OOP principles:** Multi-level inheritance, constructor chaining with `super()`.
- **Potential improvements:** Stores `__size` redundantly — parent already stores width and height.
- **Real-world analogy:** Specialized subclass that constrains parent parameters.

### Task: 11-square.py

- **Problem statement:** Custom `__str__()` for Square: `[Square] size/size`.
- **Design approach:** Overrides Rectangle's `__str__` with Square-specific format.
- **OOP principles:** Polymorphism — same method, different behavior.
- **Real-world analogy:** Different serialization formats for different API resources.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Inheritance Hierarchy | ✅ | `BaseGeometry → Rectangle → Square` |
| Template Method | ✅ | `BaseGeometry.area()` — raises exception, subclasses implement |
| Polymorphism | ✅ | `__str__()` overridden in Rectangle and Square |
| Liskov Substitution | ✅ | Square can be used wherever Rectangle is expected |
| Defensive Programming | ✅ | `integer_validator()` with comprehensive checks |
| Composition via Inheritance | ✅ | Square reuses Rectangle's validation and computation |

---

## 5. Built-ins & Keywords Deep Dive

### `isinstance()` and `issubclass()`

```python
isinstance(42, int)          # True
isinstance(True, int)        # True — bool is subclass of int
issubclass(bool, int)        # True
issubclass(Square, Rectangle)  # True
issubclass(Square, BaseGeometry)  # True — transitive
```

### `type()`

```python
type(42)           # <class 'int'>
type(True)         # <class 'bool'>
type(True) is int  # False — exact type, not inheritance
```

### `super()`

```python
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)    # Call Parent.__init__
        self.y = y
```

### `dir()`

```python
dir(42)    # All methods of int: ['__abs__', '__add__', ...]
dir([])    # All methods of list: ['append', 'clear', ...]
```

### `__str__` and `__repr__`

```python
class Square(Rectangle):
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

s = Square(5)
print(s)       # [Square] 5/5
str(s)         # "[Square] 5/5"
repr(s)        # Falls back to __repr__ if not defined
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is the Liskov Substitution Principle? Does the `Square(Rectangle)` hierarchy violate it? Discuss.
2. Explain the Method Resolution Order (MRO) in Python. How does `super()` use it?
3. What is the difference between `isinstance()` and `type()` for type checking? When should you use each?
4. Why should abstract methods raise `NotImplementedError` instead of generic `Exception`?
5. What is the Diamond Problem in multiple inheritance? How does Python resolve it?

### Practical Coding Questions

1. Design a `Vehicle → Car → ElectricCar` hierarchy with shared and specialized attributes.
2. Implement a `Shape` base class with `area()` and `perimeter()` abstract methods, then create `Circle`, `Rectangle`, and `Triangle` subclasses.
3. Write a function that determines the full inheritance chain of any object (from the object's type up to `object`).
4. Create a `Validator` base class with subclasses `IntValidator`, `StringValidator`, and `RangeValidator`. Each validates a value and raises descriptive errors.
5. Implement `is_same_class`, `is_kind_of_class`, and `inherits_from` utility functions from scratch.

### Debugging Scenarios

1. A `Square` class inherits from `Rectangle` but only accepts `size` in its constructor. When `square.width = 10` is called, the square is no longer square. How should this be handled?
2. A developer creates `class MyList(list)` and overrides `append()` but forgets to call `super().append()`. Items are never added. Explain the fix.

### System Design Question

1. Design a notification system with a `BaseNotification` class and subclasses `EmailNotification`, `SMSNotification`, and `PushNotification`. Each has different `send()` implementations but shares `validate()` and `log()` methods. How would you structure the inheritance? Would you use ABC?

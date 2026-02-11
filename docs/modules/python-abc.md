# Module: python-abc

## 1. Executive Summary

This module introduces the most advanced OOP concepts in the curriculum: **Abstract Base Classes (ABCs)**, **duck typing**, **multiple inheritance**, **Method Resolution Order (MRO)**, and **mixins**. Students learn to define interface contracts with `@abstractmethod`, design polymorphic systems without explicit type checks (duck typing), compose behavior from multiple parents, and use mixins for reusable behavior units. These patterns are the foundation of enterprise framework design and plugin architectures.

---

## 2. Deep Concept Breakdown

### 2.1 Abstract Base Classes (ABCs)

**Formal definition:** An ABC is a class that cannot be instantiated directly and may define abstract methods that subclasses *must* implement.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

# Animal()    → TypeError: Can't instantiate abstract class
# Dog()       → Works fine
```

**Runtime behavior:** Python checks at instantiation time (not class definition time) whether all abstract methods are implemented. If any `@abstractmethod` is missing, `TypeError` is raised.

**Production relevance:** ABCs define contracts in Python. The `collections.abc` module provides abstract classes like `Iterable`, `Iterator`, `Mapping`, and `Sequence` that define the interfaces for Python's data model.

### 2.2 Duck Typing

**Formal definition:** "If it walks like a duck and quacks like a duck, then it is a duck." Duck typing means an object's suitability is determined by the presence of methods and properties, not by its actual type.

```python
def shape_info(shape):
    # No type check — just call the methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

**Key insight:** `shape_info()` works with *any* object that has `area()` and `perimeter()` methods — it doesn't need to inherit from `Shape`. This is the essence of Python's duck typing philosophy.

**Comparison with explicit typing:**
```python
# Duck typing (Pythonic)
def process(data):
    for item in data:       # Works with any iterable
        print(item)

# Explicit typing (less Pythonic)
def process(data):
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    for item in data:
        print(item)
```

### 2.3 Multiple Inheritance

**Formal definition:** A class can inherit from multiple parent classes, gaining attributes and methods from all of them.

```python
class Fish:
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
```

**MRO (Method Resolution Order):** `FlyingFish.__mro__` = `[FlyingFish, Fish, Bird, object]`

Python uses the **C3 linearization algorithm** to determine MRO, ensuring:
1. Children come before parents.
2. Parents maintain their specified order.
3. No class appears twice.

### 2.4 Mixins

**Formal definition:** A mixin is a class designed to provide specific behavior to other classes through multiple inheritance, without being a standalone entity.

```python
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
```

**Design principles:**
- Mixins should have **no `__init__`** (no state of their own).
- Mixins should provide **a single, focused behavior**.
- Mixins are named with the `Mixin` suffix by convention.

**Production examples:**
- Django: `LoginRequiredMixin`, `PermissionRequiredMixin`
- DRF: `ListModelMixin`, `CreateModelMixin`
- Flask: `MethodView` uses mixin-like dispatch

### 2.5 Iterator Protocol

**Formal definition:** An iterator implements `__iter__()` (returns self) and `__next__()` (returns next value or raises `StopIteration`).

```python
class CountedIterator:
    def __init__(self, iterable):
        self.__iterator = iter(iterable)
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.__iterator)    # Raises StopIteration when done
        self.__count += 1
        return item

    def get_count(self):
        return self.__count
```

### 2.6 Extending Built-in Types

```python
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def pop(self, index=-1):
        item = self[index]
        super().pop(index)
        print(f"Removed [{item}] from the list.")
```

**Key pattern:** Always call `super()` to ensure the parent's behavior is preserved.

---

## 3. Task-Level Static Analysis

### Task: task_00_abc.py

- **Problem statement:** Define an abstract `Animal` class with abstract `sound()` method, and concrete `Dog`/`Cat` subclasses.
- **Design approach:** `ABC` metaclass with `@abstractmethod`.
- **OOP principles:** Abstraction, interface contracts, polymorphism.
- **Time complexity:** O(1) for method calls.
- **Real-world analogy:** Defining a `PaymentGateway` interface with `process_payment()` that Stripe, PayPal, and Square implementations must provide.

### Task: task_01_duck_typing.py

- **Problem statement:** Implement abstract `Shape` with `Circle` and `Rectangle` subclasses, plus a `shape_info()` function using duck typing.
- **Design approach:** ABC for Shape, concrete implementations with `math.pi`, and a function that calls methods without type checking.
- **OOP principles:** Duck typing, abstraction, polymorphism.
- **Edge-case coverage:** `Circle` handles negative radius by taking `abs()`.
- **Time complexity:** O(1) for geometric calculations.
- **Real-world analogy:** A rendering engine that draws any shape with `area()` and `perimeter()` methods.

### Task: task_02_verboselist.py

- **Problem statement:** Create a list subclass that prints notifications on modifications.
- **Design approach:** Override `append`, `extend`, `remove`, `pop` with logging.
- **OOP principles:** Inheritance from built-in, method overriding, decorator pattern.
- **Potential improvements:** `remove()` prints success message before calling `super().remove()` — if the removal fails (item not found), the message is misleading.
- **Real-world analogy:** Audit logging on database operations — every insert/update/delete is logged.

### Task: task_03_countediterator.py

- **Problem statement:** Iterator wrapper that counts items yielded.
- **Design approach:** Composition — wraps any iterable, tracks count in `__next__`.
- **OOP principles:** Iterator protocol (`__iter__`, `__next__`), composition over inheritance.
- **Time complexity:** O(1) per `__next__` call.
- **Real-world analogy:** Progress tracking in batch processing — counting processed items.

### Task: task_04_flyingfish.py

- **Problem statement:** Demonstrate multiple inheritance with `Fish`, `Bird`, and `FlyingFish`.
- **Design approach:** `FlyingFish(Fish, Bird)` overrides all methods.
- **OOP principles:** Multiple inheritance, MRO.
- **Time complexity:** O(1)
- **Real-world analogy:** A class that combines capabilities from two distinct interfaces (e.g., a device that is both a printer and a scanner).

### Task: task_05_dragon.py

- **Problem statement:** Demonstrate mixin pattern with `SwimMixin`, `FlyMixin`, and `Dragon`.
- **Design approach:** Mixins provide `swim()` and `fly()`, Dragon adds `roar()`.
- **OOP principles:** Mixins, composition over inheritance, behavior composition.
- **Time complexity:** O(1)
- **Real-world analogy:** Django class-based views composing behavior from multiple mixins.

---

## 4. Patterns & Design Principles Detected

| Pattern | Present | Location |
|---|---|---|
| Abstraction | ✅ | `task_00_abc.py`, `task_01_duck_typing.py` — ABC with `@abstractmethod` |
| Duck Typing | ✅ | `task_01_duck_typing.py` — `shape_info()` function |
| Polymorphism | ✅ | All tasks — different implementations, same interface |
| Inheritance | ✅ | `task_02_verboselist.py` — extending built-in `list` |
| Composition | ✅ | `task_03_countediterator.py` — wraps an iterator |
| Mixins | ✅ | `task_05_dragon.py` — `SwimMixin`, `FlyMixin` |
| Multiple Inheritance | ✅ | `task_04_flyingfish.py` — `FlyingFish(Fish, Bird)` |
| Decorator Pattern | ✅ | `task_02_verboselist.py` — adds logging around core operations |
| Iterator Pattern | ✅ | `task_03_countediterator.py` — `__iter__`/`__next__` protocol |

---

## 5. Built-ins & Keywords Deep Dive

### `ABC` and `@abstractmethod`

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):      # Concrete method — inherited as-is
        return "I am a shape"
```

### `super()`

```python
class VerboseList(list):
    def append(self, item):
        super().append(item)    # Call list.append()
        print(f"Added {item}")
```

### `iter()` and `next()`

```python
my_list = [1, 2, 3]
it = iter(my_list)        # Creates iterator
next(it)                   # 1
next(it)                   # 2
next(it)                   # 3
next(it)                   # StopIteration
```

### `__mro__` and `mro()`

```python
FlyingFish.__mro__
# (<class 'FlyingFish'>, <class 'Fish'>, <class 'Bird'>, <class 'object'>)

FlyingFish.mro()
# Same as above, but returns a list
```

### `getattr()`

```python
getattr(obj, "method_name")()           # Dynamic method call
getattr(obj, "missing", "default")       # With fallback
hasattr(obj, "method_name")              # Check if attribute exists
```

---

## 6. Interview Question Bank

### Conceptual Questions

1. What is an Abstract Base Class? How does it differ from a regular class?
2. Explain duck typing. How does it relate to Python's `typing.Protocol`?
3. What is the Method Resolution Order (MRO)? How does Python's C3 linearization work?
4. What is a mixin? How does it differ from regular inheritance?
5. What is the difference between composition and inheritance? When should you use each?

### Practical Coding Questions

1. Design a `Serializable` ABC with abstract `serialize()` and `deserialize()` methods, then implement `JSONSerializable` and `XMLSerializable` subclasses.
2. Create a `LoggingMixin` that adds logging to any class's method calls using `__getattr__`.
3. Implement a `CacheMixin` that adds caching behavior to any class with a `compute()` method.
4. Write an iterator class that yields Fibonacci numbers up to a limit, implementing the full iterator protocol.
5. Design a class hierarchy for a file converter: `FileConverter(ABC)` with `CSVConverter`, `JSONConverter`, and `XMLConverter`. Include a `convert(input_path, output_path)` abstract method.

### Debugging Scenarios

1. A developer creates `class MyABC(ABC)` with `@abstractmethod def process(self)` but `class Child(MyABC)` forgets to implement `process()`. `Child()` raises `TypeError`. The developer is confused because the class definition succeeded. Explain why the error occurs at instantiation, not at definition.
2. `class C(A, B)` and `class D(B, A)` both exist. `class E(C, D)` raises `TypeError: Cannot create a consistent MRO`. Explain why.

### System Design Question

1. Design a plugin system for a web application where plugins can add new API endpoints, middleware, and database models. Use ABCs for plugin interfaces, mixins for shared behavior (logging, authentication), and duck typing for optional capabilities. How would you handle plugin discovery, validation, and lifecycle management?

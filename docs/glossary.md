# Glossary

## Master Glossary of Python and OOP Terminology

This glossary provides precise definitions, code examples, and production relevance for every key concept encountered in this curriculum.

---

### Abstract Base Class (ABC)

**Definition:** A class that cannot be instantiated and may define abstract methods that subclasses must implement. Defined using `abc.ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Shape()  → TypeError
```

**Production relevance:** ABCs define contracts in frameworks. Python's `collections.abc` provides `Iterable`, `Iterator`, `Mapping`, `Sequence`, etc.

---

### Abstraction

**Definition:** Hiding complex implementation details behind a simple interface. Users interact with *what* an object does, not *how* it does it.

```python
class DatabaseConnection:
    def execute(self, query):
        # Hides: connection pooling, retry logic, encoding, etc.
        pass
```

**Production relevance:** Every API, SDK, and framework is an abstraction layer.

---

### Closure

**Definition:** A function that captures and remembers variables from its enclosing scope, even after the outer function has returned.

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
counter()  # 1
counter()  # 2
```

**Production relevance:** Used in decorators, callback functions, and functional programming patterns.

---

### Composition

**Definition:** Building complex objects by combining simpler objects, rather than through inheritance. "Has-a" relationship vs. "is-a."

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()    # Car HAS an Engine

    def start(self):
        return self.engine.start()
```

**Production relevance:** Preferred over deep inheritance hierarchies. Used extensively in dependency injection.

---

### Deep Copy vs Shallow Copy

**Definition:**
- **Shallow copy:** Creates a new object but references the same nested objects.
- **Deep copy:** Creates a new object and recursively copies all nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)       # New outer list, same inner lists
deep = copy.deepcopy(original)      # New outer list, new inner lists

shallow[0].append(5)
print(original[0])  # [1, 2, 5] — affected!

deep[0].append(6)
print(original[0])  # [1, 2, 5] — not affected
```

**Production relevance:** Critical when passing mutable data between components to avoid unintended side effects.

---

### Decorator

**Definition:** A function that takes another function and extends its behavior without modifying it.

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

**Production relevance:** Used for logging, authentication, caching, rate limiting, and input validation (Flask `@app.route`, Django `@login_required`).

---

### Duck Typing

**Definition:** "If it walks like a duck and quacks like a duck, then it is a duck." An object's suitability is determined by the presence of methods, not its type.

```python
def process(data):
    for item in data:    # Works with list, tuple, set, generator, etc.
        print(item)
```

**Production relevance:** Core Python philosophy. Enables flexible, decoupled code. Related to Python's `typing.Protocol`.

---

### Encapsulation

**Definition:** Bundling data (attributes) and methods that operate on that data within a class, and restricting direct access to internal state.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # Private

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
```

**Production relevance:** Fundamental to API design — exposing a stable public interface while keeping implementation details private.

---

### Immutable vs Mutable

**Definition:**
- **Immutable:** Cannot be changed after creation (str, int, float, tuple, frozenset).
- **Mutable:** Can be changed in place (list, dict, set, custom objects).

```python
# Immutable
s = "hello"
s[0] = "H"    # TypeError

# Mutable
lst = [1, 2, 3]
lst[0] = 10   # [10, 2, 3]
```

**Production relevance:** Immutable objects are thread-safe and hashable (usable as dict keys). Mutable default arguments are a common bug source.

---

### Iterable vs Iterator

**Definition:**
- **Iterable:** Any object that implements `__iter__()` and returns an iterator.
- **Iterator:** An object that implements `__next__()` and raises `StopIteration` when exhausted.

```python
my_list = [1, 2, 3]          # Iterable
my_iter = iter(my_list)       # Iterator

next(my_iter)  # 1
next(my_iter)  # 2
next(my_iter)  # 3
next(my_iter)  # StopIteration
```

**Key difference:** An iterable can be iterated multiple times; an iterator is consumed once.

**Production relevance:** Generators, database cursors, and file objects are iterators — they enable memory-efficient processing of large datasets.

---

### JSON (JavaScript Object Notation)

**Definition:** A lightweight, text-based data interchange format using key-value pairs and arrays.

```python
import json

data = {"name": "Alice", "scores": [95, 87, 91]}
json_str = json.dumps(data)     # Serialize
parsed = json.loads(json_str)   # Deserialize
```

**Production relevance:** The de facto standard for REST API communication, configuration files, and data interchange.

---

### Lambda Function

**Definition:** An anonymous, single-expression function defined with the `lambda` keyword.

```python
square = lambda x: x ** 2
add = lambda a, b: a + b

# Common use: sorting key
sorted(users, key=lambda u: u["age"])
```

**Production relevance:** Used for short, throwaway functions in `map()`, `filter()`, `sorted()`, and callback registrations.

---

### Magic Methods (Dunder Methods)

**Definition:** Special methods with double-underscore names (`__method__`) that Python calls implicitly for specific operations.

| Method | Trigger | Example |
|---|---|---|
| `__init__` | Object creation | `obj = MyClass()` |
| `__str__` | `str(obj)`, `print(obj)` | Human-readable representation |
| `__repr__` | `repr(obj)`, debugger | Developer representation |
| `__len__` | `len(obj)` | Collection length |
| `__eq__` | `obj1 == obj2` | Equality comparison |
| `__del__` | Object deletion | Cleanup (non-deterministic) |
| `__iter__` | `for x in obj` | Iteration support |
| `__next__` | `next(obj)` | Iterator advancement |
| `__getattr__` | Attribute not found | Dynamic attribute access |

**Production relevance:** Enables Python's operator overloading, context managers (`__enter__`/`__exit__`), and protocol implementations.

---

### Method Resolution Order (MRO)

**Definition:** The order in which Python searches for methods in a class hierarchy. Computed using the C3 linearization algorithm.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

D.__mro__
# (D, B, C, A, object)
```

**Production relevance:** Understanding MRO is critical for debugging multiple inheritance issues and designing cooperative `super()` chains.

---

### Mixin

**Definition:** A class designed to provide specific behavior to other classes through multiple inheritance, without being a standalone entity.

```python
class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class UserService(LoggingMixin):
    def create_user(self, name):
        self.log(f"Creating user {name}")
```

**Production relevance:** Django's `LoginRequiredMixin`, DRF's `ListModelMixin`, `CreateModelMixin`.

---

### OOP (Object-Oriented Programming)

**Definition:** A programming paradigm based on the concept of "objects" — entities that combine data (attributes) and behavior (methods).

**Four pillars:**
1. **Encapsulation** — Bundling data and methods, hiding internals.
2. **Abstraction** — Exposing only essential features.
3. **Inheritance** — Deriving new classes from existing ones.
4. **Polymorphism** — Same interface, different implementations.

**Production relevance:** The dominant paradigm for backend development. Django, Flask, FastAPI, SQLAlchemy all use OOP extensively.

---

### Pickle

**Definition:** Python's native binary serialization protocol. Can serialize almost any Python object.

```python
import pickle

data = {"key": [1, 2, 3], "nested": {"a": True}}
serialized = pickle.dumps(data)
deserialized = pickle.loads(serialized)
```

**⚠️ Security:** Never unpickle untrusted data — `pickle.load()` can execute arbitrary code.

**Production relevance:** Used for caching (Django cache backend), ML model persistence (scikit-learn), and inter-process communication (multiprocessing).

---

### Polymorphism

**Definition:** The ability of different objects to respond to the same method call with different behavior.

```python
class Circle:
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def area(self):
        return self.width * self.height

# Polymorphic usage
for shape in [Circle(5), Rectangle(3, 4)]:
    print(shape.area())    # Different implementation, same interface
```

**Production relevance:** Enables plugin systems, strategy patterns, and framework extensibility.

---

### Scope (LEGB Rule)

**Definition:** Python resolves names in four scopes, searched in order:
1. **L**ocal — Inside the current function
2. **E**nclosing — Inside enclosing functions (closures)
3. **G**lobal — Module-level names
4. **B**uilt-in — Python's built-in names

```python
x = "global"          # Global

def outer():
    x = "enclosing"   # Enclosing

    def inner():
        x = "local"   # Local
        print(x)       # "local"

    inner()
```

**Production relevance:** Understanding scope prevents name shadowing bugs and is essential for writing closures and decorators.

---

### Serialization vs Marshaling

**Definition:**
- **Serialization:** Converting an object to a byte stream or string for storage/transmission.
- **Marshaling:** Serialization + passing the serialized data to another process/system (includes transport).

```python
# Serialization
json_str = json.dumps({"key": "value"})    # Object → string

# Marshaling (serialization + transport)
socket.sendall(json_str.encode('utf-8'))    # String → bytes → network
```

**Production relevance:** REST APIs perform marshaling (serialize to JSON, transmit over HTTP). RPC frameworks (gRPC, XML-RPC) are marshalers.

---

### Traceback

**Definition:** A report showing the call stack at the point where an exception occurred, from the most recent call to the original entry point.

```python
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    result = divide(10, 0)
  File "utils.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero
```

**Production relevance:** Tracebacks are essential for debugging. In production, they are captured by logging frameworks and error tracking services (Sentry, Datadog).

---

### Memory References

**Definition:** In Python, variables are references (pointers) to objects in memory. Assignment copies the reference, not the object.

```python
a = [1, 2, 3]
b = a           # b points to the SAME list object
b.append(4)
print(a)        # [1, 2, 3, 4] — both affected

c = a[:]        # c is a COPY (new list object)
c.append(5)
print(a)        # [1, 2, 3, 4] — unchanged
```

**Key function:** `id(obj)` returns the memory address of an object. `a is b` checks if two references point to the same object.

**Production relevance:** Understanding references is critical for avoiding shared-state bugs in multi-threaded applications and when passing mutable objects between functions.

---

### Property

**Definition:** A Pythonic mechanism for defining getter, setter, and deleter methods that look like regular attribute access.

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
            raise ValueError("Radius must be non-negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2    # Read-only computed property
```

**Production relevance:** Properties enable computed fields, validation on assignment, lazy loading, and maintaining backward compatibility when refactoring from public attributes to computed values.

---

### `super()`

**Definition:** Returns a proxy object that delegates method calls to the next class in the Method Resolution Order (MRO).

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)    # Calls Parent.__init__
        self.age = age
```

**Production relevance:** Essential for cooperative multiple inheritance and properly initializing parent classes in complex hierarchies.

---

### Context Manager

**Definition:** An object that defines `__enter__` and `__exit__` methods, used with the `with` statement for guaranteed resource management.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False    # Don't suppress exceptions
```

**Production relevance:** Used for file handling, database transactions, locks, temporary directories, and network connections.

---

### Type Hints (PEP 484)

**Definition:** Optional annotations that specify expected types for function parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}"

from typing import List, Optional

def find(items: List[int], target: int) -> Optional[int]:
    return items.index(target) if target in items else None
```

**Production relevance:** Enables static analysis with `mypy`, IDE auto-completion, and self-documenting code. Increasingly required in professional Python codebases.

---

### Generator

**Definition:** A function that uses `yield` to produce a sequence of values lazily, one at a time.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
next(gen)  # 0
next(gen)  # 1
next(gen)  # 1
next(gen)  # 2
```

**Production relevance:** Generators enable memory-efficient processing of large datasets, streaming data, and implementing coroutines for async programming.

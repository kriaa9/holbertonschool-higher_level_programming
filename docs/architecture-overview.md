# Architecture Overview

## Conceptual Layering

This repository is organized as a **layered curriculum** where each module introduces new abstractions while reinforcing foundational concepts. The architecture can be understood in four distinct tiers:

```
┌─────────────────────────────────────────────────────────────┐
│  Tier 4: Integration & Applied Patterns                     │
│  ┌───────────────────┐  ┌────────────────────────────────┐  │
│  │ python-input_output│  │ python-serialization           │  │
│  │ (File I/O, JSON)  │  │ (JSON, Pickle, CSV, XML, Net) │  │
│  └───────────────────┘  └────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  Tier 3: Advanced OOP & Design Patterns                     │
│  ┌───────────────────┐  ┌─────────────────────────────┐    │
│  │ python-inheritance │  │ python-abc                  │    │
│  │ (Hierarchies, MRO)│  │ (ABC, Duck Typing, Mixins)  │    │
│  └───────────────────┘  └─────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│  Tier 2: OOP Foundations & Quality Assurance                │
│  ┌────────────────┐ ┌──────────────────┐ ┌──────────────┐  │
│  │ python-classes  │ │ python-more_     │ │ python-test_ │  │
│  │ (Encapsulation) │ │ classes (Magic   │ │ driven_dev   │  │
│  │                 │ │ methods, Factory)│ │ (TDD, Tests) │  │
│  └────────────────┘ └──────────────────┘ └──────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  Tier 1: Procedural Programming & Data                      │
│  ┌───────────┐ ┌────────────┐ ┌──────────┐ ┌────────────┐ │
│  │ hello_    │ │ if_else_   │ │ import_  │ │ data_      │ │
│  │ world     │ │ loops_func │ │ modules  │ │ structures │ │
│  └───────────┘ └────────────┘ └──────────┘ └────────────┘ │
│  ┌────────────────────┐ ┌──────────────────┐               │
│  │ more_data_structures│ │ python-exceptions│               │
│  └────────────────────┘ └──────────────────┘               │
└─────────────────────────────────────────────────────────────┘
```

---

## How Modules Build on Each Other

### Tier 1 → Tier 2: From Procedures to Objects

The transition from procedural to object-oriented programming is the curriculum's central pedagogical arc:

1. **`python-hello_world`** establishes output mechanics — `print()`, f-strings, string slicing.
2. **`python-if_else_loops_functions`** introduces control flow and function definitions — the building blocks of methods.
3. **`python-import_modules`** teaches modular code organization — a prerequisite for understanding class modules.
4. **`python-data_structures`** and **`python-more_data_structures`** provide the data modeling vocabulary (lists, dicts, sets) that later becomes instance attribute management.
5. **`python-exceptions`** introduces error handling patterns that are critical for robust class constructors and method implementations.

### Tier 2: OOP Emergence

6. **`python-classes`** introduces the `class` keyword, `__init__`, private attributes, properties, and encapsulation through a progressively complex `Square` class.
7. **`python-more_classes`** expands OOP with magic methods (`__str__`, `__repr__`, `__del__`), class attributes, static methods, class methods, and the Factory pattern — all through a `Rectangle` class.
8. **`python-test_driven_development`** runs in parallel, teaching students to write tests *before* implementation — a discipline that becomes essential for validating class behavior.

### Tier 2 → Tier 3: From Classes to Hierarchies

9. **`python-inheritance`** builds a `BaseGeometry → Rectangle → Square` hierarchy, demonstrating single and multi-level inheritance, `super()`, `isinstance()`, and method overriding.
10. **`python-abc`** introduces abstract base classes, the `@abstractmethod` decorator, duck typing, multiple inheritance, and mixins — the most advanced OOP concepts in the curriculum.

### Tier 3 → Tier 4: From Objects to Persistence

11. **`python-input_output`** teaches file operations and JSON serialization, connecting in-memory objects to persistent storage.
12. **`python-serialization`** extends this to multiple formats (Pickle, CSV, XML) and introduces network serialization with TCP sockets — bridging the gap to distributed systems.

---

## OOP Evolution Across Folders

| Module | OOP Concept Introduced | Key Mechanism |
|---|---|---|
| `python-classes` | Encapsulation | Private attributes (`__size`), properties, getters/setters |
| `python-more_classes` | Representation & Lifecycle | `__str__`, `__repr__`, `__del__`, class attributes |
| `python-more_classes` | Factory Pattern | `@classmethod` for alternative constructors |
| `python-more_classes` | Utility Methods | `@staticmethod` for class-related utilities |
| `python-inheritance` | Inheritance | `class Child(Parent)`, `super().__init__()` |
| `python-inheritance` | Polymorphism | Method overriding (`__str__`, `area()`) |
| `python-inheritance` | Type Introspection | `isinstance()`, `issubclass()`, `type()` |
| `python-abc` | Abstraction | `ABC`, `@abstractmethod` |
| `python-abc` | Duck Typing | Interface-based programming without explicit type checks |
| `python-abc` | Multiple Inheritance | `FlyingFish(Fish, Bird)` with MRO |
| `python-abc` | Mixins | `SwimMixin`, `FlyMixin` for behavior composition |

---

## Transition: Procedural → OOP → Advanced OOP → Serialization

```
PROCEDURAL                OOP                    ADVANCED OOP           SERIALIZATION
─────────────────────    ─────────────────────   ─────────────────────  ─────────────────
Functions                Classes                 Abstract Classes       JSON dumps/loads
Variables                Instance attributes     Inheritance trees      Pickle serialize
if/else/loops            Properties              Polymorphism           CSV DictReader
String formatting        __init__                Duck typing            XML ElementTree
Module imports           Encapsulation           Mixins + MRO           Socket + JSON
Exception handling       Magic methods           Factory pattern        File persistence
```

---

## Where Abstraction Begins

Abstraction emerges in **`python-classes`** (Tier 2) when private attributes are hidden behind properties:

```python
# python-classes/4-square.py
@property
def size(self):
    return self.__size        # Implementation detail hidden

@size.setter
def size(self, value):
    # Validation logic abstracted away from the caller
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    self.__size = value
```

Formal abstraction (in the ABC sense) appears in **`python-abc`** (Tier 3):

```python
# python-abc/task_00_abc.py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):          # Contract: subclasses MUST implement
        pass
```

---

## Where Polymorphism Appears

Polymorphism first appears in **`python-inheritance`** through method overriding:

```python
# python-inheritance/9-rectangle.py
class Rectangle(BaseGeometry):
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# python-inheritance/11-square.py
class Square(Rectangle):
    def __str__(self):        # Same interface, different behavior
        return "[Square] {}/{}".format(self._Square__size, self._Square__size)
```

Duck typing polymorphism appears in **`python-abc`**:

```python
# python-abc/task_01_duck_typing.py
def shape_info(shape):
    print("Area: {}".format(shape.area()))          # No type check
    print("Perimeter: {}".format(shape.perimeter())) # Just calls methods
```

---

## Where Encapsulation Is Enforced

Encapsulation is introduced in **`python-classes`** and enforced through Python's name mangling:

```python
# python-classes/1-square.py
class Square:
    def __init__(self, size):
        self.__size = size    # Name-mangled to _Square__size
```

The pattern matures with property-based validation in `4-square.py` through `6-square.py`, where external access is mediated through `@property` decorators that enforce type and value constraints.

---

## How Input/Output Integrates with Serialization

The curriculum builds a clear pipeline from in-memory objects to persistent and networked data:

```
python-input_output                    python-serialization
───────────────────                    ────────────────────
read_file() / write_file()      →     Basic file I/O operations
to_json_string() / from_json()  →     serialize_and_save_to_file()
save_to_json_file()             →     convert_csv_to_json()
Student.to_json()               →     CustomObject.serialize() [Pickle]
Student.reload_from_json()      →     serialize_to_xml() / deserialize_from_xml()
7-add_item.py (CLI + JSON)      →     task_04_net.py (sockets + JSON)
```

The `Student` class in `python-input_output` serves as the bridge — it demonstrates how an object can serialize itself to a dictionary (`to_json()`) and reconstruct itself from one (`reload_from_json()`). This pattern is the foundation for ORM-style object persistence used in frameworks like Django and SQLAlchemy.

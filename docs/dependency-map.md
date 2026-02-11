# Dependency Map

## Conceptual Dependencies Between Modules

This document maps the prerequisite relationships between modules, explaining *why* each dependency exists and what conceptual foundations must be in place before advancing.

---

## Visual Dependency Graph

```
python-hello_world
    │
    ▼
python-if_else_loops_functions
    │
    ├──────────────────────────────┐
    ▼                              ▼
python-import_modules         python-data_structures
    │                              │
    │                              ▼
    │                     python-more_data_structures
    │                              │
    ├──────────────────────────────┤
    ▼                              ▼
python-exceptions          python-test_driven_development
    │                              │
    ├──────────────────────────────┘
    ▼
python-classes
    │
    ▼
python-more_classes
    │
    ▼
python-inheritance
    │
    ├──────────────────┐
    ▼                  ▼
python-abc        python-input_output
    │                  │
    └──────┬───────────┘
           ▼
    python-serialization
```

---

## Dependency Explanations

### 1. `python-if_else_loops_functions` depends on `python-hello_world`

**Why:** Before writing conditional logic and loops, students must understand how to produce output with `print()` and manipulate strings. The `hello_world` module establishes the syntactic basics — string formatting, f-strings, and the execution model — that are prerequisites for every subsequent module.

**Specific dependencies:**
- `print()` with `end=""` parameter (used extensively in loop-based output)
- String formatting with `.format()` and f-strings
- Basic variable assignment and types

---

### 2. `python-import_modules` depends on `python-if_else_loops_functions`

**Why:** Module imports require understanding of functions (since imported entities are often functions), and CLI argument processing (`sys.argv`) requires knowledge of loops and conditionals to iterate over and validate arguments.

**Specific dependencies:**
- Function definitions and calls (modules export functions)
- Loops for iterating over `sys.argv`
- Conditionals for `if __name__ == "__main__"` guard

---

### 3. `python-data_structures` depends on `python-if_else_loops_functions`

**Why:** List manipulation requires loops for iteration, conditionals for filtering, and functions for encapsulating operations. Without control flow mastery, students cannot effectively work with sequential data.

**Specific dependencies:**
- `for` loops for list traversal
- Indexing and slicing (builds on string slicing from `hello_world`)
- Functions that accept and return lists

---

### 4. `python-more_data_structures` depends on `python-data_structures`

**Why:** Dictionaries and sets are higher-order data structures that build on list concepts. Comprehensions are syntactic sugar over loop patterns. `lambda` and `map()` require function understanding.

**Specific dependencies:**
- List operations (comprehensions generalize list building)
- Iteration patterns (dictionary iteration extends list iteration)
- Function concepts (`lambda` is anonymous function syntax)

---

### 5. `python-exceptions` depends on `python-if_else_loops_functions` and `python-data_structures`

**Why:** Exception handling wraps around existing operations — you cannot learn `try`/`except` without having operations that can fail. List indexing errors, type errors, and division by zero all require prior knowledge of the operations that produce them.

**Specific dependencies:**
- List indexing (for `IndexError` handling)
- Type awareness (for `TypeError` and `ValueError`)
- Function definitions (exceptions are raised and caught within functions)
- Division operations (for `ZeroDivisionError`)

---

### 6. `python-test_driven_development` depends on `python-exceptions` and `python-data_structures`

**Why:** Writing tests requires understanding what can go wrong (exceptions), how data structures behave (expected outputs), and how to design functions with clear contracts. TDD enforces design discipline by requiring students to think about edge cases and error conditions *before* implementation.

**Specific dependencies:**
- Exception types (tests verify that correct exceptions are raised)
- Data structures (tests validate list/dict operations)
- String formatting (test output comparison)
- Function design (unit under test must be a well-defined function)

---

### 7. Why Inheritance Depends on Classes

**`python-inheritance`** requires **`python-classes`** and **`python-more_classes`** because:

1. **Class syntax** — Students must understand `class`, `__init__`, and instance attributes before learning `class Child(Parent)`.
2. **Encapsulation** — Private attributes and properties established in `python-classes` explain *why* inheritance needs `super()` to properly initialize parent state.
3. **Magic methods** — `__str__` and `__repr__` from `python-more_classes` are the methods most commonly overridden in inheritance hierarchies.
4. **Validation patterns** — The type-checking logic in `Square` constructors becomes the foundation for `BaseGeometry.integer_validator()`.

**Without classes:** Inheritance is meaningless — there is nothing to inherit *from*.

---

### 8. Why ABC Depends on Inheritance

**`python-abc`** requires **`python-inheritance`** because:

1. **Abstract classes extend inheritance** — An ABC is a class that *cannot be instantiated directly*, which only makes sense if students already understand how parent classes delegate to children.
2. **`@abstractmethod` enforces contracts** — This decorator requires understanding of method overriding, which is an inheritance concept.
3. **Multiple inheritance and MRO** — The `FlyingFish(Fish, Bird)` example requires understanding single inheritance before introducing the complexity of multiple parents and method resolution order.
4. **Mixins are inheritance** — `SwimMixin` and `FlyMixin` are classes that use inheritance mechanics but follow a different design philosophy (composition over inheritance).

**Without inheritance:** Abstract classes, duck typing, and mixins have no conceptual foundation.

---

### 9. Why Serialization Depends on OOP

**`python-serialization`** requires **`python-classes`**, **`python-inheritance`**, and **`python-input_output`** because:

1. **Objects are the subjects of serialization** — `CustomObject.serialize()` requires a class to serialize. Without OOP, serialization is limited to primitive dictionaries.
2. **`@classmethod` for deserialization** — `CustomObject.deserialize()` uses a class method pattern introduced in `python-more_classes`.
3. **File I/O foundations** — `python-input_output` establishes file operations (`open()`, `with` statement, read/write modes) that serialization builds upon.
4. **JSON understanding** — `python-input_output` introduces `json.dumps()`/`json.loads()` before serialization applies them to complex objects and multiple formats.

**Without OOP:** Serialization degrades to simple file read/write — the rich patterns of object persistence, class methods for deserialization, and self-serializing objects would be inaccessible.

---

### 10. Why TDD Enforces Design Discipline

**`python-test_driven_development`** is both a dependency and a cross-cutting concern:

1. **Forces interface thinking** — Writing tests first requires defining function signatures, parameter types, return values, and error conditions *before* implementation.
2. **Documents behavior** — Doctest files serve as executable specifications that define expected behavior for every input class (valid, invalid, edge-case).
3. **Catches design flaws** — The doctest for `add_integer` reveals that the function accepts floats but truncates them — a design decision that tests make explicit.
4. **Enables refactoring** — With tests in place, students can confidently modify implementations knowing that behavioral regressions will be caught.

**Design discipline impact:** Every module after TDD benefits from students' ability to think about edge cases, error conditions, and expected behavior. The validation patterns in `python-classes` and `python-inheritance` directly reflect TDD thinking.

---

## Cross-Module Concept Flow

| Concept | Introduced In | Reinforced In | Mastered In |
|---|---|---|---|
| `print()` / output | `hello_world` | `if_else_loops` | `classes` (`my_print`) |
| String formatting | `hello_world` | `data_structures` | `more_classes` (`__str__`) |
| Loops | `if_else_loops` | `data_structures` | `input_output` (file processing) |
| Functions | `if_else_loops` | `more_data_structures` | `classes` (methods) |
| Error handling | `exceptions` | `tdd` | `serialization` |
| Type checking | `exceptions` | `classes` | `inheritance` (`integer_validator`) |
| `__init__` | `classes` | `more_classes` | `inheritance` (`super()`) |
| Properties | `classes` | `more_classes` | `inheritance` |
| `__str__` | `more_classes` | `inheritance` | `abc` (duck typing) |
| Inheritance | `inheritance` | `abc` | `serialization` |
| File I/O | `input_output` | `serialization` | `serialization` (multi-format) |
| JSON | `input_output` | `serialization` | `serialization` (network) |

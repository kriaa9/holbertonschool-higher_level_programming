# Curriculum Progression

## Module → Concepts → Skills → Real-World Equivalent

This document maps each module in the curriculum to its core concepts, the technical skills developed, and their real-world backend engineering equivalents.

---

## Progression Map

| # | Module | Core Concepts | Skills Developed | Real-World Equivalent |
|---|--------|--------------|------------------|----------------------|
| 1 | `python-hello_world` | Print statements, string formatting, f-strings, string slicing | Output generation, string manipulation | Logging, template rendering, response formatting |
| 2 | `python-if_else_loops_functions` | Conditionals, loops, functions, ASCII operations | Control flow, algorithm design, code organization | Business logic, validation rules, request routing |
| 3 | `python-import_modules` | Module imports, `sys.argv`, CLI argument handling | Code modularization, command-line tooling | Package architecture, CLI tools, microservice entry points |
| 4 | `python-data_structures` | Lists, tuples, slicing, matrix operations | Sequential data management, tuple packing/unpacking | Array-based data processing, multi-value returns |
| 5 | `python-more_data_structures` | Dictionaries, sets, comprehensions, `lambda`, `map()` | Key-value data modeling, functional programming | Configuration management, caching, data transformation pipelines |
| 6 | `python-exceptions` | `try`/`except`/`finally`, `raise`, exception types | Error recovery, defensive programming | API error responses, transaction rollback, graceful degradation |
| 7 | `python-test_driven_development` | Doctest, unittest, edge-case analysis, TDD workflow | Test writing, validation logic, specification design | CI/CD test suites, QA automation, contract testing |
| 8 | `python-classes` | Classes, `__init__`, private attributes, properties | Encapsulation, data modeling, input validation | Domain models, DTOs, configuration objects |
| 9 | `python-more_classes` | `__str__`, `__repr__`, `__del__`, class/static methods | Object lifecycle, representation, factory pattern | ORM models, admin representations, builder pattern |
| 10 | `python-inheritance` | Single/multi-level inheritance, `super()`, `isinstance()` | Hierarchy design, type checking, code reuse | Framework base classes, plugin architectures |
| 11 | `python-abc` | ABC, `@abstractmethod`, duck typing, mixins, MRO | Interface design, behavior composition | Service interfaces, middleware, protocol classes |
| 12 | `python-input_output` | File I/O, JSON serialization, `with` statement, `sys.argv` | Data persistence, file processing, CLI tools | Log processing, config files, data import/export |
| 13 | `python-serialization` | JSON, Pickle, CSV, XML, TCP sockets | Multi-format serialization, network communication | REST APIs, data interchange, microservice communication |

---

## Detailed Progression Analysis

### Stage 1: Language Mechanics (Modules 1–3)

**Goal:** Establish syntactic fluency and understand Python's execution model.

```
python-hello_world
  └─ Students learn to produce output and manipulate strings.
     This is the "I can make the computer do something" moment.

python-if_else_loops_functions
  └─ Students learn to make decisions and repeat operations.
     Functions introduce the concept of reusable code units.

python-import_modules
  └─ Students learn to organize code across files.
     sys.argv introduces the concept of external input.
```

**Backend analogy:** Understanding how a request flows through a web framework — URL routing (conditionals), middleware chains (functions), and application structure (modules).

---

### Stage 2: Data Modeling (Modules 4–5)

**Goal:** Master Python's built-in data structures and functional programming tools.

```
python-data_structures
  └─ Lists and tuples become the primary tools for
     managing collections of data.

python-more_data_structures
  └─ Dictionaries introduce key-value associations.
     Sets provide mathematical operations.
     Comprehensions and lambda enable concise data transformations.
```

**Backend analogy:** Database result sets (lists of dicts), cache key-value stores (Redis-like patterns), and ETL transformation pipelines (map/filter/reduce).

---

### Stage 3: Resilience & Quality (Modules 6–7)

**Goal:** Write code that handles failure gracefully and is verifiably correct.

```
python-exceptions
  └─ Students learn to anticipate and recover from errors.
     The try/except/finally pattern becomes second nature.

python-test_driven_development
  └─ Students learn to specify behavior before implementing it.
     Doctest and unittest provide verification frameworks.
```

**Backend analogy:** Exception handling is essential for API error responses (HTTP 4xx/5xx). TDD is the standard in production teams for maintaining code quality and preventing regressions.

---

### Stage 4: Object-Oriented Design (Modules 8–9)

**Goal:** Transition from procedural to object-oriented thinking.

```
python-classes
  └─ The Square class evolves across 7 files:
     Empty class → constructor → validation → properties → visualization
     Each file adds one concept, building encapsulation incrementally.

python-more_classes
  └─ The Rectangle class evolves across 10 files:
     Empty class → properties → area/perimeter → __str__/__repr__
     → __del__ → class attributes → print_symbol → static methods
     → class methods (Factory pattern)
```

**Backend analogy:** Django/SQLAlchemy models, where classes represent database tables with validated fields, string representations, and factory methods for common creation patterns.

---

### Stage 5: Hierarchy & Abstraction (Modules 10–11)

**Goal:** Design extensible systems using inheritance and abstraction.

```
python-inheritance
  └─ BaseGeometry → Rectangle → Square hierarchy.
     Students learn to extend behavior, validate types,
     and leverage super() for constructor chaining.

python-abc
  └─ Abstract classes enforce interface contracts.
     Duck typing enables flexible polymorphism.
     Mixins provide composable behavior units.
     MRO determines method resolution in diamond inheritance.
```

**Backend analogy:** Framework plugin systems (abstract base), API serializer hierarchies (inheritance), authentication mixins (Django's LoginRequiredMixin), and protocol-based design (Python's typing.Protocol).

---

### Stage 6: Persistence & Communication (Modules 12–13)

**Goal:** Connect in-memory objects to the outside world.

```
python-input_output
  └─ File operations (read/write/append) with context managers.
     JSON serialization for object persistence.
     Student class demonstrates object ↔ dict ↔ JSON pipeline.
     Pascal's triangle showcases algorithmic thinking.

python-serialization
  └─ Multiple serialization formats: JSON, Pickle, CSV, XML.
     Network serialization via TCP sockets.
     Real-world data interchange patterns.
```

**Backend analogy:** REST API request/response serialization, database ORM persistence, configuration file management, inter-service communication in microservice architectures.

---

## Skill Dependency Chain

```
String manipulation
    └─ Control flow
        └─ Functions
            └─ Modules
                └─ Data structures
                    ├─ Exception handling
                    │   └─ TDD
                    └─ Classes
                        └─ Advanced OOP
                            └─ Inheritance
                                └─ Abstract classes
                                    └─ File I/O
                                        └─ Serialization
                                            └─ Network communication
```

---

## Competency Milestones

| Milestone | After Module | Student Can... |
|---|---|---|
| **Scripting** | Module 3 | Write CLI tools that process arguments and produce output |
| **Data Processing** | Module 5 | Transform, filter, and aggregate data using Python collections |
| **Defensive Coding** | Module 7 | Handle errors gracefully and write tests to verify behavior |
| **OOP Modeling** | Module 9 | Design classes with encapsulation, validation, and proper representation |
| **Architecture** | Module 11 | Design extensible systems with inheritance hierarchies and interfaces |
| **Full-Stack Data** | Module 13 | Serialize objects across formats and transmit data over networks |

# Python - More Classes and Objects

An advanced exploration of Object-Oriented Programming (OOP) in Python, building upon foundational class concepts with real-world applications.

---

## 📚 Project Overview

This project dives deeper into **classes and objects** in Python by building a `Rectangle` class from scratch. You'll progressively add features like:
- Properties with validation
- Area and perimeter calculations
- String representations
- Instance counting
- Class and static methods
- Comparison operators

---

## 🧠 Learning Objectives

By the end of this project, you should understand:

### Why Python Programming is Awesome
Python's clean syntax and powerful OOP features make it ideal for modeling real-world entities. The language encourages readable, maintainable code through conventions like properties and special methods.

### Advanced OOP Concepts
- **Class attributes vs. instance attributes**
- **Properties** with getters and setters
- **Special methods** (`__str__`, `__repr__`, `__del__`)
- **Class methods** and **static methods**
- **Instance tracking** and reference counting
- **Operator overloading** for comparisons

### When to Use Class vs. Instance Attributes
- **Instance attributes:** Unique to each object (e.g., `rectangle.width`)
- **Class attributes:** Shared across all instances (e.g., `Rectangle.number_of_instances`)

### Properties: The Pythonic Way
Instead of traditional getter/setter methods, Python uses the `@property` decorator:

```python
@property
def width(self):
    """Get the width."""
    return self._width

@width.setter
def width(self, value):
    """Set the width with validation."""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value
```

### Special Methods (Magic/Dunder Methods)
- `__init__`: Constructor (initialization)
- `__str__`: Human-readable string (for `print()`)
- `__repr__`: Developer-friendly string (for debugging)
- `__del__`: Destructor (cleanup when object is deleted)

### Class Methods vs. Static Methods
```python
class Rectangle:
    @classmethod
    def class_method(cls):
        """Has access to cls (the class itself)."""
        pass

    @staticmethod
    def static_method():
        """No access to self or cls. Just a utility function."""
        pass
```

---

## 📝 Task Breakdown

### 0. Simple rectangle
**Goal:** Create an empty `Rectangle` class.

**File:** `0-rectangle.py`

**Concepts:**
- Basic class definition
- The `pass` statement
- Class instantiation

**Example:**
```python
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))  # <class '0-rectangle.Rectangle'>
print(my_rectangle.__dict__)  # {}
```

**Key Points:**
- The class is empty (no attributes or methods)
- `pass` is a placeholder that does nothing
- `__dict__` shows the instance's attributes (empty for now)

---

## 🐍 Python Concepts Reference

### Class Definition
```python
class ClassName:
    """Class docstring."""
    pass
```

### Instance Creation
```python
obj = ClassName()  # Creates a new instance
```

### The `pass` Statement
`pass` is a null operation—a placeholder when a statement is syntactically required but you don't want to execute any code.

```python
class EmptyClass:
    pass  # Does nothing, but valid syntax

def empty_function():
    pass  # Does nothing
```

### The `__dict__` Attribute
Every Python object has a `__dict__` dictionary containing its attributes:

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__dict__)  # {'name': 'Buddy'}
```

### Module Docstrings
Every Python file should start with a module docstring explaining its purpose:

```python
#!/usr/bin/python3
"""Module that defines a Rectangle class.

This module contains the Rectangle class with methods for
calculating area, perimeter, and string representations.
"""
```

---

## 📋 Requirements

### General
- **Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS, Python 3.8.5
- **Style:** pycodestyle 2.7.*
- **Shebang:** All files must start with `#!/usr/bin/python3`
- **Newline:** All files must end with a newline
- **Executable:** All files must be executable (`chmod +x`)
- **README:** This file (mandatory)
- **No imports:** You cannot import any modules

### Code Style
- Follow PEP 8 / pycodestyle
- Use meaningful variable names
- Include docstrings for modules, classes, and methods
- Keep lines under 79 characters (or 99 for comments/docstrings)

---

## 🛠️ How to Use

### Running the Code
```bash
# Make file executable
chmod +x 0-rectangle.py

# Run test file
chmod +x 0-main.py
./0-main.py
```

### Style Checking
```bash
# Check a single file
pycodestyle 0-rectangle.py

# Check all Python files
pycodestyle *.py
```

### Interactive Testing
```bash
python3
>>> Rectangle = __import__('0-rectangle').Rectangle
>>> my_rectangle = Rectangle()
>>> print(type(my_rectangle))
<class '0-rectangle.Rectangle'>
>>> print(my_rectangle.__dict__)
{}
```

---

## 📖 Resources

### Official Documentation
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Properties](https://docs.python.org/3/library/functions.html#property)

### Tutorials
- **Object-Oriented Programming:** Core OOP principles in Python
- **Class and Instance Attributes:** Understanding attribute scope
- **Properties vs. Getters/Setters:** The Pythonic approach
- **Special Methods:** `__str__`, `__repr__`, `__del__`, etc.
- **Class Methods and Static Methods:** When and how to use them

### Style Guide
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [pycodestyle Documentation](https://pycodestyle.pycqa.org/)

---

## 💡 Best Practices

### Class Design
1. **Keep it simple:** Start with the basics, add complexity as needed
2. **Validate input:** Check types and values in setters
3. **Use properties:** Don't write manual getter/setter methods
4. **Document everything:** Module, class, and method docstrings
5. **Follow naming conventions:**
   - Classes: `UpperCamelCase`
   - Methods: `lowercase_with_underscores`
   - Private attributes: `_single_leading_underscore`

### Example Class Template
```python
#!/usr/bin/python3
"""Module documentation here."""


class MyClass:
    """Class documentation here.

    Attributes:
        class_attr (type): Description of class attribute
    """

    class_attr = "shared value"

    def __init__(self, param):
        """Initialize instance.

        Args:
            param (type): Description of parameter
        """
        self._param = param

    @property
    def param(self):
        """Get param."""
        return self._param

    @param.setter
    def param(self, value):
        """Set param with validation."""
        if not isinstance(value, int):
            raise TypeError("param must be an integer")
        self._param = value

    def __str__(self):
        """Human-readable string representation."""
        return f"MyClass with param={self._param}"

    def __repr__(self):
        """Developer-friendly string representation."""
        return f"MyClass({self._param})"
```

---

## 🎯 Common Patterns

### Property with Validation
```python
@property
def width(self):
    """Get width."""
    return self._width

@width.setter
def width(self, value):
    """Set width with validation."""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value
```

### String Representations
```python
def __str__(self):
    """For print() and str()."""
    return f"Rectangle({self.width}x{self.height})"

def __repr__(self):
    """For repr() and interactive console."""
    return f"Rectangle(width={self.width}, height={self.height})"
```

### Instance Counting
```python
class Rectangle:
    number_of_instances = 0  # Class attribute

    def __init__(self):
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```

---

## 🔍 Debugging Tips

### Check Instance Attributes
```python
print(obj.__dict__)  # Shows all instance attributes
```

### Check Class Attributes
```python
print(ClassName.__dict__)  # Shows class attributes and methods
```

### Verify Property Behavior
```python
# Test getter
print(obj.width)

# Test setter with valid value
obj.width = 10

# Test setter with invalid value (should raise error)
try:
    obj.width = -5
except ValueError as e:
    print(f"Caught error: {e}")
```

---

## ✅ Checklist Before Submission

- [ ] All files start with `#!/usr/bin/python3`
- [ ] All files end with a newline
- [ ] All files are executable (`chmod +x *.py`)
- [ ] Code follows pycodestyle (`pycodestyle *.py`)
- [ ] README.md exists and is complete
- [ ] All classes and methods have docstrings
- [ ] No unauthorized imports
- [ ] All tasks produce expected output
- [ ] Properties validate input correctly
- [ ] Special methods (`__str__`, `__repr__`, etc.) work as expected

---

## 📚 Quick Reference

### Special Methods
| Method | Purpose | Called By |
|--------|---------|-----------|
| `__init__` | Constructor | `obj = Class()` |
| `__str__` | String representation | `print(obj)`, `str(obj)` |
| `__repr__` | Developer representation | `repr(obj)`, console |
| `__del__` | Destructor | `del obj`, garbage collection |

### Attribute Types
| Type | Example | Scope |
|------|---------|-------|
| Instance | `self.width = 5` | Per instance |
| Class | `Rectangle.count = 0` | Shared by all instances |
| Private | `self._private = 1` | Convention (not enforced) |

### Method Types
| Type | Decorator | First Parameter | Access |
|------|-----------|-----------------|--------|
| Instance | None | `self` | Instance and class data |
| Class | `@classmethod` | `cls` | Class data only |
| Static | `@staticmethod` | None | No access to instance/class |

---

## 🎓 Learning Path

1. **Task 0:** Understand basic class structure
2. **Future Tasks:** Will add:
   - `__init__` with width and height
   - Properties with validation
   - Area and perimeter methods
   - String representations (`__str__`, `__repr__`)
   - Instance counting
   - Comparison operators

---

Happy coding! 🐍

**Pro Tip:** Before moving to the next task, make sure you fully understand the current one. OOP concepts build on each other!

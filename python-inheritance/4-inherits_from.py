#!/usr/bin/python3
"""Module that checks if an object inherits from a class.

This module provides a function to determine if an object is an instance
of a class that inherited from a specified class, excluding the class itself.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a_class.

    This function returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    but not if it's an exact instance of the specified class itself.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
              (but not a_class itself), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or subclass.

This module provides a function to determine if an object is an instance
of a specified class or any class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclasses.

    This function returns True if the object is an instance of the class
    or if it's an instance of a class that inherits from the specified class.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Module that checks if an object is an exact instance of a class.

This module provides a function to determine if an object is exactly
an instance of a specified class, without considering subclasses.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    This function returns True only if the object is an exact instance
    of the class, not if it's an instance of a subclass.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class,
              False otherwise.
    """
    return type(obj) is a_class

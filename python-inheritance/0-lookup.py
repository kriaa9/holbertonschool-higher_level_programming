#!/usr/bin/python3
"""Module that provides a lookup function for object attributes and methods.

This module contains a function to return all available attributes and
methods of any object, which is useful for introspection and debugging.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object (class, instance, built-in type, etc.)

    Returns:
        list: A sorted list of strings representing all available attributes
              and methods of the object, including inherited ones from parent
              classes and object.
    """
    return dir(obj)

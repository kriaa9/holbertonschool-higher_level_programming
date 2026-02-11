#!/usr/bin/python3
"""Module for converting class instances to dictionaries."""


def class_to_json(obj):
    """
    Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        Dictionary containing all attributes of the object.
    """
    return obj.__dict__

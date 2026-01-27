#!/usr/bin/python3
"""
This module provides a function that adds 2 integers.
It handles integer and float inputs, casting floats to integers
before addition, and raises TypeErrors for invalid inputs.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    Returns:
        The addition of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

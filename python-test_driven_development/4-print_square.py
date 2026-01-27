#!/usr/bin/python3
"""
This module provides a function that prints a square using the '#' character.
It validates that the size is a positive integer.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

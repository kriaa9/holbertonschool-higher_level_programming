#!/usr/bin/python3
"""Provide `islower(c)` to check if a character is lowercase.

The function returns True if `c` is in the ASCII lowercase range 'a'..'z'.
No imports are used; the check relies on `ord()` to get the code point.
"""


def islower(c):
    """Check if character c is lowercase.

    Args:
        c: A single character string

    Returns:
        True if c is lowercase (a-z)
        False otherwise
    """
    # ASCII lowercase letters have codes 97 ('a') through 122 ('z')
    return ord(c) >= 97 and ord(c) <= 122

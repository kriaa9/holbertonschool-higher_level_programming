#!/usr/bin/python3
def islower(c):
    """Check if character c is lowercase.

    Args:
        c: A single character string

    Returns:
        True if c is lowercase (a-z)
        False otherwise
    """
    return ord(c) >= 97 and ord(c) <= 122

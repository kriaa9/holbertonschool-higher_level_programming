#!/usr/bin/python3
"""Provide `uppercase(str)` to print a string in uppercase.

Each character is examined. If it is lowercase (ASCII 97..122), it is
converted by subtracting 32 from its code point; otherwise it is printed
as-is. The function prints the transformed string followed by a newline.
"""
def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str: Input string to convert to uppercase

    Prints:
        The string in uppercase
    """
    # Single loop over the input string; no imports used.
    for c in str:
        print("{}".format(chr(ord(c) - 32) if ord(c) >= 97 and
                          ord(c) <= 122 else c), end='')
    print()

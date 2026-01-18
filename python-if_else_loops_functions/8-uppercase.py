#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str: Input string to convert to uppercase

    Prints:
        The string in uppercase
    """
    for c in str:
        print("{}".format(chr(ord(c) - 32) if ord(c) >= 97 and
                          ord(c) <= 122 else c), end='')
    print()

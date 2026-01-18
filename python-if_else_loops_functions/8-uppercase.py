#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line.

    Args:
        str: Input string to convert to uppercase

    Prints:
        The string in uppercase
    """
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            # Lowercase letter: convert to uppercase
            print("{}".format(chr(ord(c) - 32)), end='')
        else:
            # Not lowercase: print as is
            print("{}".format(c), end='')
    print()

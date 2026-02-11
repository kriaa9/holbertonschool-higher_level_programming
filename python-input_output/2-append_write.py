#!/usr/bin/python3
"""Module for appending to files."""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF8) and return characters added.

    Args:
        filename: The name of the file to append to.
        text: The text to append to the file.

    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

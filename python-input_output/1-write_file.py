#!/usr/bin/python3
"""Module for writing to files."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return characters written.

    Args:
        filename: The name of the file to write to.
        text: The text to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Module for reading files."""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print it to stdout.

    Args:
        filename: The name of the file to read (default empty string).
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""Module for inserting text after specific lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename: The name of the file to modify.
        search_string: The string to search for in each line.
        new_string: The string to insert after matching lines.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

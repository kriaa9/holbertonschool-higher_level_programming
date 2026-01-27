#!/usr/bin/python3
"""
This module provides a function to format text indentation.
It inserts double newlines after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".:?":
            print(buffer.strip())
            print()
            buffer = ""

    if len(buffer.strip()) > 0:
        print(buffer.strip(), end="")

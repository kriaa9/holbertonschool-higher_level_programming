#!/usr/bin/python3
"""Module for saving objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to save.
        filename: The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

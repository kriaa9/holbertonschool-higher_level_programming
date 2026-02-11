#!/usr/bin/python3
"""Module for loading objects from JSON files."""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename: The name of the JSON file to load from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

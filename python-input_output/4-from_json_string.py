#!/usr/bin/python3
"""Module for JSON string to object conversion."""
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
        my_str: The JSON string to deserialize.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

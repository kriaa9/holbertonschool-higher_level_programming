#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save to data.json.

    Args:
        csv_filename: The filename of the input CSV file.

    Returns:
        True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as f:
            json.dump(data, f)

        return True
    except FileNotFoundError:
        return False

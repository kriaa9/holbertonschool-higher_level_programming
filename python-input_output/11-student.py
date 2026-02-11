#!/usr/bin/python3
"""Module defining a Student class with serialization/deserialization."""


class Student:
    """A class that defines a student with reload capability."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs: Optional list of attribute names to retrieve.

        Returns:
            Dictionary containing the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.

        Args:
            json: Dictionary with attribute names as keys and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

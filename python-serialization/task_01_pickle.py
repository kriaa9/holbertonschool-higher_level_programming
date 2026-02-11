#!/usr/bin/env python3
"""Module for pickling custom classes."""
import pickle


class CustomObject:
    """A custom class that supports serialization with pickle."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name: A string representing the name.
            age: An integer representing the age.
            is_student: A boolean indicating student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename: The filename to save the serialized object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return a CustomObject from a file.

        Args:
            filename: The filename to load the object from.

        Returns:
            A CustomObject instance, or None on error.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

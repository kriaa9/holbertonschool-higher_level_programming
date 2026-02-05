#!/usr/bin/python3
"""Module that defines an improved base geometry class.

This module contains the BaseGeometry class with an area method that
raises an exception, and an integer_validator method for validating
integer parameters.
"""


class BaseGeometry:
    """A base geometry class.

    This class serves as a foundation for geometry-related classes.
    It includes an area method that must be implemented by subclasses,
    and a validator method for integer parameters.
    """

    def area(self):
        """Calculate the area of the geometry.

        This method must be implemented by subclasses.

        Raises:
            Exception: Always raises an exception indicating that
                      the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Module that defines an improved base geometry class.

This module contains the BaseGeometry class with an area method that
raises an exception, serving as a template for subclasses to implement.
"""


class BaseGeometry:
    """A base geometry class.

    This class serves as a foundation for geometry-related classes.
    It includes an area method that must be implemented by subclasses.
    """

    def area(self):
        """Calculate the area of the geometry.

        This method must be implemented by subclasses.

        Raises:
            Exception: Always raises an exception indicating that
                      the method is not implemented.
        """
        raise Exception("area() is not implemented")

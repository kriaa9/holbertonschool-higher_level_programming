#!/usr/bin/python3
"""Define a Rectangle class with validated width and height."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with private width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

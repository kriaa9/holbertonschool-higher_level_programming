#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with validated size.

        Args:
            size: The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
"""Module that defines a Rectangle class with customizable print symbol.

This module contains a Rectangle class with private attributes,
property getters/setters with validation, methods to calculate
area and perimeter, string representations, a destructor,
instance counting, and customizable print symbol.
"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle (private).
        height (int): The height of the rectangle (private).
        number_of_instances (int): Number of Rectangle instances (class attr).
        print_symbol: Symbol used for string representation (class attr).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Increments the number_of_instances class attribute.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        If width or height is 0, the perimeter is 0.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)),
                 or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle.

        Uses the print_symbol attribute to draw the rectangle.
        If width or height is 0, returns an empty string.

        Returns:
            str: A rectangle drawn with print_symbol, one row per line.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for row in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            if row < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Return a string representation of the rectangle.

        This representation can be used with eval() to create a new
        instance with the same width and height.

        Returns:
            str: A string in the format Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the rectangle instance is deleted.

        Decrements the number_of_instances class attribute.
        This destructor is called automatically when the instance is
        garbage collected or explicitly deleted with del statement.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

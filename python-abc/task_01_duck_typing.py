#!/usr/bin/env python3
"""Module defining shapes using abstract base classes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape.

    This class defines the interface for all shape subclasses,
    requiring them to implement area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Abstract method that should return the area of the shape.

        This method must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that should return the perimeter of the shape.

        This method must be implemented by all subclasses.
        """
        pass


class Circle(Shape):
    """Circle class that inherits from Shape.

    Represents a circle and implements the area and perimeter methods.
    """

    def __init__(self, radius):
        """Initialize a Circle with a given radius.

        Args:
            radius: The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle (π * r²).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle (2 * π * r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape.

    Represents a rectangle and implements the area and perimeter methods.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    This function relies on duck typing - it expects the passed object
    to have area() and perimeter() methods, but doesn't check the type.

    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

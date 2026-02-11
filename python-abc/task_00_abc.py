#!/usr/bin/env python3
"""Module defining an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    This class defines the interface for all animal subclasses,
    requiring them to implement the sound method.
    """

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound the animal makes.

        This method must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """Dog class that inherits from Animal.

    Represents a dog and implements the sound method.
    """

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: The string "Bark"
        """
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal.

    Represents a cat and implements the sound method.
    """

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: The string "Meow"
        """
        return "Meow"

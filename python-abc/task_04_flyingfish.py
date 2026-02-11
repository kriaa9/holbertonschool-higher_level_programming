#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance in Python.

This module contains Fish, Bird, and FlyingFish classes to explore
how Python handles multiple inheritance and method resolution order (MRO).
"""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat information."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat information."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish.

    Inherits from both Fish and Bird, demonstrating multiple inheritance.
    The MRO is: FlyingFish -> Fish -> Bird -> object
    """

    def fly(self):
        """Print flying behavior for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat information for flying fish."""
        print("The flying fish lives both in water and the sky!")

#!/usr/bin/env python3
"""
Module demonstrating mixin classes in Python.

This module contains SwimMixin, FlyMixin, and Dragon classes to explore
how mixins can be used to compose behaviors without rigid inheritance.
"""


class SwimMixin:
    """Mixin class that provides swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon.

    Inherits from SwimMixin and FlyMixin, demonstrating how mixins
    can be combined to give objects multiple capabilities.
    """

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")

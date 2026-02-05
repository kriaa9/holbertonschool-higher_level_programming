#!/usr/bin/python3
"""Module that defines a custom list class with sorting capability.

This module contains the MyList class that inherits from the built-in
list class and adds a method to print a sorted version of the list
without modifying the original list.
"""


class MyList(list):
    """A list class with additional sorting functionality.

    This class inherits from the built-in list class and provides a
    method to print the list in sorted order without modifying the
    original list.
    """

    def print_sorted(self):
        """Print the list sorted in ascending order.

        This method prints a sorted version of the list without modifying
        the original list. Assumes all elements are integers.

        Handles empty lists by printing an empty list.

        Returns:
            None
        """
        print(sorted(self))

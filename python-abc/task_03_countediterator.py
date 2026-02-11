#!/usr/bin/env python3
"""Module defining a CountedIterator class that tracks iteration count."""


class CountedIterator:
    """An iterator wrapper that counts the number of items iterated.

    This class extends the functionality of a standard iterator by keeping
    track of how many items have been fetched during iteration.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, etc.).
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself.

        Returns:
            self: The iterator object.
        """
        return self

    def __next__(self):
        """Fetch the next item and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated.

        Returns:
            int: The current count of items iterated.
        """
        return self.count

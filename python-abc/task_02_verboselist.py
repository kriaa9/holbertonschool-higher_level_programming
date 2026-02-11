#!/usr/bin/env python3
"""Module defining a VerboseList class that extends the built-in list."""


class VerboseList(list):
    """A list subclass that prints notifications for modifications.

    This class extends the built-in list class and provides verbose
    output whenever items are added or removed from the list.
    """

    def append(self, item):
        """Add an item to the end of the list with notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with multiple items and print notification.

        Args:
            iterable: An iterable of items to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list with notification.

        Args:
            item: The item to remove from the list.

        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at the given index with notification.

        Args:
            index: The index of the item to pop (default: -1, last item).

        Returns:
            The item that was popped from the list.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

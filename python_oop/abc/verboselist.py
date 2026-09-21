#!/usr/bin/env python3
"""Module that defines the VerboseList class.

This module demonstrates extending a Python built-in class,
adding notification messages to the list-modifying methods
while retaining the original functionality through super().
"""


class VerboseList(list):
    """Represent a list that announces its own modifications.

    Inherits from the built-in list class and overrides the
    methods that modify the list to print a notification
    message whenever an item is added or removed.
    """

    def append(self, item):
        """Add an item to the end of the list and announce it.

        Args:
            item: the item to add to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with items and announce the count.

        Args:
            iterable: the iterable of items to add to the list.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and announce it first.

        Args:
            item: the item to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and announce it first.

        Args:
            index (int): the index of the item to pop. Defaults
                to -1, popping the last item.

        Returns:
            the popped item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

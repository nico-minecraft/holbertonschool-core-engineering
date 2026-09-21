#!/usr/bin/env python3
"""Module that defines a Square class with an area method."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

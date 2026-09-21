#!/usr/bin/env python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the square.
        """
        self.__size = size

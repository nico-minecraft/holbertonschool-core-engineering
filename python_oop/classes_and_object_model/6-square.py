#!/usr/bin/env python3
"""Module that defines a Square class with a __str__ method."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): the size of the square. Defaults to 0.
            position (tuple): the position of the square.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): the new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): the new position of the square, as a
                tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive
                integers.
        """
        is_valid = (
            isinstance(value, tuple) and len(value) == 2 and
            all(isinstance(coord, int) and coord >= 0 for coord in value)
        )
        if not is_valid:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #.

        If size is 0, print an empty line. The square is offset by
        position: position[0] adds leading spaces on each row and
        position[1] adds blank lines above the square.
        """
        print(self)

    def __str__(self):
        """Return the string representation of the square."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines += [row] * self.__size
        return "\n".join(lines)

#!/usr/bin/env python3
"""Module that defines the Square class.

This module provides a Square class that inherits from
Rectangle, reusing its area computation and string
representation since a square is a specialized rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a specialized rectangle.

    Inherits from Rectangle, since a square is a rectangle
    whose width and height are equal.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square's sides.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

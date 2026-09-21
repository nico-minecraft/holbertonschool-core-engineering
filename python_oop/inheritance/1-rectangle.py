#!/usr/bin/env python3
"""Module that defines the Rectangle class.

This module provides a Rectangle class that inherits from
BaseGeometry, reusing its validation logic through inheritance.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle defined by its width and height.

    Inherits from BaseGeometry to reuse the integer_validator
    method for validating the rectangle's dimensions.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

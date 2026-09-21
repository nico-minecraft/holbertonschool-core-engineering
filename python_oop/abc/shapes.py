#!/usr/bin/env python3
"""Module that defines the Shape abstract class and its subclasses.

This module demonstrates the use of Python's abc module together
with duck typing: shape_info works with any object that provides
area and perimeter methods, regardless of its actual class.
"""
ABC = __import__('abc').ABC
abstractmethod = __import__('abc').abstractmethod
pi = __import__('math').pi


class Shape(ABC):
    """Represent an abstract shape.

    This class defines a common interface for all shapes
    through the abstract area and perimeter methods. Subclasses
    must provide their own concrete implementation of both.
    """

    @abstractmethod
    def area(self):
        """Compute the area of the shape.

        This method is abstract and must be implemented by any
        concrete subclass of Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape.

        This method is abstract and must be implemented by any
        concrete subclass of Shape.
        """
        pass


class Circle(Shape):
    """Represent a circle, a concrete subclass of Shape."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (float): the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Compute the area of the circle.

        Returns:
            float: the area of the circle.
        """
        return pi * self.radius ** 2

    def perimeter(self):
        """Compute the perimeter of the circle.

        Returns:
            float: the perimeter (circumference) of the circle.
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle, a concrete subclass of Shape."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (float): the width of the rectangle.
            height (float): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            float: the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Compute the perimeter of the rectangle.

        Returns:
            float: the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape.

    This function relies on duck typing: it calls the area and
    perimeter methods of the given object without checking its
    type, so it works with any object that provides them.

    Args:
        shape: an object that provides area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

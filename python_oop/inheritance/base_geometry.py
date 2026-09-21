#!/usr/bin/env python3
"""Module that defines the BaseGeometry class.

This module provides a foundational class for geometric shapes,
offering shared functionality such as parameter validation that
subclasses can reuse.
"""


class BaseGeometry:
    """Represent a foundational concept for geometric shapes.

    This class defines behavior that other shape classes will
    build upon, such as a common area interface and a reusable
    integer validator.
    """

    def area(self):
        """Compute the area of the geometric shape.

        This base implementation does not define how the area
        should be calculated, since different shapes compute
        their area differently. Subclasses must override this
        method with their own implementation.

        Raises:
            Exception: always, since this is not implemented here.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a valid positive integer.

        Args:
            name (str): the name of the parameter being validated.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

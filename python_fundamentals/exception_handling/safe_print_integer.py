#!/usr/bin/env python3
"""Module that defines a safe integer printing function."""


def safe_print_integer(value):
    """Print value formatted as an integer, followed by a new line.

    Args:
        value: the value to print.

    Returns:
        bool: True if value is an integer and was printed,
            False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

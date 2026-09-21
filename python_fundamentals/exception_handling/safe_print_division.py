#!/usr/bin/env python3
"""Module that defines a safe integer division function."""


def safe_print_division(a, b):
    """Divide a by b, always printing the result via finally.

    Args:
        a: the dividend.
        b: the divisor.

    Returns:
        The result of the division, or None if an exception occurs.
    """
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

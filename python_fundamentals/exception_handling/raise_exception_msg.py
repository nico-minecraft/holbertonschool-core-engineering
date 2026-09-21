#!/usr/bin/env python3
"""Module that defines a function raising a NameError with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError with the given message.

    Args:
        message (str): the message attached to the NameError.
    """
    raise NameError(message)

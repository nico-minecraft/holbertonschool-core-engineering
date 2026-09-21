#!/usr/bin/env python3
"""Module that defines a safe list of integers printing function."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list that are integers.

    Non-integer elements are skipped. Elements are printed on the
    same line followed by a new line.

    Args:
        my_list (list): the list to print elements from.
        x (int): the number of elements to consider.

    Returns:
        int: the number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

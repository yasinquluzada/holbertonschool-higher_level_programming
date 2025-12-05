#!/usr/bin/python3
"""Module that defines print_reversed_list_integer."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order.

    Args:
        my_list (list): list of integers.
    """
    if my_list is None:
        return

    for value in reversed(my_list):
        print("{:d}".format(value))

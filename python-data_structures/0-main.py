#!/usr/bin/python3
"""Module that defines print_list_integer function."""


def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line.

    Args:
        my_list (list): List of integers.
    """
    for number in my_list:
        print("{:d}".format(number))

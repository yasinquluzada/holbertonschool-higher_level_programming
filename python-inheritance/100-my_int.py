#!/usr/bin/python3
"""Defines a rebel integer type with inverted equality and inequality."""


class MyInt(int):
    """An int subclass that inverts == and != comparisons."""

    def __eq__(self, other):
        """Returns the inverted result of int equality."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Returns the inverted result of int inequality."""
        return int.__eq__(self, other)

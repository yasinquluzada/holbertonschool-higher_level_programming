#!/usr/bin/python3
"""Defines a list subclass that can display a sorted view of its items."""


class MyList(list):
    """Extends the built-in list type with a method that prints a sorted view."""

    def print_sorted(self):
        """Prints the items in ascending order without changing the list."""
        print(sorted(self))

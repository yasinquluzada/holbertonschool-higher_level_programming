#!/usr/bin/python3
"""Lists an object's available attributes and methods."""


def lookup(obj):
    """Return the list of names of attributes and methods on obj."""
    return dir(obj)

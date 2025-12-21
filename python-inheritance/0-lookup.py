#!/usr/bin/python3
"""Provides a function that lists an object's available attributes and methods."""


def lookup(obj):
    """Return the list of names of attributes and methods available on obj."""
    return dir(obj)

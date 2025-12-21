#!/usr/bin/python3
"""Defines inherits_from to test strict inheritance-based instances."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class, else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class

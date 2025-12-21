#!/usr/bin/python3
"""Defines a function that checks for an object's exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False."""
    return type(obj) is a_class

#!/usr/bin/python3
"""Defines BaseGeometry with validation helpers."""


class BaseGeometry:
    """Provides basic geometry utilities and a common validation method."""

    def area(self):
        """Raises an exception because area is not defined at this level."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer with the given name."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

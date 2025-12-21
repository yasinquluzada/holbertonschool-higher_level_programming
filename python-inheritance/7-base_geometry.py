#!/usr/bin/python3
"""Defines BaseGeometry with strict integer validation."""


class BaseGeometry:
    """Provides geometry behaviors and strict input validation utilities."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than zero."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

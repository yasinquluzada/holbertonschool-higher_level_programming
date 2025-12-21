#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area and strict integer validation."""


class BaseGeometry:
    """Provides base geometry behaviors and strict input validation."""

    def area(self):
        """Raises an exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a strictly positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

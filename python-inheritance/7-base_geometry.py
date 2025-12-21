#!/usr/bin/python3
"""Defines BaseGeometry with area and integer validation utilities."""


class BaseGeometry:
    """Provides geometry base behaviors and common validations."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

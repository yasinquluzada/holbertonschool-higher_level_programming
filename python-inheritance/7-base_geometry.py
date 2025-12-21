#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area and strict integer validation."""


class BaseGeometry:
    """Provides basic geometry behaviors and input validation utilities."""

    def area(self):
        """Raises an exception because the area behavior is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than zero."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

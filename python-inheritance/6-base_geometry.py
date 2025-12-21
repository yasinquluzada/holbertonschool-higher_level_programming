#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Provides a base geometry class with an area placeholder."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

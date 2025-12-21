#!/usr/bin/python3
"""Defines a Rectangle class that validates dimensions using BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated private width and height."""

    def __init__(self, width, height):
        """Initializes a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

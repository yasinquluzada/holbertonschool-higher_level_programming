#!/usr/bin/python3
"""Defines a Rectangle based on validated width and height."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle defined by its validated dimensions."""

    def __init__(self, width, height):
        """Initializes the rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

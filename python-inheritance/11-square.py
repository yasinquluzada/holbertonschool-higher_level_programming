#!/usr/bin/python3
"""Defines a Square that inherits from Rectangle and validates its size."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with a private validated size value."""

    def __init__(self, size):
        """Initializes the square with a validated positive integer size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the printable description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

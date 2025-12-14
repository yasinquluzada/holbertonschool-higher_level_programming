#!/usr/bin/python3
"""Rectangle module.

This module defines a Rectangle class with validated dimensions and
a live instance counter.
"""


class Rectangle:
    """Define a rectangle and track how many live instances exist."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width after validating type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height after validating type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute and return the rectangle perimeter, or 0 if empty."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a printable shape of the rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a recreatable string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the instance, update the counter, and print a message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

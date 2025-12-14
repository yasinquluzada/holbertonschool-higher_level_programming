#!/usr/bin/python3
"""Defines a Rectangle class that supports string and repr representations."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width after validating its type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height after validating its type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable rectangle using the '#' character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = "#" * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return a string that can recreate the instance using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

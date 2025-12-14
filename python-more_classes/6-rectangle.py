#!/usr/bin/python3
"""Defines a Rectangle class that tracks how many instances exist and supports string representations."""


class Rectangle:
    """Represents a rectangle with validated width and height, and counts active instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height values."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating its type and value."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating its type and value."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if either dimension is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return an informal string drawing of the rectangle using the '#' character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return an official string representation that can recreate the instance with eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Handle instance deletion by updating instance count and printing a farewell message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

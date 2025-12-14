#!/usr/bin/python3
"""This module defines a Rectangle class with validation, display, and helpers."""


class Rectangle:
    """Represent a rectangle defined by width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the rectangle width."""
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
        """Return the rectangle height."""
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
        """Return an informal string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join([line for _ in range(self.__height)])

    def __repr__(self):
        """Return an official string representation that can recreate the instance."""
        return "{}({}, {})".format(self.__class__.__name__, self.__width, self.__height)

    def __del__(self):
        """Handle instance deletion and update the instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area, or rect_1 if equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

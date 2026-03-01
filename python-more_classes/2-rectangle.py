#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, and perimeter."""


class Rectangle:
    """Represents a rectangle defined by its width and height."""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle.

        Think of this like creating a real rectangle toy.
        You can give it a width and a height, or leave them as 0.

        Args:
            width (int): the rectangle width
            height (int): the rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width (read it)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width (change it), but only if it is valid."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height (read it)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height (change it), but only if it is valid."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle.

        Area means: how many small 1x1 squares can fit inside.
        Formula: width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        Perimeter means: the length around the rectangle border.
        Formula: 2 * (width + height)

        Special rule (task says):
        If width == 0 or height == 0, perimeter must be 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

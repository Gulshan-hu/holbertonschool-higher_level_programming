#!/usr/bin/python3
"""Defines a Square class with getter and setter."""


class Square:
    """Square class with validated private size attribute."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size  # setter istifadə olunur

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return current square area."""
        return self.__size * self.__size

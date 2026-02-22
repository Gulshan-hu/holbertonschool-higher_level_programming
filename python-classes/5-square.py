#!/usr/bin/python3
"""Defines a Square class with printing capability."""


class Square:
    """Square class with validated private size attribute."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size

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

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

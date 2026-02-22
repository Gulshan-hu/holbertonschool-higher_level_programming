#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Square class with validated private size attribute."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

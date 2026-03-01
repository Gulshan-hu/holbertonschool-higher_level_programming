#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square (> 0)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the square description.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)

#!/usr/bin/python3
"""BaseGeometry module: area() and integer_validator()."""


class BaseGeometry:
    """Geometry base class."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an int > 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

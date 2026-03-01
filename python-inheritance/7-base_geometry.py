#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

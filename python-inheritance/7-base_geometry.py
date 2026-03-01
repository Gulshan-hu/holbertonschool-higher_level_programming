#!/usr/bin/python3
"""BaseGeometry modulu üçün docstring"""


class BaseGeometry:
    """BaseGeometry sinfi"""

    def area(self):
        """area metodu implementasiya olunmayıb"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyəri yoxlayır: integer və > 0 olmalıdır"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

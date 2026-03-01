#!/usr/bin/python3
"""
7-base_geometry modulu
Bu modul BaseGeometry sinfini təyin edir.
"""


class BaseGeometry:
    """BaseGeometry sinfi"""

    def area(self):
        """area() metodu implementasiya olunmayıb"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyəri integer və 0-dan böyük olub-olmamasına görə yoxlayır.
        Args:
            name (str): Parametrin adı (həmişə string).
            value (int): Yoxlanılacaq dəyər.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

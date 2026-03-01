#!/usr/bin/python3
"""
7-base_geometry modulu
Bu modul BaseGeometry sinfini saxlayır.
"""


class BaseGeometry:
    """BaseGeometry sinfi"""

    def area(self):
        """area() metodu hələ tətbiq olunmayıb"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyəri yoxlayır (integer və > 0 olmalıdır).
        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

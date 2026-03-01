#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul"""


class BaseGeometry:
    """BaseGeometry sinfi"""

    def area(self):
        """area() metodunun implementasiya olunmadığını bildirir"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və 0-dan böyük olmasını yoxlayır
        Args:
            name (str): Parametrin adı (həmişə string fərz edilir)
            value (int): Yoxlanılacaq dəyər
        Raises:
            TypeError: value integer deyilsə
            ValueError: value <= 0 olarsa
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

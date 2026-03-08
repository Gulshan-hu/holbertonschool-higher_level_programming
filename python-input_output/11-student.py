#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student instance"""
        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                if type(key) is str and key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

#!/usr/bin/env python3
"""Shapes, interfaces, and duck typing with ABCs."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class that defines the Shape interface."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete Circle implementation of Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Concrete Rectangle implementation of Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.
    No isinstance checks: relies on shape having area() and perimeter().
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

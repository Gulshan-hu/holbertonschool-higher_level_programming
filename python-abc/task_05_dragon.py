#!/usr/bin/env python3
"""Mixins example: SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon inherits abilities from both mixins."""

    def roar(self):
        print("The dragon roars!")

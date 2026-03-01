#!/usr/bin/env python3
"""Extending Python list with notifications."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = 0
        # Try to get length without consuming iterators
        try:
            count = len(iterable)
        except TypeError:
            # iterable might be a generator; count by iterating once
            iterable = list(iterable)
            count = len(iterable)

        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]  # may raise IndexError like normal list
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

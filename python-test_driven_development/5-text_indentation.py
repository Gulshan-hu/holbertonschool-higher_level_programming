#!/usr/bin/python3
"""
Module that contains text_indentation function.
"""


def text_indentation(text=None):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"
    line = ""

    for ch in text:
        line += ch
        if ch in chars:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")

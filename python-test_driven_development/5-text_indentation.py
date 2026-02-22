#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
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

#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    start = 0

    while i < len(text):
        if text[i] in ".?:":
            line = text[start:i + 1].strip()
            print(line)
            print()
            start = i + 1
        i += 1

    if start < len(text):
        line = text[start:].strip()
        if line:
            print(line, end="")

#!/usr/bin/python3
"""Define an append_write function"""


def append_write(filename="", text=""):
    """Append a string to the end of a file
    Args:
        filename: name of file
        text: appended string
    """
    with open(filename, "a", encoding="UTF8") as f:
        return (f.write(text))

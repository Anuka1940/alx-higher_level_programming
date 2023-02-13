#!/usr/bin/python3
"""Define write_file"""


def write_file(filename="", text=""):
    """A function that write in a file
    Args:
        filename: name of the file
        text: the written string
        return: Number of appended character
    """
    with open(filename, "w", encoding="UTF8") as f:
        return (f.write(text))

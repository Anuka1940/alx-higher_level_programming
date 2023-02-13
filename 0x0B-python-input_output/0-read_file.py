#!/usr/bin/python3
"""define a method called read_file"""


def read_file(filename=""):
    """opens a file and return it content in stdout format"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")

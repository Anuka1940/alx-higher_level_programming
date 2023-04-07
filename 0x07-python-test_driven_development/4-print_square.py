#!/usr/bin/python3
""" This Module contain a function called "print_square"
"""
def print_square(size):
    """ It print a square of size "size" """
    if type(size) not in [int]:
        raise TypeError("size must be an interger")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an interger")
    for i in  range(size):
        print('#' * size)

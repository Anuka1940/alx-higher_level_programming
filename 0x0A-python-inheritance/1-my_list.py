#!/usr/bin/python3
""" Define a sub class from super class list"""


class MyList(list):
    """sub class of super class"""
    def __init__(self):
        """initialize the object"""
        list.__init__(self)

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

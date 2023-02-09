#!/usr/bin/python3
""" Define a funtion that return True if an obj is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """compare if obj is from a_class

    return True or False"""
    return isinstance(obj, a_class)

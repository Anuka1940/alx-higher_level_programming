#!/usr/bin/python3
""" This module define a fuction that check the class of an obj
"""


def is_same_class(obj, a_class):
    """check for type of obj with a_class

    return True if same and False other wise"""
    if type(obj) is a_class:
        return True
    else:
        return False

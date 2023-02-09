#!/usr/bin/python3
""" Define a funtion check if obj is inherited from the specified class"""


def inherits_from(obj, a_class):
    """ Return True if obj is  is an instance of a class that
    inherited from class,else return False"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False

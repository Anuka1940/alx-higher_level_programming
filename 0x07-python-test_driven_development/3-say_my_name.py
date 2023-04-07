#!/usr/bin/python3
"""This module has a funtion called 'say_my_name'
"""
def say_my_name(first_name, last_name=""):
    """Print the inputed name """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

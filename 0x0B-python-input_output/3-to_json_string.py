#!/usr/bin/pyton3
"""Define from_json_string function"""
import json


def to_json_string(my_obj):
    """Represent a json string
    Arg:
    my_str: object to be converted
    return: a string of the obj
    """
    return json.dumps(my_obj)

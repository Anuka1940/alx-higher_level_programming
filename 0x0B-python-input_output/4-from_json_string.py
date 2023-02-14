#!/usr/bin/python3
import json
"""Define from_json_string function"""


def from_json_string(my_str):
    """Represent a json string
    Arg:
    my_str: object to converted
    return: a string of the obj
    """
    return json.loads(my_str)

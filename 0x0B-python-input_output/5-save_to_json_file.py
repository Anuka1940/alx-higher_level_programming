#!/usr/bin/python3
import jsonn
""" Define a save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """ It write an object to a text file using JSON representation,
    Args:
        my_obj: The writen object
        filename: The json represntaion of in obj
        return: it returns a file format of the json representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)

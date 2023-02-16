#!/usr/bin/python3
""" Define a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """ It write an object to a text file using JSON representation,
    Args:
        my_obj: The writen object
        filename: The json represntaion of in obj
        return: it returns a file format of the json representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        my_object = json.dump(my_obj, f)
        return my_object

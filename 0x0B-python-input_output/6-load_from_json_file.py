#!/usr/bin/python3
""" Define load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename: name of the json file to create the object from
        return: return an object form of a "JSON file"
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

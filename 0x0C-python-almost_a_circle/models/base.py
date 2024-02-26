#!/usr/bin/python3
"""Module defining the Base class."""

class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""Define subclass that inherit class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a subclass rectangle"""

    def __init__(self, width, height):
        """initialize a rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

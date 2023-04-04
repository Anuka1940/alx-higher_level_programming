#!/usr/bin/python3
"""Define a lass called Rectangle"""


class Rectangle:
    """Represent Class Declarations"""

    def __init__(self, width=0, height=0):
        """initializes private instances"""
        self.__width = width
        self.__height = height

    def __str__(self):
        if self.__width == 0:
            print()
        if self.__height == 0:
            print()
        for i in range(self.__height):
            result = '#' * self.__width
        return "{}".format(result)

    @property
    def width(self):
        """returns retieved private instances"""
        return self.__width

    @width.setter
    def width(self, value):
        """return set variable"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
                self.__width = value

    @property
    def height(self):
        """returns retieved private instances"""
        return self.__height

    @height.setter
    def height(self, value):
         """return set variable"""
         if type(value) != int:
             raise TypeError("height must be an integer")
         if value < 0:
            raise ValueError("height must be >= 0")
         else:
             self.__height = value

    def area(self):
        """return area of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * self.__width)

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((2 * self.__height) + (2 * self.__width))

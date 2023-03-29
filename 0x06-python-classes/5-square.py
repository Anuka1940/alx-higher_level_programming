#!/usr/bin/python3
""" Define a class square"""


class Square:
    '''define a class'''
    def __init__(self, size=0):
        '''initialize attribute

        agrs:
            size: size of square
            '''
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''return the area of a sqaure'''
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print('#' * self.size)

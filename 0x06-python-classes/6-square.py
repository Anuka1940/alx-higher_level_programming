#!/usr/bin/python3
""" Define a class square"""


class Square:
    '''define a class'''
    def __init__(self, size=0, position=(0, 0)):
        '''initialize attribute

        agrs:
            size: size of square
            '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''return the area of a sqaure'''
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        if self.position[1] > 0:
            print()
        for i in range(self.size):
            print("{}{}".format('_' * self.position[0], '#' * self.size))

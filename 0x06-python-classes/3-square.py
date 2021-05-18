#!/usr/bin/python3
"""Square class defined by size and"""


class Square:
    """size validation"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    """public class return area of square"""

    def area(self):
        return (self.__size ** 2)

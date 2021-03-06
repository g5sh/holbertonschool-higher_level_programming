#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("ize must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

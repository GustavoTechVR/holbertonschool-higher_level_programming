#!/usr/bin/python3
"""Module that defines a Square class with private size attribute"""


class Square:
    """Square class with a private size attribute"""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

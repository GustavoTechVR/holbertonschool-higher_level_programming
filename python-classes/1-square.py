#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute"""


class Square:
    """Square class with a private size attribute"""

    def __init__(self, size):
        """Initializes a new Square instance

        Args:
            size (int): The size of the square

        """
        self.__size = size

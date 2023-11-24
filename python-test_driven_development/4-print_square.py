#!/usr/bin/python3
"""Module that defines the print_square function"""


def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
        size (int): The size length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

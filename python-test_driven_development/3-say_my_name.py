#!/usr/bin/python3
"""Module that defines the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    Prints the formatted string "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

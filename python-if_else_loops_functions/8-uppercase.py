#!/usr/bin/python3
def uppercase(s):
    for char in s:
        upper_char = char
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(upper_char), end="")
    print()


if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

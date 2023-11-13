#!/usr/bin/python3

a = 1
b = 2

if __name__ == "__main__":
    add_0 = __import__('add_0')
    resultado = add_0.add(a, b)
    print("{} + {} = {}".format(a, b, resultado))

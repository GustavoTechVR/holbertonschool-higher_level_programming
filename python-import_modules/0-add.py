#!/usr/bin/python3
if _name_ == "_main_":
    a = 1
    b = 2
    exec(open("add_0.py").read())
    print("{} + {} = {}".format(a, b, add(a, b)))

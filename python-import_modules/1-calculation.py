#!/usr/bin/python3
if _name_ == "_main_":
    a = 10
    b = 5

    local_namespace = {}
    exec(open("calculator_1.py").read(), local_namespace, local_namespace)

    add = local_namespace["add"]
    sub = local_namespace["sub"]
    mul = local_namespace["mul"]
    div = local_namespace["div"]

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
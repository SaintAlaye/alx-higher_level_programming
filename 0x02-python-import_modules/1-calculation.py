#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


a = 10
b = 5


def calc():
    """
        function to print the return values
    """
    s1 = add(a, b)
    s2 = sub(a, b)
    s3 = mul(a, b)
    s4 = div(a, b)
    print("{} + {} = {}".format(a, b, s1))
    print("{} + {} = {}".format(a, b, s2))
    print("{} + {} = {}".format(a, b, s3))
    print("{} + {} = {}".format(a, b, s4))


if __name__ == "__main__":
    calc()

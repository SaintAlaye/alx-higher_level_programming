#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


a = 10
b = 5
add(a, b)
sub(a, b)
mul(a, b)
div(a, b)

def calc():
    """
        function to print the return values
    """
    print(a, '+', b, '=', add(a, b))
    print(a, '-', b, '=', sub(a, b))
    print(a, '*', b, '=', mul(a, b))
    print(a, '/', b, '=', div(a, b))


if __name__ == "__main__":
    calc()

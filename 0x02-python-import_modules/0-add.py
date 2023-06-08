#!/usr/bin/python3
from add_0 import add as add_1

a = 1
b = 2
value = add_1(a, b)
def print1():
    """
	    function that print the value
    """
    print("{} + {} = {}".format(a, b, value))

if __name__ == "__main__":
    print1()

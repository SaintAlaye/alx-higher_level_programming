#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ a function to print a list of numbers """
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))

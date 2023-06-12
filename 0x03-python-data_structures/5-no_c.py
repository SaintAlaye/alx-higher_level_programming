#!/usr/bin/python3

def no_c(my_string):
    """ remove a character in a string """
    my_string = "".join([char for char in my_string if char != "c" and char != "C"])
    new_string = my_string
    return new_string

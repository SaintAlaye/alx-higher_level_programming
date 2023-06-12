#!/usr/bin/python3

def no_c(my_string):
    """ remove a character in a string """
    loop = [char for char in my_string if char != "c" and char != "C"]
    my_string = "".join(loop)
    new_string = my_string
    return new_string

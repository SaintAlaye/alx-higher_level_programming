#!/usr/bin/python3

def no_c(my_string):
    """ remove a character in a string """
    for c in my_string:
        if c == "c" and c == "C":
            my_string -= c
            new_string = my_string
            return new_string

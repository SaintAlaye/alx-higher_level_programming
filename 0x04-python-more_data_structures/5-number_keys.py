#!/usr/bin/python3

def number_keys(a_dictionary):
    """ return len of keys in dict """
    num = 0
    list_key = list(a_dictionary.keys())
    for k in list_key:
        num += 1

    return (num)

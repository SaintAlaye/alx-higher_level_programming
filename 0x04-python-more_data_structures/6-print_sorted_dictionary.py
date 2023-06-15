#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ print a sorted dictionary """
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    for k in sorted_keys:
        print("{}: {}".format(k, a_dictionary.get(k)))

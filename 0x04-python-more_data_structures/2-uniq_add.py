#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ adding all the element in a list """
    uniq_list = set(my_list)
    num = 0

    for nums in uniq_list:
        num += nums

    return (num)

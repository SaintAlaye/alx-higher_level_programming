#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """multiply elements by 2 """
    new_dir = a_dictionary.copy()
    new_list = list(new_dir.keys())

    for num in new_list:
        new_dir[num] *= 2

    return (new_dir)

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    list_keys = list(new_dictionary.keys())

    for x in list_keys:
        new_dictionary[x] *= 2

    return (new_dictionary)

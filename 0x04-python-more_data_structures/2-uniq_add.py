#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    number = 0

    for x in unique_list:
        number += x

    return (number)

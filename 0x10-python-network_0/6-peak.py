#!/usr/bin/python3
"""a module that returns the peak value of an unsorted list of integers"""

def find_peak(list_of_integers):
    """Takes a list of integers as argument"""
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length <= 2:
        return max(list_of_integers)



#!/usr/bin/python3
"""A Function that returns True if object is exact"""


def is_same_class(obj, a_class):
    """Retruns True if Object is exactly an Instance, Otherwise False

     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

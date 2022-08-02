#!/usr/bin/python3
"""Defines an objecct attributes lookup function"""


def lookup(obj):
    """A function that returns the list of available attributes"""
    return (dir(obj))

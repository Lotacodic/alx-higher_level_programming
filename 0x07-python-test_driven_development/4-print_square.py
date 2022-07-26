#!/usr/bin/python3

def print_square(size):
    """ A function that prints a square with the character #.
    Args:
        size: is the size length of the square.
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and is less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")

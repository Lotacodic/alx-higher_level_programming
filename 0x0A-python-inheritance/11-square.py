#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"Represents a Square Class Inherited from Rectangle Class"""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print and str representation of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string

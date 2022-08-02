#!/usr/bin/python3
"""A class that inherits from the parent class"""


class MyList(list):
    """A class that inherits from the parent class"""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))

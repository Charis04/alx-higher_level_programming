#!/usr/bin/python3
"""A subclass of a class list."""


class MyList(list):
    """Represents a list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))

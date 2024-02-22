#!/usr/bin/python3
"""Define a class"""


class MyInt(int):
    """A subclass of int that reverses eq and ne"""

    def __eq__(self, other):
        return not (self == other)

    def __ne__(self, other):
        return not (self != other)

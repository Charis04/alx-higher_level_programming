#!/usr/bin/python3
"""A program that gets all available atts and meths."""


def lookup(obj):
    """Gets all available attributes and methods of an object.
    Args:
    obj (obj): The object whose attributes and methods are to be gotten.
    """
    return dir(obj)

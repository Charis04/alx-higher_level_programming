#!/usr/bin/python3
"""A function that checks if an object is an instance of a specific class"""


def is_same_class(obj, a_class):
    """Returns True if obj is instance of class and False otherwise
    Args:
        obj (obj): The object to check if it is an instance of the class.
        a_class (a_class): The class or a tuple of classes to check against.
    Returns:
        True if its and instance an False if otherwise
    """

    if type(obj) is a_class:
        return True
    else:
        return False

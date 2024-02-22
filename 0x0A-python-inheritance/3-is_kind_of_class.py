#!/usr/bin/python3
"""Program a function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a specified class or an instance
    of a subclass of the specified class
    Args:
        obj (obj): object to check
        a_class (a_class): the specified class to check against
    Returns:
        True if it is an instance and False if otherwise
    """

    return isinstance(obj, a_class)

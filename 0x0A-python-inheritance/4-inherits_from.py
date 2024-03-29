#!/usr/bin/python3
"""Program a fucntion"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a specified class"""

    if obj is a_class:
        return False
    for base_class in obj.__class__.__bases__:
        if issubclass(base_class, a_class):
            return True
    return False

#!/usr/bin/python3
"""Program a function"""


def class_to_json(obj):
    """converts a class to a dict description of the obj
    Args:
        obj (obj): obj to convert
    Returns:
        dict
    """

    return vars(obj)

#!/usr/bin/python3
"""Program a funtion"""


import json


def from_json_string(my_str):
    """Decodes a json string to a python object
    Args:
        my_str (my_str): string to be decoded
    Returns:
        python object
    """

    obj = json.loads(my_str)
    return obj

#!/usr/bin/python3
"""Program a function"""


import json


def to_json_string(my_obj):
    """Encodes a python object to Json
    Args:
        my_obj (my_obj): object to be encoded
    Returns:
        Json string
    """

    return str(json.dumps(my_obj))

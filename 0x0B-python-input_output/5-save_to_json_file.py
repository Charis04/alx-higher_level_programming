#!/usr/bin/python3
"""Program a function"""


import json


def save_to_json_file(my_obj, filename):
    """Encodes a python object to json string and writes it to a file
    Args:
        my_obj (my_obj): python object to be encoded
        filename (filename): file to be written to
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

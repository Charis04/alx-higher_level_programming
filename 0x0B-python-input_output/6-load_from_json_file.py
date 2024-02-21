#!/usr/bin/python3
"""Program a function"""


import json


def load_from_json_file(filename):
    """Creates a python object from a json file
    Args:
        filename (filename): json file to be read
    Returns:
        created python object
    """

    with open(filename, encoding='utf-8') as jf:
        content = jf.read()
        content = content.rstrip()
        obj = json.loads(content)
        return obj

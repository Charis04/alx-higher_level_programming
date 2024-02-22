#!/usr/bin/python3
"""A function"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a line of text to a file after occurence of a specified string
    Args:
        filename (filename): file to be written to
        search_string (search_string): specified string
        new_string (new_string): line to append
    """

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

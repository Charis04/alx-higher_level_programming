#!/usr/bin/python3
"""Program a function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns the
    number of characters added

    Args:
        filename (filename): file to be appended to
        text (text): text to append to file
    Returns:
        number of chars appended
    """

    with open(filename, 'a', encoding='utf-8') as f:
        nchars = f.write(txt)

    return nchars

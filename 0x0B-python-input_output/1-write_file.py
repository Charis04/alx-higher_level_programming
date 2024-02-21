#!/usr/bin/python3
"""Program a function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written

    Args:
        filename (filename): file to be written to
        text (text): text to write to the file
    Returns:
        number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        nchars = f.write(text)

    return nchars

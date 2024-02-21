#!/usr/bin/python3
"""Program a fuction"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (filename): name of file to be read
    Returns;
        None
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")

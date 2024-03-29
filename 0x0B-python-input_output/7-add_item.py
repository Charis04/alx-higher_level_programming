#!/usr/bin/python3
"""A program that adds all arguements to a list and saves to a json file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ main fuction of program"""

    ls = get_arg_list(sys.argv)
    filename = "add_item.json"
    try:
        cont = load_from_json_file(filename)
        ls = cont + ls
    except FileNotFoundError:
        pass

    save_to_json_file(ls, filename)


def get_arg_list(args_l):
    """ gets a list of arguements passed to program"""

    a = []
    for i in args_l[1:]:
        a.append(i)
    return a


if __name__ == "__main__":
    main()

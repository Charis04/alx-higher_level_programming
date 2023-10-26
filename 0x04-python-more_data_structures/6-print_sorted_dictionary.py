#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_list = list(a_dictionary.keys().sort())
    for x in key_list:
        print("{}: {}".format(x, a_dictionary.get(x)))

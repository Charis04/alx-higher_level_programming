#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    atarashi_dict = a_dictionary.copy()
    key_list = list(atarashi_dict.keys())

    for x in key_list:
        atarashi_dict[x] *= 2
    return (atarashi_dict)

#!/usr/bin/python3

def no_c(my_string):
    atarashi_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            atarashi_string += elements
    return atarashi_string

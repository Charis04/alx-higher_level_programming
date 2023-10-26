#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    if not my_list:
        return (0)
    dig = 0
    den = 0

    for x in my_list:
        dig += x[0] * x[1]
        den += x[1]

    return (dig / den)

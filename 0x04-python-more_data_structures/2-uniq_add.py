#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    count = 0
    for x in uniq_list:
        count += 1
    return (count)

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    atarashi_list = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            atarashi_list.append(True)
        else:
            atarashi_list.append(False)
    return atarashi_list

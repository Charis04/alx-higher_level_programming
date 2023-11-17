#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        mod = number * -1
    else:
        mod = number

    while mod >= 10:
        mod %= 10
    print(mod, end="")
    return mod

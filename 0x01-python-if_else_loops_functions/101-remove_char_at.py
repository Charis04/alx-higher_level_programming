#!/usr/bin/python3


def remove_char_at(str, n):
    copy = ""
    count = 0
    for i in str:
        if count == n:
            count += 1
            continue
        copy += i
        count += 1
    return copy

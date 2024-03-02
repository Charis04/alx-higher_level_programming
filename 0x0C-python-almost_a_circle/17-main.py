#!/usr/bin/python3
""" 17-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(2)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    s2 = Square.create(**{'size': 2})
    print(s1)
    print(s2)
    print(s1 is s2)
    print(s1 == s2)

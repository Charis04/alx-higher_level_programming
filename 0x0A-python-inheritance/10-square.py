#!/usr/bin/python3
"""Defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representaton of a Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size
        self._width = size
        self._height = size

    def area(self):
        area = self._size * self._size
        return area

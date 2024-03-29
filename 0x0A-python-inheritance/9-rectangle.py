#!/usr/bin/python3
"""Defines A class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a Triangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        area = self._width * self._height
        return area

    def __str__(self):
        return f"[{type(self).__name__}] {self._width}/{self._height}"

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

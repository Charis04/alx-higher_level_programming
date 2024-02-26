#!/usr/bin/python3
"""Defines a class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class that is a subclass of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width is not int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height is not int:
            raise TypeError(f"height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        else:
            self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self._y = y

    def area(self):
        return (self._width * self._height)

    def display(self):
        for i in range(self._height):
            print("#" * self._width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"

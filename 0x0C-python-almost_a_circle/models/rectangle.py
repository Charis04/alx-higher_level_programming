#!/usr/bin/python3
"""Defines a class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class that is a subclass of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if type(width) is not int:
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
        if type(height) is not int:
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
        if type(x) is not int:
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self._y = y

    def area(self):
        return (self._width * self._height)

    def display(self):
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
        """
        instead of
        arg_l = len(args)
        if arg_l > 0:
            self.id = args[0]
        if arg_l > 1:
            self.width = args[1]
        if arg_l > 2:
            self.height = args[2]
        if arg_l > 3:
            self.x = args[3]
        if arg_l > 4:
            self.y = args[4]
        """

    def __str__(self):
        return (
                f"[Rectangle] ({self.id}) {self._x}/{self._y} "
                f"- {self._width}/{self._height}"
                )

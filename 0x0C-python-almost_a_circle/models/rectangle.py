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
        """getter for width"""
        return self._width

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self._width = width

    @property
    def height(self):
        """getter for height"""
        return self._height

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError(f"height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        else:
            self._height = height

    @property
    def x(self):
        """getter for x"""
        return self._x

    @x.setter
    def x(self, x):
        """setter for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self._x = x

    @property
    def y(self):
        """getter for y"""
        return self._y

    @y.setter
    def y(self, y):
        """setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self._y = y

    def area(self):
        """
        Gets the area of the rectangle
        asdklflahdfahdfodiofjiwejfwi

        """
        return (self._width * self._height)

    def display(self):
        """displays shape as hash"""
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def update(self, *args, **kwargs):
        """updates the object attr"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def __str__(self):
        """str overloading"""
        return (
                f"[{type(self).__name__}] ({self.id}) {self._x}/{self._y} "
                f"- {self._width}/{self._height}"
                )

    def to_dictionary(self):
        """a dict representation of the obj"""
        dic = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return dic

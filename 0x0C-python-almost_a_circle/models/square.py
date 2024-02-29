#!/usr/bin/python3
"""Defines a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises the class"""
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """String overloading"""
        return (
                f"[{type(self).__name__}] ({self.id}) {self._x}/{self._y} "
                f"- {self._width}"
                )

    @property
    def size(self):
        """getter for size"""
        return self._width

    @size.setter
    def size(self, size):
        """setter for size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size < 1:
            raise ValueError("width must be > 0")
        else:
            self._width = size
            self._height = size

    def update(self, *args, **kwargs):
        """updates the attributes of the obj"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """converts the object to a dict"""
        dic = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dic

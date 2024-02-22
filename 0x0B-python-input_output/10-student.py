#!/usr/bin/python3
"""Program defines a class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the obj"""

        dict_rep vars(self)
        if attrs is not None:
            dict_rep = {
                    key: value
                    for key, value in dict_rep.items()
                    if key in attrs
                    }
        return dict_rep

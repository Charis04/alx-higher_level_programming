#!/usr/bin/python3
"""Progam a class"""

import json
import csv


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initilises the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to json string"""

        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a file as json string"""

        f_name = f"{cls.__name__}.json"
        content = "[]"
        if list_objs is not None:
            content = []
            for obj in list_objs:
                dic = obj.to_dictionary()
                content.append(dic)
            content = cls.to_json_string(content)

        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """Converts a json string to a list of dictionaries"""

        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a class from a dictionary"""

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a file of json string"""

        f_name = f"{cls.__name__}.json"
        try:
            with open(f_name, 'r', encoding='utf-8') as jf:
                l_dic = cls.from_json_string(jf.read())
        except FileNotFoundError:
            return []

        obj_list = []
        for dic in l_dic:
            obj_list.append(cls.create(**dic))

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects to a CSV file"""

        f_name = f"{cls.__name__}.csv"
        content = []
        if list_objs is not None:
            for obj in list_objs:
                dic = obj.to_dictionary()
                content.append(dic)
        with open(f_name, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=content[0].keys())
            writer.writeheader()
            writer.writerows(content)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of objects from a CSV file"""

        f_name = f"{cls.__name__}.csv"
        try:
            l_dic = []
            with open(f_name, 'r', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row = {key: int(value) for key, value in row.items()}
                    l_dic.append(row)
        except FileNotFoundError:
            return []

        obj_list = []
        for dic in l_dic:
            obj_list.append(cls.create(**dic))

        return obj_list

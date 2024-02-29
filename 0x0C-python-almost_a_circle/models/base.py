#!/usr/bin/python3
"""Progam a class"""

import json


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
        content = []
        if list_objs is not None:
            for obj in list_objs:
                dic = obj.to_dictionary()
                content.append(dic)

        with open(f_name, 'w', encoding='utf-8') as f:
            json.dump(content, f, default=cls.to_json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a json string to a list of dictionaries"""

        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a class from a dictionary"""

        obj = cls(1, 1)
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

    """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        Saves a list of objects to a CSV file

        f_name = f"{cls.__name__}.csv"
        content = []
        if list_objs is not None:
            for obj in list_objs:
                dic = obj.to_dictionary()
                content.append(dic)
            content = pd.DataFrame(content)
        content.to_csv(f_name, index=False)

    @classmethod
    def load_from_file_csv(cls):
        Loads a list of objects from a CSV file

        f_name = f"{cls.__name__}.csv"
        try:
            df = pd.read_csv(f_name)
            l_dic = df.to_dict(orient='records')
        except FileNotFoundError:
            return []

        obj_list = []
        for dic in l_dic:
            obj_list.append(cls.create(**dic))

        return obj_list
    """

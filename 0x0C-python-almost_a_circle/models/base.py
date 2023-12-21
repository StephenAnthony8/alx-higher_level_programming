#!/usr/bin/python3

"""
    Base:
    Module containing the BaseClass 'Base'
    - Answers question 1, 15, 16, 17, 18, 19, 20 & 21
"""
import json


class Base:
    """
    Base:
    - Parent and Ancestor object for Rectangle and Square objects
    - Counts the number of class instances created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            class instance initialization
            id: Object creation number
        """
        # question 1
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # question 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            to_json_string:
            - Static method
            - Returns a JSON string representation of a list(dictionary)

            @list_dictionaries: list to convert to JSON
            Return: JSON string representation
        """
        j_string = []

        if type(list_dictionaries) is list:
            j_string = json.dumps(list_dictionaries)
        else:
            j_string = json.dumps(j_string)

        return (j_string)

    # question 16
    @classmethod
    def save_to_file(cls, list_objs):
        """
            save_to_file:
            - class method
            - converts the instance attributes in list_objs to dictionaries
            - writes to files the instances JSON string representations

            @list_objs: list of instances
        """
        d_args = {}
        d_list = []
        if type(list_objs) is list:
            for i in list_objs:
                if isinstance(i, Base) and type(i) != Base:
                    d_list.append(i.to_dictionary())
                else:
                    continue

        j_list = Base.to_json_string(d_list)

        name = "{}.json".format(cls.__name__)

        with open(name, 'w') as file:
            file.write(j_list)

    # question 17
    @staticmethod
    def from_json_string(json_string):
        """
            from_json_string:
            - static method
            - Converts a JSON string representation back to pythonic syntax

            @json_string: JSON string to be converted
            Return: list of dictionaries
        """
        l_dict = []

        if (type(json_string) == str) and (len(json_string) != 0):
            l_dict = json.loads(json_string)
        return (l_dict)

    # question 18
    @classmethod
    def create(cls, **dictionary):
        """
            create:
            - class method
            - creates an instance of the current class via dummy attributes
                - dummy width, height & size values = 1
            - uses update() to assign correct values

            @dictionary: keyword attribute values
            Return: new instance
        """
        if (cls.__name__ == "Rectangle"):
            new = cls(1, 1)
        elif (cls.__name__ == "Square"):
            new = cls(1)
        new.update(**dictionary)

        return (new)

    # question 19
    @classmethod
    def load_from_file(cls):
        """
            load_from_file:
            - class method
            - reads a JSON file and creates instances from it
                - File name is the class name

            Return: [] on fail or list of instances
        """

        file_name = "{}.json".format(cls.__name__)

        l_instances = []
        try:
            with open(file_name, 'r') as file:
                json_dict = file.read()

        except FileNotFoundError:
            return (l_instances)

        l_dict = cls.from_json_string(json_dict)

        for i in l_dict:
            l_instances.append(cls.create(**i))
        return (l_instances)

    # question 20
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            save_to_file_csv:
            - class method
            - writes to a file of the same class name but in csv format
            - overwrites file if in existence

            @list_objs: list of instances inheriting from base
        """
        ...

    @classmethod
    def load_from_file_csv(cls):
        ...

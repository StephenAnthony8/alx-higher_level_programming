#!/usr/bin/python3
"""
    1!-student.py
    - Contains class 'Student'
"""


class Student:
    """
        Student
        - class object
    """

    def __init__(self, first_name, last_name, age):
        """
        initialization
        public instance attributes
            @first_name: student first name instance attribute
            @last_name: student last name instance attribute
            @age: studnet age instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            to_json - returns a serializable object for class\
                    creation from a JSON file
            attr: parameters to only consider if specified
            Return: a dict of class attributes
        """
        vars_attr = {}
        if type(attr) is list:
            for i in attr:
                try:
                    vars_attr[i] = vars(self)[i]
                except KeyError:
                    continue
            return (vars_attr)
        return (vars(self))

    def reload_from_json(self, json):
        """
            reload_from_json
            - replaces all attributes of the student instace
        """
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])

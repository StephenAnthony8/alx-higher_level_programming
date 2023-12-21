#!/usr/bin/python3
"""
    9-student.py
    - Contains class 'Student'
"""


class Student:
    """
        Student
        - class object
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (vars(self))

#!/usr/bin/python3


"""Write a class Student that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[n], str) for n in attrs):
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()\
                 if key in attrs})

    def reload_from_json(self, json):
        for n in json:
            self.__dict__[n] = json[n]

#!/usr/bin/python3
""" Module contining the class Base. Which acts as the "base" class for al
other classes in the program."""


import json


class Base():
    """Super class for all other classes in the program. Manages the ID of all
    objects."""

    # Class atributes

    __nb_objects = 0

    # Magic methods

    def __init__(self, id=None):
        """Initilization of Base. Sets id to specified value if provided
        otherwise sets the id to the number of objects created"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    # Static Methods

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries to process.
                                      If None or empty, returns "[]"

        """
        str = "[]"
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            str = json.dumps(list_dictionaries)
        return str

    @staticmethod
    def from_json_string(json_string):
        """Static method tat returns a list created
        from a json formated string

        Args:
            json_string (string): String containing a list to be converted from
                                  json format.

        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    # General Methods

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string representation of a
        list of objects.

        Args:
            cls (class): class
            list_objs (list): List of instances which inherit from Base

        """

        with open(cls.__name__ + ".json", mode="w") as f:
            new_list = []
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """Returns and instance that inherited from Base
        with all the atributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file.
        Returns an empty list no file"""
        try:
            with open(cls.__name__ + ".json", mode="r") as f:
                return [cls.create(**obj) for obj in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

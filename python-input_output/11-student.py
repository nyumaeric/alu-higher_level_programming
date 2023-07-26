#!/usr/bin/python3
"""Module containing the class Student"""


class Student():
    """Class that create a student object

    Atributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student

    Methods:
        to_json(self): gets a dictionary representation of a Student

    """

    def __init__(self, first_name, last_name, age):
        """Function that initializes a Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that that retrieves a dictionary
        representation the Student

        Args:
            attrs (list): list of atribute names to return *optional*

        """

        some = {}
        if type(attrs) == list:
            for att in attrs:
                if type(att) != str:
                    return self.__dict__
                if att in self.__dict__:
                    some.update({att: self.__dict__[att]})
            return some
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Function that relaods the dictionary from a json file"""
        if json:
            self.__dict__ = json

if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

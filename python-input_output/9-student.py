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

    def to_json(self):
        """Function that that retrieves a dictionary
        representation the Student"""

        return self.__dict__

if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))

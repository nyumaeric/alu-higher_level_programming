#!/usr/bin/python3
"""Module that contains the class BaseGeometry"""


class BaseGeometry():
    """Class in progress"""

    def area(self):
        """Incomplete method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name(str): name of value
            value(int): value stored at name

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

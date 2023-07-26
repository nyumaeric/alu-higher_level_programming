#!/usr/bin/python3
"""Module that contains the class rectangle, a subclass of BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry that describes a rectangle"""

    def __init__(self, width, height):
        """Initialize the rectangle, validates width and height

        Args:
            width (int): must be greater than 0
            height (int: must be greater than 0

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

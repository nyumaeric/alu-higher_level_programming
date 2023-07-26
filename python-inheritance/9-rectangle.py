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

    def __str__(self):
        """Description of object returned as a string"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Returns the area of the Rectangle"""

        return (self.__width * self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())

#!/usr/bin/python3
"""Module that contains the class Square, a subclass of Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle that describes a Square"""

    def __init__(self, size):
        """Initialize the Square, validates the size

        Args:
            size (int): must be greater than 0

        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Description of object returned as a string"""

        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Method that returns the area of the Square"""

        return (self.__size ** 2)

if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

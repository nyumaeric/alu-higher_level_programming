#!/usr/bin/python3
"""Module containing the class Rectangle, a subclass of Base."""


from models.base import Base


class Rectangle(Base):
    """Class that creates objects the the properties of a rectangle."""


# Magic Methods

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilization method for Rectangle.

        Args:
            width (int): Width of rectangle. Must be > 0.
            height (int): Must be > 0.
            x (int): Must be >= 0.
            y (int): Must be >= 0.

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Method that returns a string representation
        of a Rectangle object."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)


# Getters and setters

    @property
    def width(self):
        """Getter for width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): Must be >= 0

        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): Must be >= 0

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x."""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value (int): Must be >= 0

        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.

        Args:
            value (int): Must be >= 0

        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


# General Methods

    def area(self):
        """Method that returns the area of a Rectangle object."""

        return self.width * self.height

    def display(self):
        """Prints the rectangle make out f #'s to stdout."""

        if self.width > 0 and self.height > 0:
            [print("") for i in range(self.y)]
            [print((' ' * self.x) + ('#' * self.width))
             for j in range(self.height)]

    def update(self, *args, **kwargs):
        """Method to update the attributes of a Rectangle object.

        Args:
            1st (int): Must be >= 0. Represents the id attribute.
            2nd (int): Must be >= 0. Represents the width attribute.
            3rd (int): Must be >= 0. Represents the height attribute.
            4th (int): Must be >= 0. Represents the x attribute.
            5th (int): Must be >= 0. Represents the y attribute.

        """
        if len(args) > 5:
            raise Exception("Too many arguments")
        if len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                if arg == 1:
                    self.width = args[1]
                if arg == 2:
                    self.height = args[2]
                if arg == 3:
                    self.x = args[3]
                if arg == 4:
                    self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representaion of the Rectangle"""

        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

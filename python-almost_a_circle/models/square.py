#!/usr/bin/python3
"""Module that contains the class Square, a subclass of Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines square objects."""

    # Magic methods

    def __init__(self, size, x=0, y=0, id=None):
        """Initilization method of a square

        Args:
            size (int): Width and height of the square. Must be >= 0.
            x (int): Horizontal offset of square. Must be >= 0
            y (int): Verticle offset of square. Must be >= 0
            id (int): Attribute of Base class identifying obejct.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string representation of the Square"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    # Getters and setters

    @property
    def size(self):
        """Method that returns the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """Method that sets the size of the square"""

        self.width = value
        self.height = value

    # General methods

    def update(self, *args, **kwargs):
        """Method to update the attributes of a Rectangle object.

        Args:
            1st (int): Must be >= 0. Represents the id attribute.
            2nd (int): Must be >= 0. Size, represents the width
                       and height attribute.
            3rd (int): Must be >= 0. Represents the x attribute.
            4th (int): Must be >= 0. Represents the y attribute.
        """

        if len(args) > 4:
            raise Exception("Too many arguments")
        if len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                if arg == 1:
                    self.width, self.height = args[1], args[1]
                if arg == 2:
                    self.x = args[2]
                if arg == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representaion of the Square"""

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

#!/usr/bin/python3
""" Defines a Rectangle class."""


class Rectangle:
    """ Represents a rectangle.

    Args:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the width of the new rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the new rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the height of the new rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of our rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Perimeter of our rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Return the printable representation of the rectangle.

        Represents the rectangle with the # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ Return the string representation of the new rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ Print a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

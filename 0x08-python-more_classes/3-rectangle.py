#!/usr/bin/python3
"""
Define a rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.

        Args:
            width (int): The width of a rectangle.
            height (int): The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of a rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of our Rectangle. """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Perimeter of our rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        Returns the printable represetation of the Rectangle.

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

#!/usr/bin/python3
"""
Define a square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter for the current size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints in stdout the square with # character.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

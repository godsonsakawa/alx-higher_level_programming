#!/usr/bin/python3

"""Print all possible different combinations of two digits
   `01` and `10` are considered same combo of the two digits `0` and `1`
"""
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        if (digit1 != 8 or digit != 9):
            print("{}{}, ".format(digit1, digit2), end="")
        else:
            print("{}{}".format(digit1, digit2))

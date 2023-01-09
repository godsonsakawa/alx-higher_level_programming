#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers
    """
    """for row in matrix:
        print("{:d} {:d} {:d}".format(row[0], row[1], row[2]))
    else:
        print("")
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d}".format(matrix[row][col]), end="")
            if col != (len(matrix[row]) - 1):
                print(" ", end="")

        print("")

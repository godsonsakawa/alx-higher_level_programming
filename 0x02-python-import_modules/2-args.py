#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of and the list of its arguments.
    """
    import sys
    count_args = len(sys.argv) - 1
    if (count_args == 0):
        print("0 arguments.")
    elif (count_args == 1):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count_args))
    for argNo in range(count_args):
        print("{}: {}".format(argNo + 1, sys.argv[argNo + 1]))

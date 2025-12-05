#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == [[]]:
        print()
        return

    for row in matrix:
        for index, value in enumerate(row):
            if index != 0:
                print(" ", end="")
            print("{:d}".format(value), end="")
        print()

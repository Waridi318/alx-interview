#!/usr/bin/python3
"""
This module creates generates the Pascal's triangle in python
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal's triangle of n
    """

    triangle = []
    if n > 0:
        for i in range(n):
            row = [1] * (i + 1)
            for k in range(1, i):
                new_row = triangle[i - 1]

                row[k] = new_row[k - 1] + new_row[k]
            triangle.append(row)

    return(triangle)

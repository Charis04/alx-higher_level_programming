#!/usr/bin/python3
"""Program that codes pascal's triangle"""


def pascal_triangle(n):
    """Generates a pascal's triangle in form of a nested list"""

    triangle = []

    for row_num in range(n):
        row = []
        for col_num in range(row_num + 1):
            if col_num == 0 or col_num == row_num:
                row.append(1)
            else:
                value = (
                        triangle[row_num - 1][col_num - 1]
                        +
                        triangle[row_num - 1][col_num]
                        )
                row.append(value)
        triangle.append(row)

    return triangle

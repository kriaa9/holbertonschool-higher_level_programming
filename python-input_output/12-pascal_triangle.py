#!/usr/bin/python3
"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n: Number of rows to generate.

    Returns:
        List of lists representing Pascal's triangle.
        Empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

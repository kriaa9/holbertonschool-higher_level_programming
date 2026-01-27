#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It includes robust error handling for input validation.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).
    
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.
        
    Returns:
        A new matrix with the result of the division rounded to 2 decimal places.
        
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # 1. Validate 'div'
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Error message for matrix validation
    type_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    # 2. Validate 'matrix' structure and content
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_err_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_err_msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(type_err_msg)

    # 3. Validate row sizes
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Perform division
    new_matrix = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)

    return new_matrix

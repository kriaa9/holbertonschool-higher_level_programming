#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number.

    Args:
        number: The number to extract the last digit from

    Returns:
        The last digit of the number
    """
    last = abs(number) % 10
    print(last, end='')
    return last

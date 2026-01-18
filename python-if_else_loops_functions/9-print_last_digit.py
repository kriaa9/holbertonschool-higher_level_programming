#!/usr/bin/python3
"""Provide `print_last_digit(number)` to print and return a last digit.

The last digit is computed with `abs(number) % 10` so that negatives
produce the expected positive digit while printing matches the tasks.
"""
def print_last_digit(number):
    """Print and return the last digit of a number.

    Args:
        number: The number to extract the last digit from

    Returns:
        The last digit of the number
    """
    # Use abs(number) % 10 to handle negative inputs predictably
    last = abs(number) % 10
    print(last, end='')
    return last

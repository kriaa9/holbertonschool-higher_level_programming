#!/usr/bin/python3
"""Print a random number's last digit and describe its value.

This script generates a random integer in [-10000, 10000], computes its
last digit, then prints whether that last digit is greater than 5, equal
to 0, or less than 6 and not 0. It also handles negatives correctly.
"""
import random

number = random.randint(-10000, 10000)
# Compute last digit. Python's modulo on negatives is non-intuitive.
# Example: -12 % 10 == 8. We'll adjust below for negative numbers.
last_digit = number % 10

if number < 0:
    # For negative numbers, ensure the last digit carries the sign
    # Expected: last digit of -626 is -6
    last_digit = -(-number % 10)

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is " +
          "less than 6 and not 0")
